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

# database host is database address (localhost if on local computer)
# database name is name of database
db_host = "ec2-54-165-90-230.compute-1.amazonaws.com"   # address of database
db_name = "d6hp3i25m6gslc"      # name of database

# data base username/pass
db_user = "uqqcowyaruajrk"        # login name
db_pass = "e8828f90c6df41a82eac46bcb552a9cdf32a5b109db1d72ec7cb9ad988030475"      # login password

# can use a user account only with permissions to read from database to make sure
# we cannot edit anything by accident

# used to connect to the database
connect = psycopg2.connect(host=db_host, dbname=db_name, user=db_user, password=db_pass)
cursor = connect.cursor()

cursor.execute("""

SELECT * 
FROM homeownerapp 
where rent_range_start<=(
	SELECT rent_range_end 
	FROM tenantapp 
	where appid=10) 
AND rent_range_end>(
	SELECT rent_range_start 
	FROM tenantapp 
	where appid=10) 
AND city=(
	SELECT city 
	FROM tenantapp 
	where appid=10) 
AND neighborhood=(
	SELECT neighborhood 
	FROM tenantapp 
	where appid=10);

""")

# SELECT * FROM homeownerapp WHERE appid=8

records = cursor.fetchall()
#record_list = records[0].split(',')

print(records)

#print("\nComplete sentence: " + records[0][5])
pet_statement = records[0][5]

sentence_list = sent_tokenize(pet_statement)

sentiment_analyzer = SentimentIntensityAnalyzer()

#for x in sentence_list:
#    print("\n" + x)
#    print(sentiment_analyzer.polarity_scores(x))

print("I hate dogs but I lke cats")
print(sentiment_analyzer.polarity_scores("I hate dogs but I like cats"))

connect.close()