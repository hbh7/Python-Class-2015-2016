print ("Hunter Harris - 11-24-15")
print ("Welcome to the student checker!")

students = ['Hunter','Emelia','Jarrod','Tyler','Joseph','Tori','Collin','Alex','JanCarlos','Brandom','Quinn','Steven','Antonio','Nathan','Dario','Stephen']

while True:
    value = input('Enter the name of a student [\'q\' to quit]: ')
    if value == 'q' or value == 'Q':
        break
    else:
        if value in students or value.capitalize() in students:
            print ("Yes, that student is enrolled in the class")
        else:
            print ("No, that student is not in this class.")
print ("Thanks for playing!")
