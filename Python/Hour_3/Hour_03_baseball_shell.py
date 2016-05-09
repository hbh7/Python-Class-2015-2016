Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:27:37) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
===== RESTART: E:/School/2015-2016/Programming/Python/Hour_3/03hello.py =====
Hello world!
What is your name?
Hunter
It is good to meet you, Hunter
>>> 
===== RESTART: E:/School/2015-2016/Programming/Python/Hour_3/03hello.py =====
Hello world!
What is your name?
memes
Traceback (most recent call last):
  File "E:/School/2015-2016/Programming/Python/Hour_3/03hello.py", line 6, in <module>
    print ("It is good to meet you, " + MYNAME)
NameError: name 'MYNAME' is not defined
>>> 
===== RESTART: E:/School/2015-2016/Programming/Python/Hour_3/03hello.py =====
Hello world!
What is your name?
potatoes
It is good to meet you, potatoes
>>> myName
'potatoes'
>>> 
=== RESTART: E:/School/2015-2016/Programming/Python/Hour_3/Hour_03_bank.py ===
Welcome to Meme Bank, Please enter your acount number
What is your account number? 55555555555
>>> 
=== RESTART: E:/School/2015-2016/Programming/Python/Hour_3/Hour_03_bank.py ===
Welcome to Meme Bank, Please enter your acount number
What is your account number?6700
>>> 
=== RESTART: E:/School/2015-2016/Programming/Python/Hour_3/Hour_03_bank.py ===
Welcome to Meme Bank, Please enter your acount number
What is your account number? 6700
Traceback (most recent call last):
  File "E:/School/2015-2016/Programming/Python/Hour_3/Hour_03_bank.py", line 13, in <module>
    print ("You have $" + str(Account1Cash))
NameError: name 'Account1Cash' is not defined
>>> 
=== RESTART: E:/School/2015-2016/Programming/Python/Hour_3/Hour_03_bank.py ===
Welcome to Meme Bank, Please enter your acount number
What is your account number? 6700
Traceback (most recent call last):
  File "E:/School/2015-2016/Programming/Python/Hour_3/Hour_03_bank.py", line 13, in <module>
    print ("You have $" + str(Account1Cash))
NameError: name 'Account1Cash' is not defined
>>> 
=== RESTART: E:/School/2015-2016/Programming/Python/Hour_3/Hour_03_bank.py ===
Welcome to Meme Bank, Please enter your acount number
What is your account number? 6700
You have $12.62
You have money!
>>> 
=== RESTART: E:/School/2015-2016/Programming/Python/Hour_3/Hour_03_bank.py ===
Welcome to Meme Bank, Please enter your acount number
What is your account number? 6700
You have $12.62
You have money!
>>> 
=== RESTART: E:/School/2015-2016/Programming/Python/Hour_3/Hour_03_bank.py ===
Welcome to Meme Bank, Please enter your acount number
What is your account number? 7777
You have $0.0
You're out of money!
>>> 
=== RESTART: E:/School/2015-2016/Programming/Python/Hour_3/Hour_03_bank.py ===
Welcome to Meme Bank, Please enter your acount number
What is your account number? 4820
You have $-984.22
You are out of money!
>>> 
=== RESTART: E:/School/2015-2016/Programming/Python/Hour_3/Hour_03_bank.py ===
Welcome to Meme Bank, Please enter your acount number
What is your account number? 
=== RESTART: E:/School/2015-2016/Programming/Python/Hour_3/Hour_03_bank.py ===
Welcome to Meme Bank, Please enter your acount number
What is your account number? hi
Traceback (most recent call last):
  File "E:/School/2015-2016/Programming/Python/Hour_3/Hour_03_bank.py", line 10, in <module>
    User = int(input("What is your account number? "))
ValueError: invalid literal for int() with base 10: 'hi'
>>> 
=== RESTART: E:/School/2015-2016/Programming/Python/Hour_3/Hour_03_bank.py ===
Welcome to Meme Bank, Please enter your acount number
What is your account number? adfdsf
Please ensure you are only using numbers in your account number.
Traceback (most recent call last):
  File "E:/School/2015-2016/Programming/Python/Hour_3/Hour_03_bank.py", line 17, in <module>
    if User==6700:
