from db.db import sql

def all_legs():
    return sql('SELECT * FROM legs ORDER BY id ')

def get_leg(id):
    legs = sql("SELECT * FROM legs WHERE id = %s", [id])
    return legs[0]

def create_leg(day_of_month, leg_plan, current_weight, fasting_schedule, dietary_plan, image_url, input_comment):
    sql('INSERT INTO legs(day_of_month, leg_plan, current_weight, fasting_schedule, dietary_plan, image_url, input_comment) VALUES(%s, %s, %s, %s, %s, %s, %s) RETURNING *', [day_of_month, leg_plan, current_weight, fasting_schedule, dietary_plan, image_url, input_comment])


def update_leg(id, day_of_month, leg_plan, current_weight, fasting_schedule, dietary_plan, image_url, input_comment):
    sql('UPDATE legs SET day_of_month=%s, leg_plan=%s, current_weight=%s, fasting_schedule=%s, dietary_plan=%s, image_url=%s, input_comment=%s WHERE id=%s RETURNING *', [day_of_month, leg_plan, current_weight, fasting_schedule, dietary_plan, image_url, input_comment, id])


def delete_leg(id):
    sql('DELETE FROM legs WHERE id=%s RETURNING *', [id])

def comment_leg(legs_id, user_id):
  sql("INSERT INTO comments(user_id, legs_id) VALUES(%s, %s) RETURNING *", [user_id, legs_id])

def favourite_leg(legs_id, user_id):
  sql("INSERT INTO favourites(user_id, legs_id) VALUES(%s, %s) RETURNING *", [user_id, legs_id])