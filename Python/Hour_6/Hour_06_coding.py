
4Python 3.5.0 (default, Sep 20 2015, 11:28:25) 
[GCC 5.2.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> fruit = ['apple', 'strawberry', 'pear', 'papaya']
>>> fruit
['apple', 'strawberry', 'pear', 'papaya']
>>> toppings = []
>>> toppings
[]
>>> times = ['morning', 'afternoon', 'evening', 'night']
>>> times[1]
'afternoon'
>>> times[0]
'morning'
>>> times[3]
'night'
>>> times[4]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    times[4]
IndexError: list index out of range
>>> fruit1 = 'apple'
>>> fruit12 = 'pear'
>>> fruit_list = [fruit1, fruit2]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    fruit_list = [fruit1, fruit2]
NameError: name 'fruit2' is not defined
>>> fruit2 = 'pear'
>>> fruit_list = [fruit1, fruit2]
>>> fruit_list
['apple', 'pear']
>>> 
>>> fruit1 = 'grapes'
>>> fruit_list
['apple', 'pear']
>>> numbers = [1,2,5,7,8]
>>> len(numbers)
5
>>> color_list = ['red', 'blue', 'magenta', 'red', 'yellow']
>>> color_list.count('red")
		 
SyntaxError: EOL while scanning string literal
>>> color_list.count('red")
		 
SyntaxError: EOL while scanning string literal
>>> color_list.count('red')
2
>>> color_list.count('black')
0
>>> color_list.count('e')
0
>>> color_list.index('blue')
1
>>> color_list[1]
'blue'
>>> 'pink' in color_list
False
>>> 'red' in color_list
True
>>> toppings = []
>>> toppings.append('pepperoni')
>>> toppings.append('mushrooms')
>>> toppings
['pepperoni', 'mushrooms']
>>> 
