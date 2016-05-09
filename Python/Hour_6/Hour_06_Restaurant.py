print ("Hunter Harris - 10-26-15")

inventory = ['butter',
 'tomato sauce',
 'green beans',
 'chicken',
 'italian herbs',
 'garlic',
 'hamburger',
 'flour',
 'eggs',
 'noodles']
yes_text = "Yes, we have {}."

print ("Welcome to the Inventory program!")
item = input("What item do you want to check? ")
if item in inventory:
    print (yes_text.format(item))
else:
    print ("No, we don't have that.")
