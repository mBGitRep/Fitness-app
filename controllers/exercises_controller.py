from flask import render_template, request, redirect, session
from models.exercise import all_exercises, all_comments, get_exercise, create_exercise, update_exercise, delete_exercise, like_exercise, comment_exercise, favorite_exercise
from services.session_info import current_user

def index():
    comments = all_comments()
    exercises = all_exercises()
    return render_template('exercises/index.html', exercises=exercises, comments=comments, current_user=current_user())
    # return f'{comments}'

def new():
  return render_template('exercises/new.html')

def create():
  day = request.form.get ('day')
  plan = request.form.get ('plan')
  weight = request.form.get ('weight')
  fasting = request.form.get ('fasting')
  diet = request.form.get ('diet')
  image = request.form.get ('image')
  change = request.form.get('change')
  user_id = current_user()['id']
  create_exercise(day, plan, weight, fasting, diet, image, change, user_id)
  return redirect('/exercises')

def edit(id):
   exercise = get_exercise(id)
   return render_template('exercises/edit.html', exercise=exercise)
   
def update(id):
  day = request.form.get ('day')
  plan = request.form.get ('plan')
  weight = request.form.get ('weight')
  fasting = request.form.get ('fasting')
  diet = request.form.get ('diet')
  image = request.form.get ('image')
  change = request.form.get('change')
  user_id = current_user()['id']
  update_exercise(id, day, plan, weight, fasting, diet, image, change, user_id)
  return redirect('/exercises')

def delete(id):
  delete_exercise(id)
  return redirect('/exercises')


def favorite(id):
  favorite_exercise(id, session['user_id'])
  return redirect('/exercises')

def like(id):
    like_exercise(id, session['user_id'])
    return redirect(f'/sessions/page/{id}')


def comment(id):
    exercise_id = id
    user_id = current_user()['id']
    comment = request.form.get('comment')
    comment_exercise(exercise_id, user_id, comment)

    return redirect(f'/exercises')
