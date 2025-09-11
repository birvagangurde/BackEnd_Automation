

import mysql.connector

# host, db, user, password
conn = mysql.connector.connect(host='localhost', database='apiDevelop', user='root', password='' )


print(conn.is_connected())
cursor = conn.cursor()
cursor.execute('select * from CustomerInfo')
# row = cursor.fetchone()
# print(row)
# print(row[3])
# rowAll = cursor.fetchall()
# print(rowAll)  #list of tuples


# Start of the 46th Video

rows = cursor.fetchall()

print(type(rows))
print(rows)

sum = 0
for row in rows:  #('Protractor', datetime.date(2025, 9, 10), 45, 'Africa')
    print(row[2])
    sum = sum + row[2]

print(sum)

query = 'update customerInfo set Location = %s Where CourseName = %s'
data = ('UK', 'Jmeter')
cursor.execute(query, data)
conn.commit()
conn.close()






