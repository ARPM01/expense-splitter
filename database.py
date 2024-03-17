from sqlalchemy import create_engine, insert
from sqlalchemy import MetaData
from sqlalchemy import text
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional, List

# engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)


class Base(DeclarativeBase):
    """
    Base class for mapping
    """

    pass


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
    split: Mapped[bool] = mapped_column()


# Base.metadata.create_all(engine)


# stmt = insert(Expense).values(
#     name="Food", owed="HMF", currency="PHP", value="500", split=0
# )

# compiled = stmt.compile()

# with engine.connect() as conn:
#     result = conn.execute(stmt)
#     conn.commit()

# with engine.connect() as conn:
#     result = conn.execute(text("SELECT id FROM expenses ORDER BY id DESC LIMIT 1"))

# print(len(result.all()))

# if len(result.all()) == 0:
#     print("True")

# with engine.connect() as conn:
#     result = conn.execute(text("SELECT * FROM expenses"))
#     print(result.all())
