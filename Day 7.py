#Day 7 Assignment :- Python Database Connection Project which updates any one value in the table and select all the table data and print it.

import mysql.connector as sqlcon  # Importing Module

#Connecting the local MySQL database
database = sqlcon.connect(host = "localhost", user = "root", passwd = "abhi123", database = 'student')

cur = database.cursor() #helps to execute the query

cur.execute("update student set mark = 91 where roll = 18")     # Update the Record 
cur.execute("Select * from student")    #Show Table 
for i in cur:
    print(i)

cur.close()
database.commit()       # commit for save changes in database