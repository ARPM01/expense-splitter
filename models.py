from typing import List

class User:
    def __init__(self, name: str):
        """
        Initializes a User object with a name and an empty list of expenses.

        Parameters
        ----------
            name : str
                a string representing the user's name
        """
        self.name = name
        self.expenses = []
        
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
            paid_by : User
                a User object representing the user who paid for the expense
            owed_by : list
                a list of User objects representing the users who owe money for the expense
            settled : bool
                a boolean representing whether the expense has been settled
                
        """
        self.title = title
        self.amount = amount
        self.paid_by = paid_by
        self.settled = False

