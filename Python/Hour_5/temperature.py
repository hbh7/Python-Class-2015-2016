import sys

# Temperature.py
# Hunter Harris
# 10-14-15
# Design and Coding: Temperature Program

# Bugs:
# 

tempcin = float(input("Enter a temperature in Celcius: "))
tempcout = ((9.0/5.0) * tempcin + 32.0)

print ("Your temperature in Farhenheit is ", tempcout)


tempfin = float(input("Enter a temperature in Farhrenheit: "))
tempfout = ((5.0 * (tempfin - 32.0)) / 9.0)

print ("Your temperature in Farhenheit is ", tempfout)
