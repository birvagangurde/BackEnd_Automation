

import mysql.connector

# host, db, user, password
conn = mysql.connector.connect(host='localhost', database='apiDevelop', user='root', password='' )


print(conn.is_connected())
cursor = conn.cursor()
cursor.execute('select * from CustomerInfo')
row = cursor.fetchone()
print(row)
print(row[3])
rowAll = cursor.fetchall()
print(rowAll)  #list of tuples