NameError: name 'User' is not defined
>>> 
=== RESTART: E:/School/2015-2016/Programming/Python/Hour_3/Hour_03_bank.py ===
Welcome to Meme Bank, Please enter your acount number
What is your account number? afadf
Please ensure you are only using numbers in your account number.
Error: Your ID is not registered with our system.
>>> 
=== RESTART: E:/School/2015-2016/Programming/Python/Hour_3/Hour_03_bank.py ===
Welcome to Meme Bank, Please enter your acount number
What is your account number? dassad
Error: Please ensure you are only using numbers in your account number.
Error: Your ID is not registered with our system.
--------------
QUESTION 2:
--------------

>>> 
=== RESTART: E:/School/2015-2016/Programming/Python/Hour_3/Hour_03_bank.py ===
Welcome to Potato Bank, Please enter your acount number
Made by Hunter Harris, 9-17-15
What is your account number? 5
Error: Your ID is not registered with our system.

-----------
QUESTION 2:
-----------

Please input a friend's name: matt
Traceback (most recent call last):
  File "E:/School/2015-2016/Programming/Python/Hour_3/Hour_03_bank.py", line 66, in <module>
    if Friend==matt:
NameError: name 'matt' is not defined
>>> 
=== RESTART: E:/School/2015-2016/Programming/Python/Hour_3/Hour_03_bank.py ===
Welcome to Potato Bank, Please enter your acount number
Made by Hunter Harris, 9-17-15
What is your account number? 
Error: Please ensure you are only using numbers in your account number.
Error: Your ID is not registered with our system.

-----------
QUESTION 2:
-----------

Please input a friend's name: matt
They would like to see the new Star Wars movie.
>>> 
=== RESTART: E:/School/2015-2016/Programming/Python/Hour_3/Hour_03_bank.py ===

-----------
QUESTION 1:
-----------

Welcome to Potato Bank, Please enter your acount number
Made by Hunter Harris, 9-17-15
What is your account number? 
Error: Please ensure you are only using numbers in your account number.
Error: Your ID is not registered with our system.

-----------
QUESTION 2:
-----------

Please input a friend's name: 
Error: Something went wrong.
Traceback (most recent call last):
  File "E:/School/2015-2016/Programming/Python/Hour_3/Hour_03_bank.py", line 72, in <module>
    if Friend=="matt":
NameError: name 'Friend' is not defined
>>> 
=== RESTART: E:/School/2015-2016/Programming/Python/Hour_3/Hour_03_bank.py ===

-----------
QUESTION 1:
-----------

Welcome to Potato Bank, Please enter your acount number
Made by Hunter Harris, 9-17-15
What is your account number? 
Error: Please ensure you are only using numbers in your account number.
Error: Your ID is not registered with our system.

-----------
QUESTION 2:
-----------

Traceback (most recent call last):
  File "E:/School/2015-2016/Programming/Python/Hour_3/Hour_03_bank.py", line 64, in <module>
    Friend = NA
NameError: name 'NA' is not defined
>>> 
=== RESTART: E:/School/2015-2016/Programming/Python/Hour_3/Hour_03_bank.py ===

-----------
QUESTION 1:
-----------

Welcome to Potato Bank, Please enter your acount number
Made by Hunter Harris, 9-17-15
What is your account number? 
Error: Please ensure you are only using numbers in your account number.
Error: Your ID is not registered with our system.

-----------
QUESTION 2:
-----------

Please input a friend's name: 
Error: Something went wrong.
Error: Friend name is not registered with our system.
>>> 
=== RESTART: E:/School/2015-2016/Programming/Python/Hour_3/Hour_03_bank.py ===

-----------
QUESTION 1:
-----------

Welcome to Potato Bank!
Made by Hunter Harris, 9-17-15
What is your account number? 
Error: Please ensure you are only using numbers in your account number.
Error: Your ID is not registered with our system.

-----------
QUESTION 2:
-----------

Please input a friend's name: 
Error: Something went wrong.
Error: Friend name is not registered with our system.
>>> 
= RESTART: E:/School/2015-2016/Programming/Python/Hour_3/Hour_03_baseball.py =
Made by Hunter Harris, 9-17-15
Question 1: How far ahead is the leading team's score? 14
Question 2: Does the winning team have the ball? yes
Question 3: How many seconds are left in the game? 46
Traceback (most recent call last):
  File "E:/School/2015-2016/Programming/Python/Hour_3/Hour_03_baseball.py", line 22, in <module>
    points = points^2
