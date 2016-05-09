Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:27:37) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> number = input()
5
>>> number
'5'
>>> s = input()
Hello
>>> S
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    S
NameError: name 'S' is not defined
>>> s
'Hello'
>>> t = input()
"Hello"
>>> t
'"Hello"'
>>> u = input()
'Hello'
>>> u
"'Hello'"
>>> name = raw_input()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    name = raw_input()
NameError: name 'raw_input' is not defined
>>> 
