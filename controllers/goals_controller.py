from flask import render_template, request, redirect
from models.goal import all_goals, get_goal, create_goal, update_goal, delete_goal
from services.session_info import current_user

def index():
    goals = all_goals()
    return render_template('goals/index.html', goals=goals, current_user=current_user())

def new():
  return render_template('goals/new.html')

def create():
  goal_text = request.form.get ('goal_text')
  goal_image_url = request.form.get ('goal_image_url')
  create_goal(goal_text, goal_image_url)
  return redirect('/')

def edit(id):
   goal = get_goal(id)
   return render_template('goals/edit.html', goal=goal)
   
def update(id):
  goal_text = request.form.get ('goal_text')
  goal_image_url = request.form.get ('goal_image_url')
  update_goal(id, goal_text, goal_image_url)
  return redirect('/')

def delete(id):
  delete_goal(id)
  return redirect('/')