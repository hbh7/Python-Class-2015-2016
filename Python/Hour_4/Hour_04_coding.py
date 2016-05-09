Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:27:37) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> s = "Hello, world"
>>> s
'Hello, world'
>>> name = "Jeremy'
SyntaxError: EOL while scanning string literal
>>> name = "Jeremy' #note the mismatched types of quotse
SyntaxError: EOL while scanning string literal
>>> name = "William"
>>> name
'William'
>>> name2 = 'Vasquez' # note the different types of quotes than before
>>> name2
'Vasquez'
>>> greeting = "Hello"
>>> print (greeting)
Hello
>>> print ('Apple: ', end='')
Apple: 
>>> print ('$1.59 / lb')
$1.59 / lb
>>> 
==== RESTART: E:/School/2015-2016/Programming/Python/Hour_4/Hour_04_1.py ====
Apple: $1.59 / lb
>>> name = ("Maximillion")
>>> len(name)
11
>>> title = "wind in the willows"
>>> title.upper()
'WIND IN THE WILLOWS'
>>> title.lower()
'wind in the willows'
>>> title.capitalize()
'Wind in the willows'
>>> title.title()
'Wind In The Willows'
>>> title
'wind in the willows'
>>> movie_title = "the housetrap"
>>> movie_title.upper()
'THE HOUSETRAP'
>>> movie_title
'the housetrap'
>>> birth_year = "1998"
>>> state = "CT"
>>> birth_year.isdigit()
True
>>> state.isalpha()
True
>>> state.isdigit()
False
>>> state = "2CT3"
>>> state.isdigit()
False
>>> first_name = "Mitchell"
>>> last_name="Buhler"
>>> first_name + last_name
'MitchellBuhler'
>>> first_name + " " + la
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    first_name + " " + la
NameError: name 'la' is not defined
>>> first_name + " " + last_name
'Mitchell Buhler'
>>> s = 'hello '
>>> s * 5
'hello hello hello hello hello '
>>> s * 10
'hello hello hello hello hello hello hello hello hello hello '
>>> s * 0
''
>>> s = '5'
>>> s * 5
'55555'
>>> meme = s * 5
>>> meme.isdigit()
True
>>> s = "hello"
>>> s * -5
''
>>> s * 1.0
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    s * 1.0
TypeError: can't multiply sequence by non-int of type 'float'
>>> a = "Connecticut"
>>> b = "connecticut"
>>> a == b
False
>>> greet1 = "Hello "
>>> greet2 = "Hello"
>>> greet1 == greet2
False
>>> s = "6"
>>> s / 1
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    s / 1
TypeError: unsupported operand type(s) for /: 'str' and 'int'
>>> s / 1
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    s / 1
TypeError: unsupported operand type(s) for /: 'str' and 'int'
>>> s / 1
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    s / 1
TypeError: unsupported operand type(s) for /: 'str' and 'int'
>>> meme
'55555'
>>> s / 1
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    s / 1
TypeError: unsupported operand type(s) for /: 'str' and 'int'
>>> s = 6
>>> s /
SyntaxError: invalid syntax
>>> s / 1
6.0
>>> rhyme = "Little Miss Muffet\nSat on a tuffet\nEating her curds and whey."
>>> print (rhyme)
Little Miss Muffet
Sat on a tuffet
Eating her curds and whey.
>>> rhyme2 = "Little Miss Muffet\n\
Sat on a Tuffet\n\
Eating her curds and whey."
>>> print (rhyme2)
Little Miss Muffet
Sat on a Tuffet
Eating her curds and whey.
>>> header = "Dish\tPrice\tType"
>>> print(header)
Dish	Price	Type
>>> name = 'T'Yanna Dailey'
SyntaxError: invalid syntax
>>> name = 'T\'Yanna Dailey'
>>> print (name)
T'Yanna Dailey
>>> name = "T\'Yanna Dailey"
>>> print (name)
T'Yanna Dailey
>>> path = "C:\\Applications\\"
>>> print (path)
C:\Applications\
>>> first_name = "Austin "
>>> middle_name = "Awesome"
>>> print (first_name + " " + middle_name
       )
Austin  Awesome
>>> if first_name == 'Austin':
	print ("Hi, Austin!")
else:
	print ("Who are you?")

	
Who are you?
>>> first_name = "Austin ") #note the space after the name but before the end quotes
SyntaxError: invalid syntax
>>> first_name = ("Austin ") #note the space after the name but before the end quotes
>>> first_name.strip
<built-in method strip of str object at 0x000000395FBD4CE0>
>>> first_name.strip()
'Austin'
>>> bad_input = "****Austin****"
>>> bad_input.strip('*')
'Austin'
>>> bad_input
'****Austin****'
>>> bad_input.lstrip('*')
'Austin****'
>>> bad_input.rstrip('*')
'****Austin'
>>> print (bad_input
       )
****Austin****
>>> birthday = "Happy birthday to you, \n\
Happy birthday to you, n\n
SyntaxError: EOL while scanning string literal
>>> birthday = "Happy birthday to you, \n\
Happy birthday to you, \n\
Happy birthday dear Hunter, \n\
Happy birthday to you")
SyntaxError: invalid syntax
>>> birthday = "Happy birthday to you, \n\
Happy birthday to you, \n\
Happy birthday dear Hunter, \n\
Happy birthday to you"
>>> birthday.count('Happy')
4
>>> birthday.find('dear')
63
>>> birthday.find('dearfadsfs')
-1
>>> print (birthday.replace('Birthday','Anniversary'))
Happy birthday to you, 
Happy birthday to you, 
Happy birthday dear Hunter, 
Happy birthday to you
>>> print (birthday.replace('birthday','Anniversary'))
Happy Anniversary to you, 
Happy Anniversary to you, 
Happy Anniversary dear Hunter, 
Happy Anniversary to you
>>> print (birthday)
Happy birthday to you, 
Happy birthday to you, 
Happy birthday dear Hunter, 
Happy birthday to you
>>> 
