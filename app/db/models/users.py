from app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from uuid import UUID
from sqlalchemy import UUID as PGUUID, text, String, Enum as PG_Enum
from datetime import datetime
import enum

class themeEnum(str, enum.Enum):
    DARK = "dark"
    LIGHT = "light"

class currencyEnum(str, enum.Enum):
    INR = "inr"
    USD = "usd"
    EUR = "eur"

class Users(Base):
    __tablename__="users"
    __table_args__={"schema": "Users"}
    id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
    first_name: Mapped[str] = mapped_column(String(100), nullable=False)
    last_name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)
    password_hash: Mapped[str] = mapped_column(String, nullable=False)
    auth_source: Mapped[str] = mapped_column(String, server_default="basic")
    date_of_birth: Mapped[str] = mapped_column(String(12), nullable=False)
    gender: Mapped[str] = mapped_column(String(10), nullable=False)
    country: Mapped[str] = mapped_column(String(100), nullable=False)
    city: Mapped[str] = mapped_column(String(100), nullable=False)
    created_at: Mapped[datetime] = mapped_column(nullable=False, server_default=text("now()"))
    updated_at: Mapped[datetime] = mapped_column(nullable=False, server_default=text("now()"))

class UserPreference(Base):
    __tablename__="preferences"
    __table_args__={"schema": "Users"}
    id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
    theme: Mapped[themeEnum] = mapped_column(PG_Enum(themeEnum), server_default=text("'DARK'"))
    selected_currency: Mapped[currencyEnum] = mapped_column(PG_Enum(currencyEnum), server_default=text("'INR'"))
