from flask import render_template, request, redirect, session
from models.shoulder import all_shoulders, all_comments, get_shoulder, create_shoulder, update_shoulder, delete_shoulder, like_shoulder, comment_shoulder, favorite_shoulder
from services.session_info import current_user

def index():
    comments = all_comments()
    shoulders = all_shoulders()
    return render_template('shoulders/index.html', shoulders=shoulders, comments=comments, current_user=current_user())
    # return f'{comments}'

def new():
  return render_template('shoulders/new.html')

def create():
  day = request.form.get ('day')
  plan = request.form.get ('plan')
  weight = request.form.get ('weight')
  fasting = request.form.get ('fasting')
  diet = request.form.get ('diet')
  image = request.form.get ('image')
  change = request.form.get('change')
  user_id = current_user()['id']
  create_shoulder(day, plan, weight, fasting, diet, image, change, user_id)
  return redirect('/shoulders')

def edit(id):
   shoulder = get_shoulder(id)
   return render_template('shoulders/edit.html', shoulder=shoulder)
   
def update(id):
  day = request.form.get ('day')
  plan = request.form.get ('plan')
  weight = request.form.get ('weight')
  fasting = request.form.get ('fasting')
  diet = request.form.get ('diet')
  image = request.form.get ('image')
  change = request.form.get('change')
  user_id = current_user()['id']
  update_shoulder(id, day, plan, weight, fasting, diet, image, change, user_id)
  return redirect('/shoulders')

def delete(id):
  delete_shoulder(id)
  return redirect('/shoulders')


def favorite(id):
  favorite_shoulder(id, session['user_id'])
  return redirect('/favorites')

def like(id):
    like_shoulder(id, session['user_id'])
    return redirect('/likes')


def comment(id):
    exercise_id = id
    user_id = current_user()['id']
    comment = request.form.get('comment')
    comment_shoulder(exercise_id, user_id, comment)

    return redirect(f'/shoulders')