from flask import Flask, jsonify, render_template, request, redirect, url_for

from models import Base, Expense, User, users_list, expenses_list
from sqlalchemy import create_engine, insert, select, update, delete
from sqlalchemy.orm import Session


class ExpenseSplitterApp:
    def __init__(self):
        self.app = Flask(__name__, template_folder="templates")
        self.setup_routes()
        self.engine = create_engine("sqlite+pysqlite:///database.db", echo=True)
        self.metadata = Base.metadata
        self.metadata.create_all(self.engine)

    def run(self):
        """
        Runs the Flask app on port 5000.
        """
        self.app.run(host="0.0.0.0", debug=True)

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
            return render_template(
                "expenses.html",
                expenses=expenses_list,
                users=users_list,
                active_page="expenses",
            )

        @self.app.route("/users")
        def users():
            """
            Renders the users page with the list of expenses and users.
            """

            return render_template(
                "users.html",
                expenses=expenses_list,
                users=users_list,
                active_page="users",
            )

        @self.app.route("/create", methods=["POST"])
        def create():
            """
            Creates a new expense entry and adds it to the list of expenses.
            """
            expense_name = request.form["name"]
            expense_amount = request.form["amount"]
            expense_paid_by = request.form["paidBy"]
            expense_equally_split = request.form.get("equallySplit")

            get_user_id = select(User.id).where(User.name == expense_paid_by)

            stmt = insert(Expense)

            with Session(self.engine) as session:
                id = session.scalars(get_user_id)
                result = session.execute(
                    stmt,
                    [
                        {
                            "name": expense_name,
                            "owed": id,
                            "value": expense_amount,
                            "split": expense_equally_split,
                        }
                    ],
                )
                session.commit()

            return redirect(url_for("expenses"))

        @self.app.route("/delete/<int:index>")
        def delete(index):
            """
            Deletes an expense from the list of expenses.
            """
            if len(expenses_list) > index:
                del expenses_list[index]
            return redirect(url_for("expenses"))

        @self.app.route("/modify/<int:index>", methods=["POST"])
        def modify(index):
            """
            Modifies an expense from the list of expenses.
            """
            try:
                expense_selected = get_expense
            except IndexError:
                return redirect(url_for("home"))
            expense_selected.title = request.form["newName"]
            expense_selected.amount = request.form["newAmount"]
            expense_selected.paid_by = request.form["newPaidBy"]
            expense_selected.equally_split = request.form.get("newEquallySplit")

            return redirect(url_for("expenses"))

        @self.app.route("/settle/<int:index>")
        def settle(index):
            """
            Changes the settled status of an expense from the list of expenses.
            """
            try:
                expense_selected = expenses_list[index]
            except IndexError:
                return redirect(url_for("home"))
            expense_selected.settled = True
            # TODO: Move settled expenses to the bottom of the list.
            return redirect(url_for("expenses"))

        @self.app.route("/expense/<int:id>", methods=["GET"])
        def get_expense(id):
            """
            Returns the jsonified expense object with the given id.
            """
            expense = expenses_list[id]
            print(expense.__dict__)
            return jsonify(expense.__dict__)


if __name__ == "__main__":
    ExpenseSplitter = ExpenseSplitterApp()
    ExpenseSplitter.run()
