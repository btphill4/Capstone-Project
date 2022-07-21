# test

# database connection import
import psycopg2

# natural language toolkit
import nltk
from HomeOwners import *
# necessary imports to run the sentiment analyzer
nltk.download('wordnet')
nltk.download('vader_lexicon')
nltk.download('punkt')

from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import sent_tokenize

# Database host is database address (localhost if on local computer)
# Database name is name of database
db_host = "ec2-54-165-90-230.compute-1.amazonaws.com"
db_name = "d6hp3i25m6gslc"

# Data base username/pass
db_user = "uqqcowyaruajrk"
db_pass = "e8828f90c6df41a82eac46bcb552a9cdf32a5b109db1d72ec7cb9ad988030475"
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

list = []
for x in range(0, cursor.rowcount):
    item = cursor.fetchone()
    list.append(dict(zip(colnames, item)))

print(list[0]['userid'])    
HO1 = HomeOwner(cursor.fetchone())
print(HO1)

connect.close()