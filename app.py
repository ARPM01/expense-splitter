from flask import Flask, render_template, request, redirect, url_for

from models import Expense

app = Flask(__name__, template_folder="templates")

expenses = []


@app.route("/")
def root():
    return redirect(url_for("home"))


@app.route("/home")
def home():
    return render_template("home.html", expenses=expenses)


@app.route("/create", methods=["POST"])
def create():
    expense_title = request.form["expense_title"]
    # TODO: Add new fields to the form
    expenses.append(
        Expense(
            title=expense_title,
            amount=50.0,
            paid_by=None,
            owed_by=[],
        )
    )
    return redirect(url_for("home"))


@app.route("/delete/<int:index>")
def delete(index):
    if len(expenses) > index:
        del expenses[index]
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
