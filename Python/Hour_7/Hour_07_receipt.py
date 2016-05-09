print ("Hunter Harris - 11-24-15")
print ("Welcome to the receipt program!")

total = 0

while True:
    value = input('Enter the value for the seat [\'q\' to quit]: ')
    if value == 'q' or value == 'Q':
        print ("*****")
        print ("Total: $" + str(total))
        break
    else:
        try:
            total += float(value)
        except:
            print ('Sorry, {} isn\'t valid.'.format(value))
print ("Thanks for playing!")
