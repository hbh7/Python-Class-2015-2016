print ("Hunter Harris - 12-7-15")
print ("Welcome to the Student Checker!")

students = ['Hunter','Emelia','Jarrod','Tyler','Joseph','Tori','Colin','Alex','JanCarlos','Brandom','Quinn','Steven','Antonio','Nathan','Dario','Stephen']

def checkStudent(studentName):
    if studentName in students or studentName.capitalize() in students:
        return True
    else:
        return False


def main():
    while True:
        studentName = input('Enter the name of a student [\'q\' to quit]: ')
        if studentName == 'q' or studentName == 'Q':
            break
        if checkStudent(studentName) == True:
            print ("Yes, that student is enrolled in the class")
            continue
        else:
            print ("No, that student is not in this class.")
            continue

main()    
print ("Thanks for playing!")

