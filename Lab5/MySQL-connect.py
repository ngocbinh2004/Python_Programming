import mysql.connector

dbConfig = {
    'user': 'root',
    'password': '123456',
    'host': '127.0.0.1'
}

conn = mysql.connector.connect(**dbConfig)
cursor = conn.cursor()
cursor.execute("SHOW DATABASES")
print(cursor.fetchall())
conn.close()
