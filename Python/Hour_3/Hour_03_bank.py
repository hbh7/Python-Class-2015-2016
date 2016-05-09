print ("")
print ("-----------")
print ("QUESTION 1:")
print ("-----------")
print ("")

print ("Welcome to Potato Bank!")
print ("Made by Hunter Harris, 9-17-15")


Account1 = 6700 
Account2 = 7777
Account3 = 4820
Account1Balance = 12.62
Account2Balance = 0.00
Account3Balance = -984.22
User = 0000

def bank():
    try:
        User = int(input("What is your account number? "))
    except:
        print ("Error: Please ensure you are only using numbers in your account number.")



    if User==6700: 
        print ("You have $" + str(Account1Balance))
    
        if Account1Balance > 0.00: 
            print ("You have money!")
        elif Account1Balance == 0:
            print ("You're out of money!")
        elif Account1Balance < 0:
            print ("You are out of money!")
    elif User==7777:
        print ("You have $" + str(Account2Balance))
    
        if Account2Balance > 0.00: 
            print ("You have money!")
        elif Account2Balance == 0:
            print ("You're out of money!")
        elif Account2Balance < 0:
            print ("You are out of money!")
    elif User==4820:
        print ("You have $" + str(Account3Balance))
        
        if Account3Balance > 0.00: 
            print ("You have money!")
        elif Account3Balance == 0:
            print ("You're out of money!")
        elif Account3Balance < 0:
            print ("You are out of money!")
    else:
        print ("Error: Your ID is not registered with our system.")


bank()
bank()
bank()



print ("")
print ("-----------")
print ("QUESTION 2:")
print ("-----------")
print ("")

Friend = "NA"

try:
    Friend = str(input("Please input a friend's name: "))
except:
    print ("Error: Something went wrong.")



if Friend=="matt": 
    print ("They would like to see the new Star Wars movie.")

elif Friend=="amy":
    print ("They would like to see pixels.")

elif Friend=="jake":
    print ("They would like to see anything in theaters.")
    
else:
    print ("Error: Friend name is not registered with our system.")









































