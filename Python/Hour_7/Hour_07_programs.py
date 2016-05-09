age = input("Please give me your age in years (e.g. 30): ")
while not age.isdigit():
    print ("I'm sorry, but {} isn't valid.".format(age))
    age = input("Please give me your age in years (e.g. 30): ")
print ("Thanks! Your age is set to {}".format(age))
