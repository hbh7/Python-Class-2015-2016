Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:16:59) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> list(range(7))
[0, 1, 2, 3, 4, 5, 6]
>>> list(range(3))
[0, 1, 2]
>>> list(range(1,5)
     )
[1, 2, 3, 4]
>>> list(range(20,25))
[20, 21, 22, 23, 24]
>>> list(range(-5,5))
[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]
>>> list(range(2,20,2))
[2, 4, 6, 8, 10, 12, 14, 16, 18]
>>> for i in range(5):
	print(i)

	
0
1
2
3
4
>>> for i in range(5):
print(i)
SyntaxError: expected an indented block
>>> for year in range(1980,2020):
	print("in the year {} ... ".format(year))

	
in the year 1980 ... 
in the year 1981 ... 
in the year 1982 ... 
in the year 1983 ... 
in the year 1984 ... 
in the year 1985 ... 
in the year 1986 ... 
in the year 1987 ... 
in the year 1988 ... 
in the year 1989 ... 
in the year 1990 ... 
in the year 1991 ... 
in the year 1992 ... 
in the year 1993 ... 
in the year 1994 ... 
in the year 1995 ... 
in the year 1996 ... 
in the year 1997 ... 
in the year 1998 ... 
in the year 1999 ... 
in the year 2000 ... 
in the year 2001 ... 
in the year 2002 ... 
in the year 2003 ... 
in the year 2004 ... 
in the year 2005 ... 
in the year 2006 ... 
in the year 2007 ... 
in the year 2008 ... 
in the year 2009 ... 
in the year 2010 ... 
in the year 2011 ... 
in the year 2012 ... 
in the year 2013 ... 
in the year 2014 ... 
in the year 2015 ... 
in the year 2016 ... 
in the year 2017 ... 
in the year 2018 ... 
in the year 2019 ... 
>>> cats = ['manx', 'tabby', 'calico']
>>> for cat in cats:
	print ("That's a nice {} you have there!".format(cat))

	
That's a nice manx you have there!
That's a nice tabby you have there!
That's a nice calico you have there!
>>> numbers = [5,2,0,20,30]
>>> for number in numbers:
	if number == 0:
		print ("Ugh. You have me a 0")
		continue
	new_number = 100.0/number
	print ("100/{} = {}".format(number, new_number))

	
100/5 = 20.0
100/2 = 50.0
Ugh. You have me a 0
100/20 = 5.0
100/30 = 3.3333333333333335
>>> cart = [20.25,30.04,102.4,50,80]
>>> for item in cart:
	print(item)
	if item > 100:
		print ("You are going to require insurrance on this order.")
		break

	
20.25
30.04
102.4
You are going to require insurrance on this order.
>>> cart =[50.25,20.98,99.99,1.24,0.84,60.03]
>>> for item in cart:
	print (item)
	if item > 100:
		print ("You are going to require insurrance on this order.")
		break
else: #Note that this else is for the for loop and not the if condition
	print ("No insurance will be required for this order.")

	
50.25
20.98
99.99
1.24
0.84
60.03
No insurance will be required for this order.
>>> 
= RESTART: E:/School/2015-2016/Programming/Python/Hour_7/Hour_07_programs.py =
Please give me your age in years (e.g. 30): 17 years
I'm sorry, but 17 years isn't valid.
Please give me your age in years (e.g. 30): seventeen
I'm sorry, but seventeen isn't valid.
Please give me your age in years (e.g. 30): 17
Thanks! Your age is set to 17
>>> while True:
	text = input("Give me some text, and I'll count the e's. Enter 'q' to quit: ")
	if text == 'q':
		break
	print (text.count('e'))

	
Give me some text, and I'll count the e's. Enter 'q' to quit: quest for the Holy Grail
2
Give me some text, and I'll count the e's. Enter 'q' to quit: I blow my nose at you 
1
Give me some text, and I'll count the e's. Enter 'q' to quit: your father smelt of elderberries
6
Give me some text, and I'll count the e's. Enter 'q' to quit: q
>>> while True:
	text = input("Give me some text, and I'll count the e's. Enter 'q' to quit: ")
	if text == 'q':
		break
	print (text.count('e'))

	
Give me some text, and I'll count the e's. Enter 'q' to quit: queen
2
Give me some text, and I'll count the e's. Enter 'q' to quit: 
