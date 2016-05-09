import sqlite3
conn = sqlite3.connect('mytest2.db')
cursor = conn.cursor()
sql = "select * from students"
results = cursor.execute(sql)
all_students = results.fetchall()
for student in all_students:
    print (student)
