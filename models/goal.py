from db.db import sql

def all_goals():
    return sql('SELECT * FROM goals ORDER BY id ')

def get_goal(id):
    goals = sql("SELECT * FROM goals WHERE id = %s", [id])
    return goals[0]

def create_goal(goal_text, goal_image_url):
    sql('INSERT INTO goals(goal_text, goal_image_url) VALUES(%s, %s) RETURNING *', [goal_text, goal_image_url])


def update_goal(id, goal_text, goal_image_url):
    sql('UPDATE goals SET goal_text=%s, goal_image_url=%s WHERE id=%s RETURNING *', [goal_text, goal_image_url, id])


def delete_goal(id):
    sql('DELETE FROM goals WHERE id=%s RETURNING *', [id])
 