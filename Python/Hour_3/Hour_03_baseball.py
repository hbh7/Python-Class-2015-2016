import sys

print ("Made by Hunter Harris, 9-17-15")
score = 0

try:
    score = float(input("Question 1: How far ahead is the leading team's score? "))
    hasBall = str(input("Question 2: Does the winning team have the ball? "))
    secondsRemaining = float(input("Question 3: How many seconds are left in the game? "))
except:
    print ("Error: Something went wrong. Try again.")

score = score - 3
if hasBall == "yes":
    points = score + 0.5
elif hasBall == "no":
    points = score - 0.5
else:
    print ("Error: Something other than 'yes' or 'no' was entered for the second question. ")
    sys.exit()

points = points**2.0

if points > secondsRemaining:
    print ("The lead is safe.")
else:
    print ("The lead is not safe.")






