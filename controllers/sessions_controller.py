from flask import render_template, request, redirect, session
from models.user import find_user_by_email
from models.exercise import all_exercises, get_exercise, all_comments, all_likes
from services.session_info import current_user
import bcrypt

def new():
  return render_template('sessions/new.html')

def create():
  email = request.form.get('email')
  password = request.form.get('password')
  user = find_user_by_email(email)
  if user == None:
    return redirect('/sessions/new')

  valid_password = bcrypt.checkpw(password.encode(), user['password_digest'].encode())
  if valid_password:
    session['user_id'] = user['id'] # logs the user in
    return redirect('/')
  else:
        return redirect('/sessions/new')

def delete():
  session.clear() # logs the user out
  return redirect('/')

def index():
    exercises = all_exercises()
    return render_template('exercise/index.html', exercises=exercises,current_user= current_user())

def exercise(id):
    exercise = get_exercise(id)
    comments = all_comments(id)
    likes_count = all_likes(id)[0]
    return render_template('sessions/exercise.html', exercise=exercise,current_user= current_user(), comments = comments, likes_count = likes_count)