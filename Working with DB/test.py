import mysql.connector

myDb = mysql.connector.connect(
    host="localhost",
    user="Admin",
    passwd="M1t0t5CuTEda1ra",
    database="sql_store"
)

myCursor = myDb.cursor()

myCursor.execute("SELECT * FROM customers")

myResults = myCursor.fetchall()

for x in myResults:
    for y in x:
        print(y, end=' ')
    print()

print(myDb)


