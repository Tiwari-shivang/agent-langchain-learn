import importlib
import unittest
from contextlib import asynccontextmanager
from unittest.mock import AsyncMock, patch

from sqlalchemy import create_mock_engine
from sqlalchemy.schema import CreateSchema


application = importlib.import_module("app.main")
Base = application.Base


class DatabaseSchemaTests(unittest.TestCase):
    def test_app_import_registers_all_tables_and_resolves_foreign_keys(self):
        self.assertEqual(
            set(Base.metadata.tables),
            {
                "Users.users", "Users.preferences", "Users.accounts",
                "Users.wallets", "Users.portfolio", "Users.holdings",
                "Market.trades", "Market.stocks",
            },
        )
        for table in Base.metadata.sorted_tables:
            for foreign_key in table.foreign_keys:
                self.assertIn(foreign_key.column.table.key, Base.metadata.tables)

    def test_postgresql_ddl_and_defaults(self):
        statements = []
        engine = create_mock_engine(
            "postgresql+asyncpg://",
            lambda sql, *args, **kwargs: statements.append(
                str(sql.compile(dialect=engine.dialect))
            ),
        )
        Base.metadata.create_all(engine, checkfirst=False)
        self.assertEqual(sum("CREATE TABLE" in sql for sql in statements), 8)
        for table in Base.metadata.tables.values():
            self.assertEqual(str(table.c.id.server_default.arg), "gen_random_uuid()")
            for column in table.columns:
                if hasattr(column.type, "enums") and column.server_default is not None:
                    label = str(column.server_default.arg).strip("'")
                    self.assertIn(label, column.type.enums)


class StartupTests(unittest.IsolatedAsyncioTestCase):
    async def test_schemas_are_created_before_tables_and_engine_is_disposed(self):
        events = []

        async def execute(statement):
            self.assertIsInstance(statement, CreateSchema)
            self.assertTrue(statement.if_not_exists)
            events.append(statement.element)

        async def run_sync(callback):
            self.assertEqual(callback, Base.metadata.create_all)
            events.append("tables")

        connection = AsyncMock()
        connection.execute.side_effect = execute
        connection.run_sync.side_effect = run_sync

        @asynccontextmanager
        async def begin():
            yield connection

        engine = AsyncMock()
        engine.begin = begin
        with patch.object(application, "engineLocal", engine), patch.object(
            application, "test_db_connection", new_callable=AsyncMock
        ):
            async with application.life_span(application.app):
                self.assertEqual(events, ["Market", "Users", "tables"])
            engine.dispose.assert_awaited_once()


if __name__ == "__main__":
    unittest.main()
