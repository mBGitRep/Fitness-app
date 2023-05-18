CREATE DATABASE exercises_app;


CREATE TABLE goals (
  id SERIAL PRIMARY KEY,
  goal_text TEXT,
  goal_image_url TEXT
);


INSERT INTO goals (goal_text, goal_image_url)
VALUES 
('Gain Muscles', 'https://infinitefitnesspro.com/wp-content/uploads/2021/02/How-Long-Does-It-Take-To-Build-Muscle.jpg')
('Loose Weight', 'https://www.pristyncare.com/blog/wp-content/uploads/2019/08/9-Simple-Tips-and-Diet-Plan-That-Will-Help-You-Lose-Weight-In-Just-30-Days.jpg')
('Get Active', 'https://www.alcoa.ca/wp-content/uploads/2018/08/Active-lifestyle-communities-in-Canada-880x660.jpg');


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

INSERT INTO exercises (day, plan, weight, fasting, diet, image, change, user_id)
VALUES 
('Monday', 'Arms', '100 kgs', 'Yes 2 hours', 'Low Carb', 'https://i.postimg.cc/wTV4p3Pq/abeef7a408652305a6ff4af52c09fa9e.jpg', 'Lost 2 kgs', 0)
('Tuesday', 'Legs', '99 kgs', 'Yes 3 hours', 'Low Carb', 'https://i.postimg.cc/yx777ZkT/legs.jpg', 'Lost 3 kgs', 0)
('Wednesday', 'Back', '98 kgs', 'Yes 1 hour', 'No Carb', 'https://i.postimg.cc/k5pJwNTj/back.jpg', 'Lost 2 kgs', 0);

CREATE TABLE legs (
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

INSERT INTO legs (day, plan, weight, fasting, diet, image, change, user_id)
VALUES 
('Monday', 'Running', '180 kgs', 'Yes 5 hours', 'No Carb', 'https://www.printablee.com/postpic/2013/02/free-printable-ball-exercise-chart_260072.jpg', 'Lost 1 kg', 0)
('Tuesday', 'Cardio', '178 kgs', 'Yes 3 hours', 'Low Carb', 'https://www.thefitindian.com/blog/wp-content/uploads/2021/12/Beginners-exercises-to-weight-loss.jpg', 'Lost 3 kgs', 0)
('Wednesday', 'Pushups', '172 kgs', 'Yes 2 hour', 'No Carb', 'https://i.pinimg.com/564x/da/d3/33/dad333aa04bc3c0b697a761a7ceb395a.jpg', 'Lost 9 kgss', 0);

CREATE TABLE shoulders (
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

INSERT INTO shoulders (day, plan, weight, fasting, diet, image, change, user_id)
VALUES 
('Monday', 'Stretching', '98 kgs', 'Yes 2 hours', 'Low Carb', 'https://offgridweb.com/wp-content/uploads/2016/06/Stretching-exercises-2-1024x724.jpg', 'Lost 2 kgs', 0)
('Tuesday', 'Yoga', '98 kgs', 'Yes 3 hours', 'No Carb', 'https://veritas.widen.net/content/1cmlnjmhpu/webp/Stretching-Pinterest-v5.webp?use=idsla&crop=0&k=&color=&retina=false&u=at8tiu&w=658', 'No Change', 0)
('Wednesday', 'PE', '97 kgs', 'Yes 1 hour', 'Low Carb', 'https://en.pimg.jp/092/077/314/1/92077314.jpg', 'Lost 3 kgs', 0);



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