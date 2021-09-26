from db.run_sql import run_sql
from models.merchant import Merchant
from models.transaction import Transaction

def save(merchant):
    sql = "INSERT INTO merchants (name) VALUES (%s) RETURNING id"
    values = [merchant.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    merchant.id = id

def select(id):
    merchant=None
    sql = "SELECT * FROM merchants WHERE id=%s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        merchant = Merchant(result['name'], result['id'])
    return merchant

def select_all():
    merchants=[]

    sql = "SELECT * FROM merchants"
    results = run_sql(sql)

    for row in results:
        merchant = Merchant(row['name'], row['id'])
        merchants.append(merchant)
    return merchants