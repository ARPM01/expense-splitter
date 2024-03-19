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
    Base class for mapping
    """

    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r})"


class Expense(Base):
    __tablename__ = "expenses"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    owed = mapped_column(ForeignKey("users.id"))
    value: Mapped[float] = mapped_column()
    split: Mapped[bool] = mapped_column()
    settled: Mapped[bool] = mapped_column()


if __name__ == "__main__":
    engine = create_engine("sqlite+pysqlite:///database.db", echo=True)
    Base.metadata.create_all(engine)

    # stmt = insert(User).values([{"name": "ARPM"}, {"name": "HMF"}])

    # with Session(engine) as session:
    #     result = session.execute(stmt)
    #     session.commit()

    # stmt = insert(Expense).values(
    #     [{"name": "Water", "owed": 1, "value": 30, "split": True, "settled": False}]
    # )

    # with Session(engine) as session:
    #     session.execute(stmt)
    #     session.commit()

    # stmt = select(Expense)

    # with Session(engine) as session:
    #     result = session.execute(stmt).scalars().all()
    #     print(result)
