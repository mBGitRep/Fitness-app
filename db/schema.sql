CREATE DATABASE exercises_app;


CREATE TABLE goals (
  id SERIAL PRIMARY KEY,
  goal_text TEXT,
  goal_image_url TEXT
);


CREATE TABLE exercises (
  id SERIAL PRIMARY KEY,
  day_of_month TEXT,
  exercise_plan TEXT,
  current_weight TEXT,
  fasting_schedule TEXT,
  dietary_plan TEXT,
  image_url TEXT, 
  input_comment TEXT
);

CREATE TABLE legs (
  id SERIAL PRIMARY KEY,
  day_of_month TEXT,
  exercise_plan TEXT,
  current_weight TEXT,
  fasting_schedule TEXT,
  dietary_plan TEXT,
  image_url TEXT, 
  input_comment TEXT
);

CREATE TABLE shoulders (
  id SERIAL PRIMARY KEY,
  day_of_month TEXT,
  exercise_plan TEXT,
  current_weight TEXT,
  fasting_schedule TEXT,
  dietary_plan TEXT,
  image_url TEXT, 
  input_comment TEXT
);







CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    email TEXT,
    password_digest TEXT
);


CREATE TABLE comments (
  id SERIAL PRIMARY KEY,
  user_id INTEGER,
  exercises_id INTEGER,
  comment TEXT
);

CREATE TABLE favourites (
  id SERIAL PRIMARY KEY,
  user_id INTEGER,
  exercises_id INTEGER,
  is_favorite BOOLEAN DEFAULT false
);