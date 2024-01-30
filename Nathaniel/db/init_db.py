import sqlite3

connection = sqlite3.connect('McLink.db')


with open('Nathaniel/db/schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()


connection.commit()
connection.close()