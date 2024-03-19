from typing import List, Optional
from sqlalchemy import create_engine, insert, text, select, update, delete
from sqlalchemy import Table, Column, Integer, ForeignKey, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.orm import Session

import random


# TODO: Implement a database to store user and expense data
# TODO: Organize models into separate files


class Base(DeclarativeBase):
    """
    SQLAlchemy subclassing DeclarativeBase for defining ORM classes.
    """

    pass


class User(Base):
    """
    A SQLAlchemy Declarative Base class representing a user with associated attributes.

    Attributes
    ----------
    id : Mapped[int]
        A primary key column in the database, representing the user's ID.
    name : Mapped[str]
        A column in the database representing the user's name.

    Methods
    -------
    __repr__() -> str
        Represent the User instance as a string.
    """

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r})"


class Expense(Base):
    """
    A SQLAlchemy Declarative Base class representing an expense.

    Attributes
    ----------
    id : Mapped[int]
        A primary key column in the database, representing the expense's ID.
    name : Mapped[str]
        A column in the database representing the name of the expense.
    owed : Mapped[int]
        A foreign key column pointing to the User ID who owes this expense.
    value : Mapped[float]
        A column in the database storing the value of the expense.
    split : Mapped[bool]
        A Boolean column indicating whether the expense is to be split.
    settled : Mapped[bool]
        A Boolean column indicating whether the expense has been settled.

    Methods
    -------
    __repr__() -> str
        Represent the Expense instance as a string.
    """

    __tablename__ = "expenses"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    owed = mapped_column(ForeignKey("users.id"))
    value: Mapped[float] = mapped_column()
    split: Mapped[bool] = mapped_column()
    settled: Mapped[bool] = mapped_column()

    def __repr__(self) -> str:
        return f"Expense(name={self.name!r}, value={self.value!r})"
