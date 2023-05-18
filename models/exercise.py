from db.db import sql

def all_exercises():
    return sql('SELECT * FROM exercises ORDER BY id ')

def get_exercise(id):
    exercises = sql("SELECT * FROM exercises WHERE id = %s", [id])
    return exercises[0]

def create_exercise(day, plan, weight, fasting, diet, image, change, user_id):
    sql('INSERT INTO exercises(day, plan, weight, fasting, diet, image, change, user_id) VALUES(%s, %s, %s, %s, %s, %s, %s, %s) RETURNING *', [day, plan, weight, fasting, diet, image, change, user_id])


def update_exercise(id, day, plan, weight, fasting, diet, image, change, user_id):
    sql('UPDATE exercises SET day=%s, plan=%s, weight=%s, fasting=%s, diet=%s, image=%s, change=%s, user_id=%s WHERE id=%s RETURNING *', [day, plan, weight, fasting, diet, image, change, user_id, id])

def delete_exercise(id):
    sql('DELETE FROM exercises WHERE id=%s RETURNING *', [id])

def commt_exercise(exercises_id, user_id):
  sql("INSERT INTO comments(user_id, exercises_id) VALUES(%s, %s) RETURNING *", [user_id, exercises_id])

def favorite_exercise(exercise_id, user_id):
  sql("INSERT INTO favorites(user_id, exercise_id) VALUES(%s, %s) RETURNING *", [user_id, exercise_id])

def like_exercise(exercise_id, user_id):
    check_if_already_liked = sql('SELECT * FROM likes WHERE user_id = %s AND exercise_id = %s', [user_id, exercise_id])
    if len(check_if_already_liked)>0:
        sql('DELETE FROM likes WHERE user_id=%s AND exercise_id=%s RETURNING *',[user_id, exercise_id])
    else:
        sql("INSERT INTO likes(user_id, exercise_id) VALUES(%s, %s) RETURNING *", [user_id, exercise_id])

def comment_exercise(exercise_id, user_id, comment):
    sql("INSERT INTO comments (exercise_id, user_id, comment) VALUES (%s, %s, %s) RETURNING *",[exercise_id, user_id, comment])

# def all_comments(exercise_id):
#     return sql("SELECT * FROM comments WHERE exercise_id =%s",[exercise_id])

def all_comments():
    return sql("SELECT * FROM comments")

def all_likes(exercise_id):
    return sql('SELECT COUNT(*) FROM likes WHERE exercise_id = %s', [exercise_id])
