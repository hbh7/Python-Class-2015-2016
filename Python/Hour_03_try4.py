a = 5
try:
    a = a + 1
    a = a/0
except ZeroDivisionError:
    print ("Please don't do that.")

print (a)

