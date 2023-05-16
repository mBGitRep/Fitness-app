from flask import render_template, request, redirect, session
from models.shoulder import all_shoulders, get_shoulder, create_shoulder, update_shoulder, delete_shoulder, comment_shoulder, favourite_shoulder
from services.session_info import current_user

def index():
    shoulders = all_shoulders()
    return render_template('shoulders/index.html', shoulders=shoulders, current_user=current_user())

def new():
  return render_template('shoulders/new.html')

def create():
  day_of_month = request.form.get ('day_of_month')
  shoulder_plan = request.form.get ('shoulder_plan')
  current_weight = request.form.get ('current_weight')
  fasting_schedule = request.form.get ('fasting_schedule')
  dietary_plan = request.form.get ('dietary_plan')
  image_url = request.form.get ('image_url')
  input_comment = request.form.get('input_comment')
  create_shoulder(day_of_month, shoulder_plan, current_weight, fasting_schedule, dietary_plan, image_url, input_comment)
  return redirect('/shoulders')

def edit(id):
   shoulder = get_shoulder(id)
   return render_template('shoulders/edit.html', shoulder=shoulder)
   
def update(id):
  day_of_month = request.form.get ('day_of_month')
  shoulder_plan = request.form.get ('shoulder_plan')
  current_weight = request.form.get ('current_weight')
  fasting_schedule = request.form.get ('fasting_schedule')
  dietary_plan = request.form.get ('dietary_plan')
  image_url = request.form.get ('image_url')
  input_comment = request.form.get('input_comment')
  update_shoulder(day_of_month, shoulder_plan, current_weight, fasting_schedule, dietary_plan, image_url, input_comment, id)
  return redirect('/shoulders')

def delete(id):
  delete_shoulder(id)
  return redirect('/shoulders')

def comment(id):
  comment_shoulder(id, session['user_id'])
  return redirect('/shoulders')

def favourite(id):
  favourite_shoulder(id, session['user_id'])
  return redirect('/shoulders')