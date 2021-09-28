from flask import Flask, Blueprint, render_template, request, redirect
from models.transaction import Transaction
from datetime import datetime
import repositories.transaction_repository as transaction_repository
import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository

transactions_blueprint = Blueprint("transactions", __name__)

@transactions_blueprint.route("/transactions/view_transactions")
def view_transactions():
    transactions = transaction_repository.select_all()
    return render_template("transactions/view_transactions.html", all_transactions=transactions)

@transactions_blueprint.route("/transactions/new_transaction", methods=['GET'])
def new_transaction():
    merchants = merchant_repository.select_all()
    tags = tag_repository.select_all()
    return render_template("transactions/new_transaction.html", all_merchants=merchants, all_tags=tags)

@transactions_blueprint.route("/transactions", methods=['POST'])
def create_transaction():
    amount = request.form['amount']
    merchant_id = request.form['merchant_id']
    tag_id = request.form['tag_id']
    timestamp = datetime.now().strftime("%d/%m/%Y, %H:%M")
    merchant = merchant_repository.select(merchant_id)
    tag = tag_repository.select(tag_id)
    transaction = Transaction(amount, merchant, tag, timestamp)
    transaction_repository.save(transaction)
    return redirect("/transactions/view_transactions")
