# CRUD.py
'''
Application = SQLlite

After 2-3 years, no of entries have gone upto 10s of millions
Solution:
Need to migrate it to MySQL, Oracle or PostgresDB

ORM -> Object Relational Mapping/Mapper

Application => Intermediate Layer (IL) => Talk to any relational DB (Sqlite3, MySQL, Oracle PostgresDB)


Examples of IL (ORM):
1. DjangoORM
2. SQLAlchemy

Classes And Objects
'''

dbName = "Practice.db"

# CRUD
# Create Read Update Delete

def CreateTable(cursor, connection):
    cursor.execute("CREATE TABLE IF NOT EXISTS PLAYERS "
                   "(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, NAME TEXT NOT NULL, TEAM TEXT NOT NULL, AGE INT NOT NULL, PRICE REAL);")
    connection.commit()

def DataEntry(cursor, connection):
    cursor.execute("INSERT INTO PLAYERS VALUES (1, 'Rohit', 'MUM', 29, 1000)")
    connection.commit()

def DynamicDataEntry(cursor, connection, name, team, age, price):
    cursor.execute("INSERT INTO PLAYERS (NAME, TEAM, AGE, PRICE) VALUES (?,?,?,?)", (name, team, age, price))
    connection.commit()

def ReadData(cursor):
    cursor.execute("SELECT * FROM PLAYERS")
    for item in cursor.fetchall():
        print(item)

def UpdateData(cursor, connection):
    cursor.execute("UPDATE PLAYERS SET TEAM = 'CSK' WHERE NAME='KL Rahul'")
    connection.commit()

def DeleteData(cursor, connection):
    cursor.execute("DELETE FROM PLAYERS WHERE TEAM = 'CSK'")
    connection.commit()