TypeError: unsupported operand type(s) for ^: 'float' and 'int'
>>> 
= RESTART: E:/School/2015-2016/Programming/Python/Hour_3/Hour_03_baseball.py =
Made by Hunter Harris, 9-17-15
Question 1: How far ahead is the leading team's score? 14
Question 2: Does the winning team have the ball? yes
Question 3: How many seconds are left in the game? 46
Traceback (most recent call last):
  File "E:/School/2015-2016/Programming/Python/Hour_3/Hour_03_baseball.py", line 22, in <module>
    points = points^2
TypeError: unsupported operand type(s) for ^: 'float' and 'int'
>>> 
= RESTART: E:/School/2015-2016/Programming/Python/Hour_3/Hour_03_baseball.py =
Made by Hunter Harris, 9-17-15
Question 1: How far ahead is the leading team's score? 14
Question 2: Does the winning team have the ball? yes
Question 3: How many seconds are left in the game? 46
Traceback (most recent call last):
  File "E:/School/2015-2016/Programming/Python/Hour_3/Hour_03_baseball.py", line 22, in <module>
    points = points^2
TypeError: unsupported operand type(s) for ^: 'float' and 'int'
>>> 
= RESTART: E:/School/2015-2016/Programming/Python/Hour_3/Hour_03_baseball.py =
Made by Hunter Harris, 9-17-15
Question 1: How far ahead is the leading team's score? 14
Question 2: Does the winning team have the ball? yes
Question 3: How many seconds are left in the game? 46
Traceback (most recent call last):
  File "E:/School/2015-2016/Programming/Python/Hour_3/Hour_03_baseball.py", line 22, in <module>
    points = points^2.0
TypeError: unsupported operand type(s) for ^: 'float' and 'float'
>>> 
= RESTART: E:/School/2015-2016/Programming/Python/Hour_3/Hour_03_baseball.py =
Made by Hunter Harris, 9-17-15
Question 1: How far ahead is the leading team's score? 14
Question 2: Does the winning team have the ball? yes
Question 3: How many seconds are left in the game? 46
The lead is safe.
>>> 
= RESTART: E:/School/2015-2016/Programming/Python/Hour_3/Hour_03_baseball.py =
>>> 
Made by Hunter Harris, 9-17-15
Question 1: How far ahead is the leading team's score? 18
Question 2: Does the winning team have the ball? no
Question 3: How many seconds are left in the game? 130
The lead is safe.
>>> 
= RESTART: E:/School/2015-2016/Programming/Python/Hour_3/Hour_03_baseball.py =
Made by Hunter Harris, 9-17-15
Question 1: How far ahead is the leading team's score? 3
Question 2: Does the winning team have the ball? yes
Question 3: How many seconds are left in the game? 14
The lead is not safe.
>>> 
= RESTART: E:/School/2015-2016/Programming/Python/Hour_3/Hour_03_baseball.py =
Made by Hunter Harris, 9-17-15
Question 1: How far ahead is the leading team's score? 8
Question 2: Does the winning team have the ball? yes
Question 3: How many seconds are left in the game? 17
The lead is safe.
>>> 
= RESTART: E:/School/2015-2016/Programming/Python/Hour_3/Hour_03_baseball.py =
Made by Hunter Harris, 9-17-15
Question 1: How far ahead is the leading team's score? 10
Question 2: Does the winning team have the ball? yes
Question 3: How many seconds are left in the game? 81
The lead is not safe.
>>> 
= RESTART: E:/School/2015-2016/Programming/Python/Hour_3/Hour_03_baseball.py =
Made by Hunter Harris, 9-17-15
Question 1: How far ahead is the leading team's score? 7
Question 2: Does the winning team have the ball? no
Question 3: How many seconds are left in the game? 11
The lead is safe.
>>> 
= RESTART: E:/School/2015-2016/Programming/Python/Hour_3/Hour_03_baseball.py =
Made by Hunter Harris, 9-17-15
Question 1: How far ahead is the leading team's score? 18
Question 2: Does the winning team have the ball? no
Question 3: How many seconds are left in the game? 210
The lead is safe.
>>> 
