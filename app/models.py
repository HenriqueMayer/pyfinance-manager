from datetime import date
from decimal import Decimal
from enum import Enum
from typing import List, Optional

from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import Column
from sqlalchemy.types import Numeric
from pydantic import field_validator


class TransactionType(str, Enum):
    INCOME = "income"
    EXPENSE = "expense"
    TRANSFER = "transfer"


class AccountType(str, Enum):
    CHECKING = "checking"
    SAVINGS = "savings"
    CREDIT = "credit"
    CASH = "cash"
    INVESTMENT = "investment"


class Category(SQLModel, table=True):
    """Category model for classifying transactions."""

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    description: Optional[str] = None

    transactions: List["Transaction"] = Relationship(back_populates="category")


class Account(SQLModel, table=True):
    """Account model representing a financial account."""

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    account_type: AccountType

    transactions: List["Transaction"] = Relationship(back_populates="account")


class Transaction(SQLModel, table=True):
    """Transaction model representing a financial transaction."""

    id: Optional[int] = Field(default=None, primary_key=True)
    date: date
    description: str
    # Store monetary values with fixed precision (10,2)
    amount: Decimal = Field(sa_column=Column(Numeric(10, 2)))
    type: TransactionType

    account_id: Optional[int] = Field(default=None, foreign_key="account.id")
    category_id: Optional[int] = Field(default=None, foreign_key="category.id")

    account: Optional[Account] = Relationship(back_populates="transactions")
    category: Optional["Category"] = Relationship(back_populates="transactions")

    @field_validator("amount")
    @classmethod
    def validate_positive_amount(cls, value):
        """
        Ensures the amount is always greater than zero.
        If it's an expense, the 'EXPENSE' type will handle the logic,
        but the raw number must be positive.
        """
        if value <= 0:
            raise ValueError(
                "Transaction amount must be positive and greater than zero."
            )
        return value

    @field_validator("description")
    @classmethod
    def validate_description(cls, value):
        """
        Ensures the description is not empty or whitespace-only.
        """
        if not value.strip():
            raise ValueError("Description cannot be empty.")
        return value.strip()
