import sqlite3
import sys 

def buildCursor():
    global conn
    conn = sqlite3.connect('students.db')
    global cursor 
    cursor = conn.cursor()

def inputData():
    name = input('Student\'s name: ')
    username = input('Student\'s username: ')
    id_num = input('Student\'s id number: ')
    sql = ''' INSERT INTO students
              (name, username, id)
              VALUES (:st_name, :st_username, :id_num)'''
    cursor.execute(sql, {'st_name':name, 'st_username':username, 'id_num':id_num})
    conn.commit()

def retrieveData():
    sql = "select * from students"
    data = cursor.execute(sql)
    retrievedData = data.fetchall()
    for student in retrievedData:
        print (student)

def modifyData():
    field = input("What do you want to modify? [name, username, id]: ")
    if field != "name" and field != "username" and field != "id":
        print ("Invalid Input")
        return
    oldText = input("Which entry would you like to modify? ")
    newText = input("What do you want to put instead? ")

    if field == "name": 
        cursor.execute("""UPDATE students SET name = ? WHERE name = ?""", (newText, oldText))
    elif field == "username":
        cursor.execute("""UPDATE students SET username = ? WHERE username = ?""", (newText, oldText))
    elif field == "id":
        cursor.execute("""UPDATE students SET id = ? WHERE id = ?""", (newText, oldText))

    conn.commit()

def removeData():
    name = input("Who do you want to delete? ")
    cursor.execute("""DELETE FROM students WHERE name=?""", (name,))

    conn.commit()
# Start
run = True
buildCursor()
try:
    sql = '''create table students (
        name text,
        username text,
        id int)'''
    cursor.execute(sql)
    print ("No database found, creating students.db")
except:
    print ("Database aready exists, using students.db")

print ("Welcome to the Student Database!")

while run == True:
    control = input("Please select an option. [Input][Retrieve][Modify][Remove][Exit]: ")
    #control = "modify" # OVERRIDE
    if control.lower() == "input":
        inputData()
    elif control.lower() == "retrieve":
        retrieveData()
    elif control.lower() == "modify":
        modifyData()
    elif control.lower() == "remove":
        removeData()
    elif control.lower() == "exit":
        run = False
    else:
        print ("Invalid Input")




cursor.close() 
