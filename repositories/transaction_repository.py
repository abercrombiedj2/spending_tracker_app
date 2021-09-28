from db.run_sql import run_sql
from models.transaction import Transaction
from models.merchant import Merchant
from models.tag import Tag
import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository

def save(transaction):
    sql = "INSERT INTO transactions (amount, merchant_id, tag_id, timestamp) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [transaction.amount, transaction.merchant.id, transaction.tag.id, transaction.timestamp]
    results = run_sql(sql, values)
    id = results[0]['id']
    transaction.id = id

def select_all():
    transactions=[]

    sql = "SELECT * from transactions"
    results = run_sql(sql)

    for row in results:
        merchant = merchant_repository.select(row['merchant_id'])
        tag = tag_repository.select(row['tag_id'])
        transaction = Transaction(row['amount'], merchant, tag, row['timestamp'], row['id'])
        transactions.append(transaction)
    return transactions