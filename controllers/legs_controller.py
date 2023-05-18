from flask import render_template, request, redirect, session
from models.leg import all_legs, all_comments, get_leg, create_leg, update_leg, delete_leg, like_leg, comment_leg, favorite_leg
from services.session_info import current_user

def index():
    comments = all_comments()
    legs = all_legs()
    return render_template('legs/index.html', legs=legs, comments=comments, current_user=current_user())
    # return f'{comments}'

def new():
  return render_template('legs/new.html')

def create():
  day = request.form.get ('day')
  plan = request.form.get ('plan')
  weight = request.form.get ('weight')
  fasting = request.form.get ('fasting')
  diet = request.form.get ('diet')
  image = request.form.get ('image')
  change = request.form.get('change')
  user_id = current_user()['id']
  create_leg(day, plan, weight, fasting, diet, image, change, user_id)
  return redirect('/legs')

def edit(id):
   leg = get_leg(id)
   return render_template('legs/edit.html', leg=leg)
   
def update(id):
  day = request.form.get ('day')
  plan = request.form.get ('plan')
  weight = request.form.get ('weight')
  fasting = request.form.get ('fasting')
  diet = request.form.get ('diet')
  image = request.form.get ('image')
  change = request.form.get('change')
  user_id = current_user()['id']
  update_leg(id, day, plan, weight, fasting, diet, image, change, user_id)
  return redirect('/legs')

def delete(id):
  delete_leg(id)
  return redirect('/legs')


def favorite(id):
  favorite_leg(id, session['user_id'])
  return redirect('/favorites')

def like(id):
    like_leg(id, session['user_id'])
    return redirect('/likes')


def comment(id):
    exercise_id = id
    user_id = current_user()['id']
    comment = request.form.get('comment')
    comment_leg(exercise_id, user_id, comment)

    return redirect(f'/legs')