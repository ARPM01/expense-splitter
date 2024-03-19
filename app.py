from flask import Flask, jsonify, render_template, request, redirect, url_for

from models import Base, Expense, User
from sqlalchemy import create_engine, insert, select, update, delete
from sqlalchemy.orm import Session


class ExpenseSplitterApp:
    def __init__(self):
        self.app = Flask(__name__, template_folder="templates")
        self.setup_routes()
        self.engine = create_engine("sqlite+pysqlite:///database.db", echo=True)
        self.metadata = Base.metadata
        self.metadata.create_all(self.engine)
        self.__update_lists()

    def get_user_paid_by(self, expense):
        """
        Get name of user who paid.
        """
        stmt = select(User.name).where(User.id == expense.owed)
        with Session(self.engine) as session:
            result = session.execute(stmt).scalars().first()

        return result

    def run(self):
        """
        Runs the Flask app on port 5000.
        """
        self.app.run(host="0.0.0.0", debug=True)

    def update_users(self):
        """
        Update user list
        """
        stmt = select(User)
        with Session(self.engine) as session:
            result = session.execute(stmt).scalars().all()
            self.users_list = result

    def update_expenses(self):
        """
        Update expense list
        """
        stmt = select(Expense)
        with Session(self.engine) as session:
            result = session.execute(stmt).scalars().all()
            self.expenses_list = result

    def __update_lists(self):
        """
        Update expense and user list
        """
        self.update_expenses()
        self.update_users()

    def setup_routes(self):
        """
        Sets up the routes for the Flask app.
        """

        @self.app.route("/")
        def root():
            return redirect(url_for("home"))

        @self.app.route("/home")
        def home():
            return render_template("home.html", active_page="home")

        @self.app.route("/expenses")
        def expenses():
            """
            Renders the expenses page with the list of expenses and users.
            """

            self.__update_lists()

            return render_template(
                "expenses.html",
                expenses=self.expenses_list,
                users=self.users_list,
                active_page="expenses",
                app=self,
            )

        @self.app.route("/users")
        def users():
            """
            Renders the users page with the list of expenses and users.
            """

            self.__update_lists()

            return render_template(
                "users.html",
                expenses=self.expenses_list,
                users=self.users_list,
                active_page="users",
                app=self,
            )

        @self.app.route("/create", methods=["POST"])
        def create():
            """
            Creates a new expense entry and adds it to the list of expenses.
            """
            expense_name = request.form["name"]
            expense_amount = request.form["amount"]
            expense_paid_by = request.form["paidBy"]
            expense_equally_split = request.form.get("equallySplit") is not None

            get_user_id = select(User.id).where(User.name == expense_paid_by)

            stmt = insert(Expense)

            with Session(self.engine) as session:
                result = session.execute(get_user_id)
                id = result.scalars().first()
                result = session.execute(
                    stmt,
                    [
                        {
                            "name": expense_name,
                            "owed": id,
                            "value": expense_amount,
                            "split": expense_equally_split,
                            "settled": False,
                        }
                    ],
                )
                session.commit()

            self.__update_lists()

            return redirect(url_for("expenses"))

        @self.app.route("/remove/<int:index>")
        def remove(index):
            """
            Deletes an expense from the list of expenses.
            """

            target = self.expenses_list[index]
            # need to convert index to expense ID
            stmt = delete(Expense).where(Expense.id == target.id)

            with Session(self.engine) as session:
                result = session.execute(stmt)
                session.commit()

            self.__update_lists()

            return redirect(url_for("expenses"))

        @self.app.route("/modify/<int:index>", methods=["POST"])
        def modify(index):
            """
            Modifies an expense from the list of expenses.
            """

            target = self.expenses_list[index]

            try:
                expense_selected = get_expense(index)
            except IndexError:
                return redirect(url_for("home"))

            name = request.form["newName"]
            value = request.form["newAmount"]
            owed = request.form["newPaidBy"]
            split = request.form.get("newEquallySplit") is not None

            stmt = (
                update(Expense)
                .where(Expense.id == target.id)
                .values(
                    name=name,
                    value=value,
                    owed=owed,
                    split=split,
                )
            )

            with Session(self.engine) as session:
                result = session.execute(stmt)
                session.commit()

            self.__update_lists()

            return redirect(url_for("expenses"))

        @self.app.route("/settle/<int:index>")
        def settle(index):
            """
            Changes the settled status of an expense from the list of expenses.
            """

            target = self.expenses_list[index]

            stmt = select(Expense).where(Expense.id == target.id)
            with Session(self.engine) as session:
                result = session.execute(stmt).scalars().first()

            if result is None:
                return redirect(url_for("home"))

            stmt = update(Expense).where(Expense.id == target.id).values(settled=True)
            with Session(self.engine) as session:
                result = session.execute(stmt)
                session.commit()

            self.__update_lists()

            # TODO: Move settled expenses to the bottom of the list.
            return redirect(url_for("expenses"))

        @self.app.route("/expense/<int:id>", methods=["GET"])
        def get_expense(index):
            """
            Returns the jsonified expense object with the given index.
            """

            target = self.expenses_list[index]

            stmt = select(Expense).where(Expense.id == target.id)

            with Session(self.engine) as session:
                result = session.execute(stmt).scalars().first()
                expense_dict = {
                    k: v for k, v in result.__dict__.items() if not k.startswith("_sa_")
                }
                return jsonify(expense_dict)


if __name__ == "__main__":
    ExpenseSplitter = ExpenseSplitterApp()
    ExpenseSplitter.run()
