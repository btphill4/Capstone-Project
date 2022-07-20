# test

# database connection import
import psycopg2

# natural language toolkit
import nltk

# necessary imports to run the sentiment analyzer
nltk.download('wordnet')
nltk.download('vader_lexicon')
nltk.download('punkt')

from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import sent_tokenize

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

SELECT * FROM homeownerapp;

""")

temp = cursor.fetchall()
for x in temp:
    print("\n\n")
    print(x)

connect.close()