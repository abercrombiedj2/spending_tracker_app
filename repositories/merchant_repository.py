from db.run_sql import run_sql
from models.merchant import Merchant
from models.transaction import Transaction

def save(merchant):
    sql = "INSERT INTO merchants (name) VALUES (%s) RETURNING *"
    values = [merchant.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    merchant.id = id
    return merchant

def select(id):
    merchant=None
    sql = "SELECT * FROM merchants WHERE id=%s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        merchant = Merchant(result['name'], result['id'])
    return merchant