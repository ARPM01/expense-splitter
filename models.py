from typing import List
import random


# TODO: Implement a database to store user and expense data
# TODO: Organize models into separate files
class User:
    def __init__(self, name: str, id: int):
        """
        Initializes a User object with a name, id, and an empty list of expenses.

        Parameters
        ----------
            name : str
                a string representing the user's name
            id : int
                a int representing the user's id
        """
        self.name = name
        # TODO: This id is temporary. Use database to generate unique ids.
        self.id = id
        self.expenses = []

    def __str__(self) -> str:
        return self.name


class Expense:
    def __init__(self, title: str, amount: float, paid_by: User, owed_by: List[User]):
        """
        Initializes an Expense object with title, amount, paid_by, and settled attributes.

        Parameters
        ----------
            title : str
                a string representing the title of the expense
            amount : float
                a float representing the amount of the expense
            paid_by : int
                a int representing the id of a User object who paid for the expense
            owed_by : list
                a list of User objects representing the users who owe money for the expense
            settled : bool
                a boolean representing whether the expense has been settled

        """
        self.title = title
        self.amount = amount
        self.paid_by = paid_by
        self.settled = False

        self.user_paid_by = self.__get_user_paid_by()

    def __get_user_paid_by(self) -> User:
        # TODO: Implement user search in database
        for user in users:
            if user.id == int(self.paid_by):
                return user


expenses = []
users = [
    User("ARPM", id=1),
    User("HMF", id=2),
]
