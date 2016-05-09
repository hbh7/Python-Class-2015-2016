Python 3.5.0 (default, Sep 20 2015, 11:28:25) 
[GCC 5.2.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> def print_total(customer_name, items):
	print ("Total for {}".format(customer_name))
	total = 0
	for item in items:
		total = total + item
	print ("${}".format(total))

	
>>> print_total(items=[4.52,6.31,5.00], customer_name="Max")
Total for Max
$15.829999999999998
>>> print_total(items=[4.52,6.31,5.00], "Max")
SyntaxError: positional argument follows keyword argument
>>> print_total(items=[4.52,6.31,5.00])
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print_total(items=[4.52,6.31,5.00])
TypeError: print_total() missing 1 required positional argument: 'customer_name'
>>> def print_welcome(first, last, middle=' '):
	print ("Welcome, {} {} {}".format(first, middle, last))
	print ("Enjoy your stay!")

	
>>> print_welcome(first = "Edwin", last = "Castellano
	      
SyntaxError: EOL while scanning string literal
>>> print_welcome(first = "Edwin", last = "Castellano")
Welcome, Edwin   Castellano
Enjoy your stay!
>>> def print_welcome(first, last, middle=''):
	print ("Welcome, {} {} {}".format(first, middle, last))
	print ("Enjoy your stay!")

	
>>> print_welcome(first = "Edwin", last = "Castellano")
Welcome, Edwin  Castellano
Enjoy your stay!
>>> print_welcome(first = "Saul", middle="Danger", last = "Gutierrez")
Welcome, Saul Danger Gutierrez
Enjoy your stay!
>>> def get_total(items):
	total = 0
	for item in items
	
SyntaxError: invalid syntax
>>> def get_total(items):
	total = 0
	for item in items:
		total = total + item
	return total

>>> items = [2,5,7,8,2]
>>> items_total = get_total(items)
>>> items_total
24
>>> def get_square_and_cube(number)
SyntaxError: invalid syntax
>>> def get_square_and_cube(number):
	square = number ** 2
	cube = number ** 3
	return square, cube

>>> result = get_square_and_cube(5)
>>> result
(25, 125)
>>> square,cube = get_square_and_cube(4)
>>> square
16
>>> cube
64
>>> def get_five_things():
	return 1,2,3,4,5

>>> a,b,c = get_five_things
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    a,b,c = get_five_things
TypeError: 'function' object is not iterable
>>> a,b,c = get_five_things()
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    a,b,c = get_five_things()
ValueError: too many values to unpack (expected 3)
>>> a,b,c,d,e,f = get_five_things()
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    a,b,c,d,e,f = get_five_things()
ValueError: not enough values to unpack (expected 6, got 5)
>>> def check_year(year):
	if len(year) != 4:
		print ("{} is invalid as a year.".format(year))
		return
	print ("Good, that seems to work aas a year!")

	
>>> check_year("80")
80 is invalid as a year.
>>> def get_name()
SyntaxError: invalid syntax
>>> def get_name():
	name = input("Give me your name")

	
>>> get_name()
Give me your name
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    get_name()
  File "<pyshell#57>", line 2, in get_name
    name = input("Give me your name")
  File "/usr/lib/python3.5/idlelib/PyShell.py", line 1385, in readline
    line = self._line_buffer or self.shell.readline()
TypeError: 'int' object is not callable
>>> def get_name():
	name = input("Give me your name: ")

	
>>> get_name()
Give me your name: Hunter
>>> name
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    name
NameError: name 'name' is not defined
>>> def add_five(x):
	x = x+5
	print (x)

	
>>> x = 5
>>> add_five(x)
10
>>> x
5
>>> def test_args(item_one, item_two, **kwargs):
	print (item_one)
	print (item_two)
	print (kwargs)

	
>>> test_args(item_one="Hello", item_two="world", item_three="How are you?")
Hello
world
{'item_three': 'How are you?'}
>>> def test_args(first, second, *args):
	print (first)
	print (second)
	print (args)

	
>>> test_args(1,2,3,4,5)
1
2
(3, 4, 5)
>>> python
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    python
NameError: name 'python' is not defined
>>> python= 0
>>> python
0
>>> 
