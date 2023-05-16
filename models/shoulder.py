from db.db import sql

def all_shoulders():
    return sql('SELECT * FROM shoulders ORDER BY id ')

def get_shoulder(id):
    shoulders = sql("SELECT * FROM shoulders WHERE id = %s", [id])
    return shoulders[0]

def create_shoulder(day_of_month, shoulder_plan, current_weight, fasting_schedule, dietary_plan, image_url, input_comment):
    sql('INSERT INTO shoulders(day_of_month, shoulder_plan, current_weight, fasting_schedule, dietary_plan, image_url, input_comment) VALUES(%s, %s, %s, %s, %s, %s, %s) RETURNING *', [day_of_month, shoulder_plan, current_weight, fasting_schedule, dietary_plan, image_url, input_comment])


def update_shoulder(id, day_of_month, shoulder_plan, current_weight, fasting_schedule, dietary_plan, image_url, input_comment):
    sql('UPDATE shoulders SET day_of_month=%s, shoulder_plan=%s, current_weight=%s, fasting_schedule=%s, dietary_plan=%s, image_url=%s, input_comment=%s WHERE id=%s RETURNING *', [day_of_month, shoulder_plan, current_weight, fasting_schedule, dietary_plan, image_url, input_comment, id])


def delete_shoulder(id):
    sql('DELETE FROM shoulders WHERE id=%s RETURNING *', [id])

def comment_shoulder(shoulders_id, user_id):
  sql("INSERT INTO comments(user_id, shoulders_id) VALUES(%s, %s) RETURNING *", [user_id, shoulders_id])

def favourite_shoulder(shoulders_id, user_id):
  sql("INSERT INTO favourites(user_id, shoulders_id) VALUES(%s, %s) RETURNING *", [user_id, shoulders_id])