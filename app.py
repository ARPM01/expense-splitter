from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine, text, insert
import models

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
    expense_paid_by = request.form["paid_by"]
    expense_equally_split = request.form.get("equally_split")

    engine = create_engine("sqlite+pysqlite:///database.db", echo=True)
    models.Base.metadata.create_all()

    stmt = insert(models.Expense).values(
        name=expense_name,
        owed=expense_paid_by,
        value=expense_amount,
        split=expense_equally_split,
    )

    with engine.connect() as conn:
        result = conn.execute(stmt)
        conn.commit()

    return redirect(url_for("home"))


@app.route("/delete/<int:index>")
def delete(index):
    if len(expenses) > index:
        del expenses[index]
    return redirect(url_for("home"))


@app.route("/modify/<int:index>")
def modify(index):
    # TODO: Add a modal to modify the expense
    if len(expenses) > index:
        return redirect(url_for("home"))
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
