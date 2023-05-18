from db.db import sql

def all_favorites():
    return sql('SELECT * FROM favorites ORDER BY id ')

def get_favorite(id):
    favorites = sql("SELECT * FROM favorites WHERE id = %s", [id])
    return favorites[0]

def create_favorite(day, plan, weight, fasting, diet, image, change, user_id):
    sql('INSERT INTO favorites(day, plan, weight, fasting, diet, image, change, user_id) VALUES(%s, %s, %s, %s, %s, %s, %s, %s) RETURNING *', [day, plan, weight, fasting, diet, image, change, user_id])


def update_favorite(id, day, plan, weight, fasting, diet, image, change, user_id):
    sql('UPDATE favorites SET day=%s, plan=%s, weight=%s, fasting=%s, diet=%s, image=%s, change=%s, user_id=%s WHERE id=%s RETURNING *', [day, plan, weight, fasting, diet, image, change, user_id, id])

def delete_favorite(id):
    sql('DELETE FROM favorites WHERE id=%s RETURNING *', [id])

def commt_favorite(exercises_id, user_id):
  sql("INSERT INTO comments(user_id, exercises_id) VALUES(%s, %s) RETURNING *", [user_id, exercises_id])

def favorite_favorite(exercise_id, user_id):
  sql("INSERT INTO favorites(user_id, exercise_id) VALUES(%s, %s) RETURNING *", [user_id, exercise_id])

def like_favorite(exercise_id, user_id):
    check_if_already_liked = sql('SELECT * FROM likes WHERE user_id = %s AND exercise_id = %s', [user_id, exercise_id])
    if len(check_if_already_liked)>0:
        sql('DELETE FROM likes WHERE user_id=%s AND exercise_id=%s RETURNING *',[user_id, exercise_id])
    else:
        sql("INSERT INTO likes(user_id, exercise_id) VALUES(%s, %s) RETURNING *", [user_id, exercise_id])

def comment_favorite(exercise_id, user_id, comment):
    sql("INSERT INTO comments (exercise_id, user_id, comment) VALUES (%s, %s, %s) RETURNING *",[exercise_id, user_id, comment])

def all_comments():
    return sql("SELECT * FROM comments")

def all_likes(exercise_id):
    return sql('SELECT COUNT(*) FROM likes WHERE exercise_id = %s', [exercise_id])
