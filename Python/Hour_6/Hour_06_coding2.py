Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:16:59) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> order1 = ['pizza', 'fries', 'baklava']
>>> order2 = ['soda','lasagna']
>>> order1.extend(order2)
>>> order1
['pizza', 'fries', 'baklava', 'soda', 'lasagna']
>>> colors = ['red', 'green', 'yollew']
>>> colors[2] = 'yellow'
>>> colors
['red', 'green', 'yellow']
>>> numbers = [1,2,5,6,7,4,2]
>>> numbers.remove(5)
>>> numbers
[1, 2, 6, 7, 4, 2]
>>> numbers.index(2)
1
>>> numbers = [1,2,5,6,7,5,4,2]
>>> numbers.remove(5)
>>> numbers
[1, 2, 6, 7, 5, 4, 2]
>>> numbers = [1,3,5,6,3,9]
>>> numbers.remove(3)
>>> numbers
[1, 5, 6, 3, 9]
n
>>> umbers.remove(10)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    umbers.remove(10)
NameError: name 'umbers' is not defined
>>> numbers.remove(10)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    numbers.remove(10)
ValueError: list.remove(x): x not in list
>>> colors = ['red', 'yellow', 'green' 'blue', 'indigo', 'violet']
>>> colors.insert(1,'orange')
>>> colors
['red', 'orange', 'yellow', 'greenblue', 'indigo', 'violet']
>>> a = [1,2,4]
>>> b = [5,7,10]
>>> a + b
[1, 2, 4, 5, 7, 10]
>>> nums = [1,2,3]
>>> nums * 3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
>>> names = ['Moe' , 'Larry', 'Curly']
>>> names.reverse()
>>> names
['Curly', 'Larry', 'Moe']
>>> names = ['Moe' , 'Larry', 'Curly']
>>> names.sort()
>>> names
['Curly', 'Larry', 'Moe']
>>> prices = [1, 4.7, 25, 3.0 2.75]
SyntaxError: invalid syntax
>>> prices = [1, 4.7, 25, 3.0, 2.75]
>>> prices.sort()
>>> prices
[1, 2.75, 3.0, 4.7, 25]
>>> prices = ['$1', '$4.7', '$25', '$3.0', '$2.75']
>>> prices.sort()
>>> prices
['$1', '$2.75', '$25', '$3.0', '$4.7']
>>> requested_classes = ['ENGL101', 'CS100', 'SPAN102']
>>> schedule = ['ENGL101', 'CS100', 'SPAN102']
>>> requested_classes == schedule
True
>>> schedule = ['ENGL101', 'SPAN102', 'CS100']
>>> requested_classes == schedule
False
>>> 
