from dotenv import load_dotenv
load_dotenv()  
import os
from flask import Flask, redirect
from routes.goals_routes import goals_routes
from routes.exercises_routes import exercises_routes
from routes.legs_routes import legs_routes
from routes.shoulders_routes import shoulders_routes
from routes.users_routes import users_routes
from routes.sessions_routes import sessions_routes

SECRET_KEY = os.environ.get("FLASK_SECRET_KEY", "my_KEY")

app = Flask(__name__)

app.config['SECRET_KEY'] = SECRET_KEY
app.register_blueprint(goals_routes, url_prefix='/goals')
app.register_blueprint(exercises_routes, url_prefix='/exercises')
app.register_blueprint(legs_routes, url_prefix='/legs')
app.register_blueprint(shoulders_routes, url_prefix='/shoulders')
app.register_blueprint(users_routes, url_prefix='/users')
app.register_blueprint(sessions_routes, url_prefix='/sessions')

@app.route('/')
def index():
    return redirect('/goals')
  