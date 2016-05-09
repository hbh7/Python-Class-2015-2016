print ("Hunter Harris - 9-28-15")

asterics = 0
breakfast_special = "Texas Omelet"
breakfast_notes = "Contains brisket, horseradish cheddar"
lunch_special = "Greek patty melt"
lunch_notes = "Like the regular one, but with tzatziki sauce"
dinner_special = "Buffalo steak"
dinner_notes = "Top loin with hot sauce and blue cheese. NOT BUFFALO MEAT."
breakfast_special2 = "Chocolate Chip Pancakes"
breakfast_notes2 = "Three large pancakes mixed with semi-sweet morsels of chocolate"
breakfast_price2 = 4.99
lunch_special2 = "Monte Cristo Sandwich"
lunch_notes2 = "Thick slices of sourdough bread surrounding ham and cheese, grilled and served with maple syrup"
lunch_price2 = 5.99
dinner_special2 = "1/2 lb Angus Buffalo Burger"
dinner_notes2 = "Half pound of 100% Angus buffalo ground beef surved on a sesame seed bun with lettuce, tomato, onion, and barbecue sauce"
dinner_price2 = 8.99

if len(breakfast_notes) > asterics:
    asterics = len(breakfast_notes)
if len(lunch_notes) > asterics:
    asterics = len(lunch_notes2)
if len(dinner_notes) > asterics:
    asterics = len(dinner_notes)
if len(breakfast_notes2) > asterics:
    asterics = len(breakfast_notes2)
if len(lunch_notes2) > asterics:
    asterics = len(lunch_notes2)
if len(dinner_notes2) > asterics:
    asterics = len(dinner_notes2)

print ("\nToday's specials\n" + "*"*asterics)
print ("Breakfast: ", end="")
print (breakfast_special.upper())
print (breakfast_notes)
print ()
print ("Lunch: ",end="")
print (lunch_special.upper())
print (lunch_notes)
print ()
print ("Dinner: ",end="")
print (dinner_special.upper())
print (dinner_notes)

print ("\nTomorrow's specials\n" + "*"*asterics)
print ("Breakfast: ", end="")
print (breakfast_special2.upper(), "\t\t$", breakfast_price2)
print (breakfast_notes2)
print ()
print ("Lunch: ",end="")
print (lunch_special2.upper(), "\t\t\t$", lunch_price2)
print (lunch_notes2)
print ()
print ("Dinner: ",end="")
print (dinner_special2.upper(), "\t\t$", dinner_price2)
print (dinner_notes2)

print ("\nCalculations \n" + "*"*asterics)
print ("2 orders of", breakfast_special2, "\t\t$", (breakfast_price2*2), "\n")
# print ("Orders of", (breakfast_special2 + ",") + (lunch_special2, ","), dinner_special2, "\t\t$", (dinner_price2*2))
print ("Orders of Chocolate Chip Pancakes, Monte Cristo Sandwich, and 1/2 lb Angus Buffalo Burger" , "\n\t\t\t\t\t\t$", (dinner_price2+breakfast_price2+lunch_price2), "\n")
print ("Orders of Chocolate Chip Pancakes, Monte Cristo Sandwich, and 1/2 lb Angus Buffalo Burger, plus 6.5% tax and 20% tip", "\n\t\t\t\t\t\t$", "{0:.2f}".format(((dinner_price2+breakfast_price2+lunch_price2)*1.065*1.2),2))
print ("Tax:\t\t\t\t\t\t$ ", "{0:.2f}".format(((dinner_price2+breakfast_price2+lunch_price2)*0.065),2))
print ("Tip:\t\t\t\t\t\t$ ", "{0:.2f}".format(((dinner_price2+breakfast_price2+lunch_price2)*1.065*0.2),2))






