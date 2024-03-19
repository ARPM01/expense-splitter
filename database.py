from sqlalchemy import create_engine, insert, select, delete, update
from sqlalchemy import MetaData
from sqlalchemy import text
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.orm import Session
from typing import Optional, List


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

    # name = "HMF"
    # stmt = select(User.id).where(User.name == name)

    # with Session(engine) as session:
    #     result = session.execute(stmt)
    #     print(result.scalars().first())

    stmt = select(User)
    stmt2 = select(Expense)

    with Session(engine) as session:
        result = session.execute(stmt).scalars().all()
        result2 = session.execute(stmt2).scalars().all()
        print(result, result2)
