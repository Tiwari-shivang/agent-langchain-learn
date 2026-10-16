"""Import every model so its table is registered with Base.metadata."""

from app.db.models.users import Users, UserPreference
from app.db.models.account import Account, Wallet, Portfolio, Holdings, Trade, Stock

__all__ = [
    "Users", "UserPreference", "Account", "Wallet",
    "Portfolio", "Holdings", "Trade", "Stock",
]
