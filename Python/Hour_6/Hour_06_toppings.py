print ("Hunter Harris - 10-26-15")

inventory = ['pepperoni',
 'sausage',
 'cheese',
 'peppers']
yes_text = "We have {}!"
no_text = "Sorry, we don't have {}."

inventorySelected = []

item = input("Please give me a topping: ")

if item in inventory:
    print (yes_text.format(item))
    inventorySelected.append(item)
elif item.lower() in inventory:
    print (yes_text.format(item.lower()))
    inventorySelected.append(item.lower())
else:
    print (no_text.format(item.lower()))
        
item = input("Please give me one more topping: ")

if item in inventory:
    print (yes_text.format(item))
    inventorySelected.append(item)
elif item.lower() in inventory:
    print (yes_text.format(item.lower()))
    inventorySelected.append(item.lower())
else:
    print (no_text.format(item.lower()))

print ("Here are your toppings:")
print (inventorySelected)
