from db.run_sql import run_sql
from models.tag import Tag

def save(tag):
    sql = "INSERT INTO tags (name, active) VALUES (%s, %s) RETURNING *"
    values = [tag.name, tag.active]
    results = run_sql(sql, values)
    id = results[0]['id']
    tag.id = id

def select(id):
    tag=None
    sql = "SELECT * FROM tags WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        tag = Tag(result['name'], result['id'], result['active'])
    return tag

def select_all():
    tags=[]

    sql = "SELECT * FROM tags"
    results = run_sql(sql)

    for row in results:
        tag = Tag(row['name'], row['id'], row['active'])
        tags.append(tag)
    return tags

def update(tag):
    sql = "UPDATE tags SET (name, active) = (%s, %s) WHERE id = %s"
    values = [tag.name, tag.active, tag.id]
    run_sql(sql, values)