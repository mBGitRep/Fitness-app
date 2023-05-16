from flask import render_template, request, redirect, session
from models.exercise import all_exercises, get_exercise, create_exercise, update_exercise, delete_exercise, comment_exercise, favourite_exercise
from services.session_info import current_user

def index():
    exercises = all_exercises()
    return render_template('exercises/index.html', exercises=exercises, current_user=current_user())

def new():
  return render_template('exercises/new.html')

def create():
  day_of_month = request.form.get ('day_of_month')
  exercise_plan = request.form.get ('exercise_plan')
  current_weight = request.form.get ('current_weight')
  fasting_schedule = request.form.get ('fasting_schedule')
  dietary_plan = request.form.get ('dietary_plan')
  image_url = request.form.get ('image_url')
  input_comment = request.form.get('input_comment')
  create_exercise(day_of_month, exercise_plan, current_weight, fasting_schedule, dietary_plan, image_url, input_comment)
  return redirect('/exercises')

def edit(id):
   exercise = get_exercise(id)
   return render_template('exercises/edit.html', exercise=exercise)
   
def update(id):
  day_of_month = request.form.get ('day_of_month')
  exercise_plan = request.form.get ('exercise_plan')
  current_weight = request.form.get ('current_weight')
  fasting_schedule = request.form.get ('fasting_schedule')
  dietary_plan = request.form.get ('dietary_plan')
  image_url = request.form.get ('image_url')
  input_comment = request.form.get('input_comment')
  update_exercise(day_of_month, exercise_plan, current_weight, fasting_schedule, dietary_plan, image_url, input_comment, id)
  return redirect('/exercises')

def delete(id):
  delete_exercise(id)
  return redirect('/exercises')

def comment(id):
  comment_exercise(id, session['user_id'])
  return redirect('/exercises')

def favourite(id):
  favourite_exercise(id, session['user_id'])
  return redirect('/exercises')