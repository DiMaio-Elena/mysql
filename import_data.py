import mysql.connector
import pandas as pd

#Connect to mysql
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)
mycursor = mydb.cursor()

#Create the DB (if not already exists)

#Create the table for the csv data (if not exists)
mycursor.execute("""
  CREATE TABLE IF NOT EXISTS EPISODES(
    index VARCHAR(30) NOT NULL,
    number_of_seasons INTEGER,
    title_of_the_episode VARCHAR(30),
    description_of_the_episode VARCHAR(30),
    ratings_given_to_the_episode VARCHAR(30),
    duration_of_the_episode INTEGER(30),
    date_on_which_the_episode_was_released VARCHAR(30),
 

  );""")

#Delete data from the table Clsh_Unit
mycursor.execute("DELETE FROM THEOFFICE.EPISODES")
mydb.commit()

#Read data from a csv file
clash_data = pd.read_csv('./cr-unit-attributes.csv', index_col=False, delimiter = ',')
clash_data = clash_data.fillna('Null')
print(clash_data.head(20))

#Fill the table
for i,row in clash_data.iterrows():
    cursor = mydb.cursor()
    #here %S means string values 
    sql = "INSERT INTO EPISODES VALUES (%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql, tuple(row))
    print("Record inserted")
    # the connection is not auto committed by default, so we must commit to save our changes
    mydb.commit()

#Check if the table has been filled
mycursor.execute("SELECT * FROM THEOFFICE.EPISODES")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)