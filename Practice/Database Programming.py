import sqlite3
import CRUD as dbOps

connection = sqlite3.connect(dbOps.dbName)
print("Connection: ", connection)
print("Type of Connection: ", type(connection))

print("Opened database {} successfully.".format(dbOps.dbName))

print("Closing the connection.")
connection.close()

# -----------------------------------------------------------------------------------

import sqlite3
import CRUD as dbOps

connection = sqlite3.connect(dbOps.dbName)

print("Opened database {} successfully".format(dbOps.dbName))

print("Create cursor object")
cursor = connection.cursor()
dbOps.CreateTable(cursor, connection)

print("Closing the connection")
connection.close()

# -----------------------------------------------------------------------------------

import sqlite3
import CRUD as dbOps

connection = sqlite3.connect(dbOps.dbName)

print("Opened database {} successfully".format(dbOps.dbName))

print("Create cursor object")
cursor = connection.cursor()
dbOps.CreateTable(cursor, connection)

# Add data to the table
dbOps.DataEntry(cursor, connection)

print("Closing the connection")
connection.close()

# -----------------------------------------------------------------------------------

import sqlite3
import CRUD as dbOps

connection = sqlite3.connect(dbOps.dbName)

print("Opened database {} successfully".format(dbOps.dbName))

print("Create cursor object")
cursor = connection.cursor()
dbOps.CreateTable(cursor, connection)

# Add Dynamic Data
dbOps.DynamicDataEntry(cursor, connection, "KL Rahul", "KINGS", 31, 2000)

# Read the data
dbOps.ReadData(cursor)

print("Closing the connection")
connection.close()

# -----------------------------------------------------------------------------------

import sqlite3
import CRUD as dbOps

connection = sqlite3.connect(dbOps.dbName)

print("Opened database {} successfully".format(dbOps.dbName))

print("Create cursor object")
cursor = connection.cursor()
dbOps.CreateTable(cursor, connection)

# Read the data
dbOps.ReadData(cursor)

# Update the Data
print("Updating the Data")
dbOps.UpdateData(cursor, connection)

# Read the Data
print("Reading the Data after updation")
dbOps.ReadData(cursor)

print("Closing the connection")
connection.close()

# -----------------------------------------------------------------------------------

import sqlite3
import CRUD as dbOps

connection = sqlite3.connect(dbOps.dbName)

print("Opened database {} successfully".format(dbOps.dbName))

print("Create cursor object")
cursor = connection.cursor()
dbOps.CreateTable(cursor, connection)

# Read the data
dbOps.ReadData(cursor)

# Delete the Data
print("Deleting the Data")
dbOps.DeleteData(cursor, connection)

# Read the Data
print("Reading the Data after deletion")
dbOps.ReadData(cursor)

print("Closing the connection")
connection.close()
