Python 3.5.0 (default, Sep 20 2015, 11:28:25) 
[GCC 5.2.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> def hello():
	print ("Hello! How are you?")

	
>>> hello()
Hello! How are you?
>>> def hello2(name):
	print ("Hello, {}".format(name))

	
>>> hello2('Matthew')
Hello, Matthew
>>> def hello():
	print ("Hello! How are you?")

	
>>> hello
<function hello at 0x7f02fcb62158>
>>> def print_address(name, address):
	print (name)
	print (address)

	
>>> school = "Pathways Academy of Technology and Design"
>>> adress = "2 Pent Road\n\
East Hartford, CT 06118"
>>> print_address(school, address)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    print_address(school, address)
NameError: name 'address' is not defined
>>> address = "2 Pent Road\n\
East Hartford, CT 06118"
>>> print_address(school, address)
Pathways Academy of Technology and Design
2 Pent Road
East Hartford, CT 06118
>>> print ("Hunter Harris - 12-2-15")
Hunter Harris - 12-2-15
>>> def print_total(customer_name, items):
	print ("Total for {}".format(customer_name))
	total = 0
	for item in items:
		total = total + item

		
>>> def print_total(customer_name, items):
	print ("Total for {}".format(customer_name))
	total = 0
	for item in items:
		total = total + item
	print ("${}".format(total))

	
>>> print_total(items=
