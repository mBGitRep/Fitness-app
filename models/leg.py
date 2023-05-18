from db.db import sql

def all_legs():
    return sql('SELECT * FROM legs ORDER BY id ')

def get_leg(id):
    legs = sql("SELECT * FROM legs WHERE id = %s", [id])
    return legs[0]

def create_leg(day, plan, weight, fasting, diet, image, change, user_id):
    sql('INSERT INTO legs(day, plan, weight, fasting, diet, image, change, user_id) VALUES(%s, %s, %s, %s, %s, %s, %s, %s) RETURNING *', [day, plan, weight, fasting, diet, image, change, user_id])


def update_leg(id, day, plan, weight, fasting, diet, image, change, user_id):
    sql('UPDATE legs SET day=%s, plan=%s, weight=%s, fasting=%s, diet=%s, image=%s, change=%s, user_id=%s WHERE id=%s RETURNING *', [day, plan, weight, fasting, diet, image, change, user_id, id])

def delete_leg(id):
    sql('DELETE FROM legs WHERE id=%s RETURNING *', [id])

def commt_leg(exercises_id, user_id):
  sql("INSERT INTO comments(user_id, exercises_id) VALUES(%s, %s) RETURNING *", [user_id, exercises_id])

def favorite_leg(exercise_id, user_id):
  sql("INSERT INTO favorites(user_id, exercise_id) VALUES(%s, %s) RETURNING *", [user_id, exercise_id])

def like_leg(exercise_id, user_id):
    check_if_already_liked = sql('SELECT * FROM likes WHERE user_id = %s AND exercise_id = %s', [user_id, exercise_id])
    if len(check_if_already_liked)>0:
        sql('DELETE FROM likes WHERE user_id=%s AND exercise_id=%s RETURNING *',[user_id, exercise_id])
    else:
        sql("INSERT INTO likes(user_id, exercise_id) VALUES(%s, %s) RETURNING *", [user_id, exercise_id])

def comment_leg(exercise_id, user_id, comment):
    sql("INSERT INTO comments (exercise_id, user_id, comment) VALUES (%s, %s, %s) RETURNING *",[exercise_id, user_id, comment])

def all_comments():
    return sql("SELECT * FROM comments")

def all_likes(exercise_id):
    return sql('SELECT COUNT(*) FROM likes WHERE exercise_id = %s', [exercise_id])