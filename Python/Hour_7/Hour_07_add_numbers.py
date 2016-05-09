print ("Hunter Harris - 11-20-15")

numbers_to_add = int(input("How many numbers would you like to add? "))
sum = 0
counter = 1
while counter <= numbers_to_add:
        number = int(input("What number would you like to add? "))
        sum = sum + number
        counter = counter + 1
print ("The sum is", sum)
