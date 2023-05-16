from db.db import sql

def all_exercises():
    return sql('SELECT * FROM exercises ORDER BY id ')

def get_exercise(id):
    exercises = sql("SELECT * FROM exercises WHERE id = %s", [id])
    return exercises[0]

def create_exercise(day_of_month, exercise_plan, current_weight, fasting_schedule, dietary_plan, image_url, input_comment):
    sql('INSERT INTO exercises(day_of_month, exercise_plan, current_weight, fasting_schedule, dietary_plan, image_url, input_comment) VALUES(%s, %s, %s, %s, %s, %s, %s) RETURNING *', [day_of_month, exercise_plan, current_weight, fasting_schedule, dietary_plan, image_url, input_comment])


def update_exercise(id, day_of_month, exercise_plan, current_weight, fasting_schedule, dietary_plan, image_url, input_comment):
    sql("UPDATE exercises SET day_of_month=%s, exercise_plan=%s, current_weight=%s, fasting_schedule=%s, dietary_plan=%s, image_url=%s, input_comment=%s WHERE id=%s RETURNING *", [ day_of_month, exercise_plan, current_weight, fasting_schedule, dietary_plan, image_url, input_comment, id])


def delete_exercise(id):
    sql('DELETE FROM exercises WHERE id=%s RETURNING *', [id])

def comment_exercise(exercises_id, user_id):
  sql("INSERT INTO comments(user_id, exercises_id) VALUES(%s, %s) RETURNING *", [user_id, exercises_id])

def favourite_exercise(exercises_id, user_id):
  sql("INSERT INTO favourites(user_id, exercises_id) VALUES(%s, %s) RETURNING *", [user_id, exercises_id])