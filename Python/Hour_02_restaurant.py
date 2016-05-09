person1 = 12.50
person2 = 13.25
person3 = 11.64
person4 = 27.90
person5 = 17.85
apetizers = 13.50
mealsTotal = person1 + person2 + person3 + person4 + person5 + apetizers
tax = 1.065

print ("Total Price before Tax: $", "%.2f" % round(mealsTotal,2))

mealsTotalTax = mealsTotal * tax

print ("\nTotal Price with Tax: $", "%.2f" % round(mealsTotalTax,2))

# 2nd Part
a5thOfApetizers = apetizers / 5

person1Bill = ((2 * a5thOfApetizers) + person1 + person2) * tax
person2Bill = 0
person3Bill = ((2 * a5thOfApetizers) + person3 + person4) * tax
person4Bill = 0
person5Bill = (person5 + a5thOfApetizers) * tax

print ("\nTotal Price For Person 1 to pay: $", "%.2f" % round(person1Bill,2))
print ("\nTotal Price For Person 2 to pay: $", "%.2f" % round(person2Bill,2))
print ("\nTotal Price For Person 3 to pay: $", "%.2f" % round(person3Bill,2))
print ("\nTotal Price For Person 4 to pay: $", "%.2f" % round(person4Bill,2))
print ("\nTotal Price For Person 5 to pay: $", "%.2f" % round(person5Bill,2))

