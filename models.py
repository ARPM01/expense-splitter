from typing import List, Optional
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, ForeignKey, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column, relationship

import random


# TODO: Implement a database to store user and expense data
# TODO: Organize models into separate files

engine = create_engine("sqlite+pysqlite:///test.db", echo=True)


class Base(DeclarativeBase):
    """
    Base class for mapping
    """

    pass


# user_group_association = Table(
#     "user_group_association",
#     Base.metadata,
#     Column("user_id", Integer, ForeignKey("users.id")),
#     Column("group_id", Integer, ForeignKey("groups.id")),
# )


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]

    groups: Mapped[List["Group"]] = relationship("Group", back_populates="members")

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r})"


class Group(Base):
    __tablename__ = "groups"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))

    members: Mapped[List["User"]] = relationship("User", back_populates="groups")

    def __repr__(self) -> str:
        return f"Group(id={self.id!r}, name={self.name!r})"


class Expense(Base):
    __tablename__ = "expenses"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    owed = mapped_column(ForeignKey("users.id"))
    currency: Mapped[str] = mapped_column(String(3))
    value: Mapped[float] = mapped_column()

    ower: Mapped[List["User"]] = relationship("User")


Base.metadata.create_all(engine)
