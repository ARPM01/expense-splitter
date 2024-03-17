from flask import Flask, jsonify, render_template, request, redirect, url_for

from models import Expense, User, users, expenses

# TODO: Research on how to make this OOP.

app = Flask(__name__, template_folder="templates")


@app.route("/")
def root():
    return redirect(url_for("home"))


@app.route("/home")
def home():
    return render_template(
        "home.html",
        expenses=expenses,
        users=users,
    )


@app.route("/create", methods=["POST"])
def create():
    expense_name = request.form["name"]
    expense_amount = request.form["amount"]
    expense_paid_by = request.form["paidBy"]
    expense_equally_split = request.form.get("equallySplit")

    expenses.append(
        Expense(
            title=expense_name,
            amount=expense_amount,
            paid_by=expense_paid_by,
            equally_split=expense_equally_split,
        )
    )
    return redirect(url_for("home"))


@app.route("/delete/<int:index>")
def delete(index):
    if len(expenses) > index:
        del expenses[index]
    return redirect(url_for("home"))


@app.route("/modify/<int:index>", methods=["POST"])
def modify(index):
    try:
        expense_selected = expenses[index]
    except IndexError:
        return redirect(url_for("home"))
    expense_selected.title = request.form["newName"]
    expense_selected.amount = request.form["newAmount"]
    expense_selected.paid_by = request.form["newPaidBy"]
    expense_selected.equally_split = request.form.get("newEquallySplit")

    return redirect(url_for("home"))


@app.route("/expense/<int:id>", methods=["GET"])
def get_expense(id):
    expense = expenses[id]
    print(expense.__dict__)
    return jsonify(expense.__dict__)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
