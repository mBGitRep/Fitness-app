CREATE DATABASE exercises_app;


CREATE TABLE goals (
  id SERIAL PRIMARY KEY,
  goal_text TEXT,
  goal_image_url TEXT
);

CREATE TABLE exercises (
  id SERIAL PRIMARY KEY,
  day TEXT,
  plan TEXT,
  weight TEXT,
  fasting TEXT,
  diet TEXT,
  image TEXT,
  change TEXT,
  user_id INTEGER
);

CREATE TABLE comments(
  id SERIAL PRIMARY KEY,
  exercise_id INTEGER,
  user_id INTEGER,
  comment TEXT
);

CREATE TABLE likes(
  id SERIAL PRIMARY KEY,
  user_id INTEGER,
  exercise_id INTEGER
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    email TEXT,
    password_digest TEXT
);

CREATE TABLE favorites (
  id SERIAL PRIMARY KEY,
  user_id INTEGER,
  exercise_id INTEGER,
  is_favorite BOOLEAN DEFAULT false
);