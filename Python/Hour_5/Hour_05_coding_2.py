Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:27:37) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> name = raw_input()
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    name = raw_input()
NameError: name 'raw_input' is not defined
>>> age = input()
30 years
>>> print(age)
30 years
>>> age
'30 years'
>>> name = input("Please give me your name: ")
Please give me your name: Andrew
>>> name
'Andrew'
>>> age = input()
17
>>> age
'17'
>>> age = float(age)
>>> age
17.0
>>> height = 67.75
>>> int(height)
67
>>> age = input("What is your age? ")
What is your age? 12.5
>>> age
'12.5'
>>> int(age)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    int(age)
ValueError: invalid literal for int() with base 10: '12.5'
>>> from getpass import getpass
>>> password = getpass()

Warning (from warnings module):
  File "C:\Users\newhb\AppData\Local\Programs\Python\Python35\lib\getpass.py", line 101
    return fallback_getpass(prompt, stream)
GetPassWarning: Can not control echo on the terminal.
Warning: Password input may be echoed.
Password: 
>>> password
''
>>> from getpass import getpass
>>> password = getpass('Password, please: ')
Warning: Password input may be echoed.
Password, please: potato
>>> passwrod
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    passwrod
NameError: name 'passwrod' is not defined
>>> password
'potato'
>>> password = getpass('Password, please: ')
Warning: Password input may be echoed.
Password, please: 
>>> password
''
>>> year = input("What year were you born [ex: 1996]? ")
What year were you born [ex: 1996]? 1999
>>> year
'1999'
>>> year = input("What year were you born [ex: 1996]? ")
What year were you born [ex: 1996]? 1999
>>> if len(year) != 4 or not year.isdigit():
	print("I'm sorry, I dont like that number")
else:
	print("That's good. Moving on!")

	
That's good. Moving on!
>>> name = input("Street name, please: ")
Street name, please: "    Pent Road     "
>>> name
'"    Pent Road     "'
>>> name = name.strip()
>>> name
'"    Pent Road     "'
>>> name = input("Street name, please: ")
Street name, please:     Pent Road    
>>> name
'    Pent Road    '
>>> name = name.strip()
>>> name
'Pent Road'
>>> name = "Muneeb"
>>> time = "morning"
>>> print ("Good" + time + "," + name + ". How are you doing?")
Goodmorning,Muneeb. How are you doing?
>>> greeting = "Good {}, {}. How are you doing?"
>>> name = "Muneeb"
>>> time = "morning"
>>> print (greeting.format(time,name))
Good morning, Muneeb. How are you doing?
>>> specials_text = "Good {time}? Today's specials are: {special1} and {special2}."
>>> time = "afternoon"
>>> food1 = "spam with eggs"
>>> food2 = "eggs with spam"
>>> print (specials_text.format(time=time, special1 = food1, special2 = food2))
Good afternoon? Today's specials are: spam with eggs and eggs with spam.
>>> line = "Cities with Python meet-ups: {0}, {1}, {2}"
>>> print(line.format("District of Columbia", "Baltimore", "and many more!"))
Cities with Python meet-ups: District of Columbia, Baltimore, and many more!
>>> fruit = "Types of fruit on sale: {}, {}, and {}."
>>> fruit.format('apples','pears')
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    fruit.format('apples','pears')
IndexError: tuple index out of range
>>> fruit = "Types of fruit on sale: {}, {}, and {}."
>>> fruit.format('apples','pears', 'mangos', 'bananas')
'Types of fruit on sale: apples, pears, and mangos.'
>>> 
