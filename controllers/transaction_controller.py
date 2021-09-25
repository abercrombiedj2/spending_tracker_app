from flask import Flask, Blueprint, render_template, request, redirect
from models.transaction import Transaction
import repositories.transaction_repository as transaction_repository
import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository

transactions_blueprint = Blueprint("transactions", __name__)

@transactions_blueprint.route("/transactions")
def view_transactions():
    transactions = transaction_repository.select_all()
    return render_template("transactions/view_transactions.html", all_transactions=transactions)
