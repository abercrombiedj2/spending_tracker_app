from db.run_sql import run_sql
from models.tag import Tag
from models.transaction import Transaction

def save(tag):
    sql = "INSERT INTO tags (name) VALUES (%s) RETURNING *"
    values = [tag.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    tag.id = id
    return tag

def select(id):
    tag=None
    sql = "SELECT * FROM tags WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        tag = Tag(result['name'], result['id'])
    return result