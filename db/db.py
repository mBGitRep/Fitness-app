import psycopg2
import psycopg2.extras
import os
from dotenv import load_dotenv
load_dotenv()

DB_URL = os.environ.get("DATABASE_URL", "dbname=exercises_app")

def sql(query, parameters=[]):
  connection = psycopg2.connect(DB_URL) # open connection
  cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor) # we use cursor to run SQL commandsrun SQL commands
  cursor.execute(query, parameters) # begin transaction
  results = cursor.fetchall()
  connection.commit() # end transaction
  connection.close() # close connection
  return results