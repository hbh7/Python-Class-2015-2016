Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:16:59) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: E:\School\2015-2016\Programming\Python\Hour_7\Hour_07_restaurant.py 
Traceback (most recent call last):
  File "E:\School\2015-2016\Programming\Python\Hour_7\Hour_07_restaurant.py", line 8, in <module>
    meal_time = raw_input('Which mealtime do you want? [breakfast, lunch, dinner, q to quit] ')
NameError: name 'raw_input' is not defined
>>> 
 RESTART: E:\School\2015-2016\Programming\Python\Hour_7\Hour_07_restaurant.py 
Which mealtime do you want? [breakfast, lunch, dinner, q to quit] breakfast
Specials for breakfast :
Texas Omelet
Contains brisket, horseradish cheddar
Which mealtime do you want? [breakfast, lunch, dinner, q to quit] lunch
Specials for lunch :
Greek patty melt
Like the regular one, but with tzatziki sauce
Which mealtime do you want? [breakfast, lunch, dinner, q to quit] dinner
Specials for dinner :
Buffalo steak
Top loin with hot sauce and blue cheese. NOT BUFFALO MEAT.
Which mealtime do you want? [breakfast, lunch, dinner, q to quit] q
Goodbye!
>>> 
 RESTART: E:\School\2015-2016\Programming\Python\Hour_7\Hour_07_restaurant.py 
Which mealtime do you want? [breakfast, lunch, dinner, q to quit] queen
Specials for queen :
Sorry, queen isn't valid.
Which mealtime do you want? [breakfast, lunch, dinner, q to quit] 
 RESTART: E:\School\2015-2016\Programming\Python\Hour_7\Hour_07_restaurant.py 
Which mealtime do you want? [breakfast, lunch, dinner, q to quit] Q
Traceback (most recent call last):
  File "E:\School\2015-2016\Programming\Python\Hour_7\Hour_07_restaurant.py", line 9, in <module>
    if meal_time == 'q' | meal_time == 'Q':
TypeError: unsupported operand type(s) for |: 'str' and 'str'
>>> 
 RESTART: E:\School\2015-2016\Programming\Python\Hour_7\Hour_07_restaurant.py 
Which mealtime do you want? [breakfast, lunch, dinner, q to quit] Q
Goodbye!
>>> 
 RESTART: E:\School\2015-2016\Programming\Python\Hour_7\Hour_07_restaurant.py 
Hunter Harris - 11-24-15
Which mealtime do you want? [breakfast, lunch, dinner, q to quit] q
Goodbye!
>>> 
