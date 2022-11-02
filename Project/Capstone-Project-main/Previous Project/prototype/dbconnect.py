# test

# database connection import
import psycopg2

# natural language toolkit
import nltk

#from HomeOwners2 import *


# necessary imports to run the sentiment analyzer
nltk.download('wordnet')
nltk.download('vader_lexicon')
nltk.download('punkt')

from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import sent_tokenize

def db_connect():
  # Database host is database address (localhost if on local computer)
  # Database name is name of database
  db_host = "ec2-18-215-96-22.compute-1.amazonaws.com"   # address of database
  db_name = "db926f75ofgha2"      # name of database

  # Data base username/pass
  db_user = "glkawdwwyajxsd"        # login name
  db_pass = "ab13a8d4d623d059a6c6fa355da18839af9ce573edc56ae8ab09ba0b99b70a72"      # login password
  db_port = 5432

  # can use a user account only with permissions to read from database to make sure
  # we cannot edit anything by accident

  # used to connect to the database
  connect = psycopg2.connect(host=db_host, dbname=db_name, user=db_user, password=db_pass, port=db_port)

  cursor = connect.cursor()

  cursor.execute("""

  SELECT * FROM homeownerapp

  """)

  colnames = [desc[0] for desc in cursor.description]

  global list
  list = []
  for x in range(0, cursor.rowcount):
      item = cursor.fetchone()
      #HO2 = HomeOwner2(item, colnames)
      #print(HO2)
      list.append(dict(zip(colnames, item)))

  #print(list[0]['userid'])
  #print(list[0]['fullname'])    
  #HO1 = HomeOwner2(list[0])
  #print(HO2)

  connect.close()
  return list

arr = db_connect()
#print(arr)