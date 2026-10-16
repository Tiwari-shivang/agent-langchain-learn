from app.db.base import Base
from uuid import UUID
from sqlalchemy import UUID as PGUUID, text, ForeignKey, String, Boolean, Numeric, BigInteger, Enum as PG_Enum
from sqlalchemy.orm import Mapped, mapped_column
from decimal import Decimal
from datetime import datetime
from app.db.models.users import currencyEnum
import enum

class OrderTypeEnum(str, enum.Enum):
    BUY = "buy"
    SELL = "sell"


class Account(Base):
    __tablename__="accounts"
    __table_args__={"schema": "Users"}
    id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
    user_id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), ForeignKey("Users.users.id"), nullable=False)
    account_number: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    bank_name: Mapped[str] = mapped_column(String, nullable=False)
    account_type: Mapped[str] = mapped_column(String, nullable=False)
    amount: Mapped[Decimal] = mapped_column(Numeric, server_default=text("0"))
    is_active: Mapped[bool] = mapped_column(Boolean, server_default=text("true"))
    added_on: Mapped[datetime] = mapped_column(server_default=text("now()"))
    default_currency: Mapped[currencyEnum] = mapped_column(PG_Enum(currencyEnum), server_default=text("'INR'"))
    created_at: Mapped[datetime] = mapped_column(server_default=text("now()"))
    updated_at: Mapped[datetime] = mapped_column(server_default=text("now()"))


class Wallet(Base):
    __tablename__="wallets"
    __table_args__={"schema": "Users"}
    id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
    account_id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), ForeignKey("Users.accounts.id"), nullable=False)
    wallet_name: Mapped[str] = mapped_column(String)
    balance: Mapped[Decimal] = mapped_column(Numeric, server_default=text("0"))
    is_active: Mapped[bool] = mapped_column(Boolean, server_default=text("true"))
    created_at: Mapped[datetime] = mapped_column(server_default=text("now()"))
    updated_at: Mapped[datetime] = mapped_column(server_default=text("now()"))

class Portfolio(Base):
    __tablename__="portfolio"
    __table_args__={"schema": "Users"}
    id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
    user_id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), ForeignKey("Users.users.id"), nullable=False)
    description: Mapped[str] = mapped_column(String, server_default="Portfolio basic")
    total_invested_value: Mapped[Decimal] = mapped_column(Numeric, server_default=text("0"))
    current_value: Mapped[Decimal] = mapped_column(Numeric, server_default=text("0"))
    total_pnl: Mapped[Decimal] = mapped_column(Numeric, server_default=text("0"))
    pnl_percentage: Mapped[Decimal] = mapped_column(Numeric, server_default=text("0"))
    max_drawdown_limit: Mapped[Decimal] = mapped_column(Numeric, server_default=text("0"))
    is_active: Mapped[bool] = mapped_column(Boolean, server_default=text("true"))
    created_at: Mapped[datetime] = mapped_column(server_default=text("now()"))
    updated_at: Mapped[datetime] = mapped_column(server_default=text("now()"))

class Holdings(Base):
    __tablename__="holdings"
    __table_args__={"schema": "Users"}
    id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
    portfolio_id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), ForeignKey("Users.portfolio.id"), nullable=False)
    symbol: Mapped[str] = mapped_column(String, nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False)
    quantity: Mapped[int] = mapped_column(Numeric, nullable=False)
    created_at: Mapped[datetime] = mapped_column(server_default=text("now()"))
    updated_at: Mapped[datetime] = mapped_column(server_default=text("now()"))

class Trade(Base):
    __tablename__="trades"
    __table_args__={"schema": "Market"}
    id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
    portfolio_id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), ForeignKey("Users.portfolio.id"), nullable=False)
    symbol: Mapped[str] = mapped_column(String, nullable=False)
    order_type: Mapped[OrderTypeEnum] = mapped_column(PG_Enum(OrderTypeEnum), nullable=False)
    quantity: Mapped[int] = mapped_column(Numeric, nullable=False)
    execution_price: Mapped[int] = mapped_column(Numeric, nullable=False)
    reasoning: Mapped[str] = mapped_column(String)
    created_at: Mapped[datetime] = mapped_column(server_default=text("now()"))
    updated_at: Mapped[datetime] = mapped_column(server_default=text("now()"))

class Stock(Base):
    __tablename__="stocks"
    __table_args__={"schema": "Market"}
    id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
    symbol: Mapped[str] = mapped_column(String, nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False)
    sector: Mapped[str] = mapped_column(String, nullable=False)
    current_price: Mapped[Decimal] = mapped_column(Numeric, server_default=text("0"))
    previous_close: Mapped[Decimal] = mapped_column(Numeric, server_default=text("0"))
    day_high: Mapped[Decimal] = mapped_column(Numeric, server_default=text("0"))
    day_low: Mapped[Decimal] = mapped_column(Numeric, server_default=text("0"))
    volume: Mapped[int] = mapped_column(BigInteger, server_default=text("0"))
    created_at: Mapped[datetime] = mapped_column(server_default=text("now()"))
    updated_at: Mapped[datetime] = mapped_column(server_default=text("now()"))

