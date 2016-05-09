# Hunter Harris - 10-28-15
# Description: A program that shows the value of the Python debugger

import random
number1 = random.randint(1, 10)
number2 = random.randint(1, 10)
print('What is ' + number1 + ' + ' + number2 + '?')
answer = int(input())
if answer == number1 + number2:
    print ('Correct!')
else:
    print ('Nope! The answer is ' + str(number1 + number2) + '.')
    
