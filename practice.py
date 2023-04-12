import sqlite3 #library (Open source)

con = sqlite3.connect('project.db')

test = "CREATE TABLE USERTEST(username varchar(25),password varchar(25),gender varchar(10),email varchar(50),phone varchar(50),PRIMARY KEY(username));"

con.execute(test) # excute test

con.commit() # Save

con.close()

print("Done!")
