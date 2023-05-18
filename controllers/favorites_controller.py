from flask import render_template, request, redirect, session
from models.favorite import all_favorites, all_comments, get_favorite, create_favorite, update_favorite, delete_favorite, like_favorite, comment_favorite, favorite_favorite
from services.session_info import current_user

def index():
    comments = all_comments()
    favorites = all_favorites()
    return render_template('favorites/index.html', favorites=favorites, comments=comments, current_user=current_user())
    # return f'{comments}'

def new():
  return render_template('favorites/new.html')

def create():
  day = request.form.get ('day')
  plan = request.form.get ('plan')
  weight = request.form.get ('weight')
  fasting = request.form.get ('fasting')
  diet = request.form.get ('diet')
  image = request.form.get ('image')
  change = request.form.get('change')
  user_id = current_user()['id']
  create_favorite(day, plan, weight, fasting, diet, image, change, user_id)
  return redirect('/favorites')

def edit(id):
   favorite = get_favorite(id)
   return render_template('favorites/edit.html', favorite=favorite)
   
def update(id):
  day = request.form.get ('day')
  plan = request.form.get ('plan')
  weight = request.form.get ('weight')
  fasting = request.form.get ('fasting')
  diet = request.form.get ('diet')
  image = request.form.get ('image')
  change = request.form.get('change')
  user_id = current_user()['id']
  update_favorite(id, day, plan, weight, fasting, diet, image, change, user_id)
  return redirect('/favorites')

def delete(id):
  delete_favorite(id)
  return redirect('/favorites')


def favorite(id):
  favorite_favorite(id, session['user_id'])
  return redirect('/favorites')

def like(id):
    like_favorite(id, session['user_id'])
    return redirect('/likes')


def comment(id):
    exercise_id = id
    user_id = current_user()['id']
    comment = request.form.get('comment')
    comment_favorite(exercise_id, user_id, comment)

    return redirect(f'/favorites')

