# Hunter Harris - 10-30-15
# Description: A program that shows the value the Python Debugger

import random
print('I will flip a coin 1000 times. Guess how many times it will come up heads. (Press enter to begin)')
input()
flips = 0
heads = 0
while flips < 1000:
    if random.randint(0, 1) == 1:
        heads = heads + 1
    flips = flips + 1

    if flips == 900:
        print('900 flips and there have been ' + str(heads) + ' heads.')     #set a break point on this line of code
    if flips == 100:
        print('At 100 tosses, heads has come up ' + str(heads) + ' times so far.')     #set a break point on this line of code
    if flips == 500:
        print('Half way done, and heads has come up ' + str(heads) + ' times.')     #set a break point on this line of code

print()
print('Out of 1000 coin tosses, heads came up ' + str(heads) + ' times!')
print('Were you close?')
