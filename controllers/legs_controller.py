from flask import render_template, request, redirect, session
from models.leg import all_legs, get_leg, create_leg, update_leg, delete_leg, comment_leg, favourite_leg
from services.session_info import current_user

def index():
    legs = all_legs()
    return render_template('legs/index.html', legs=legs, current_user=current_user())

def new():
  return render_template('legs/new.html')

def create():
  day_of_month = request.form.get ('day_of_month')
  leg_plan = request.form.get ('leg_plan')
  current_weight = request.form.get ('current_weight')
  fasting_schedule = request.form.get ('fasting_schedule')
  dietary_plan = request.form.get ('dietary_plan')
  image_url = request.form.get ('image_url')
  input_comment = request.form.get('input_comment')
  create_leg(day_of_month, leg_plan, current_weight, fasting_schedule, dietary_plan, image_url, input_comment)
  return redirect('/legs')

def edit(id):
   leg = get_leg(id)
   return render_template('legs/edit.html', leg=leg)
   
def update(id):
  day_of_month = request.form.get ('day_of_month')
  leg_plan = request.form.get ('leg_plan')
  current_weight = request.form.get ('current_weight')
  fasting_schedule = request.form.get ('fasting_schedule')
  dietary_plan = request.form.get ('dietary_plan')
  image_url = request.form.get ('image_url')
  input_comment = request.form.get('input_comment')
  update_leg(day_of_month, leg_plan, current_weight, fasting_schedule, dietary_plan, image_url, input_comment, id)
  return redirect('/legs')

def delete(id):
  delete_leg(id)
  return redirect('/legs')

def comment(id):
  comment_leg(id, session['user_id'])
  return redirect('/legs')

def favourite(id):
  favourite_leg(id, session['user_id'])
  return redirect('/legs')