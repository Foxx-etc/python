"""
We created A decorator func() and we want to use
it only for once on a Regular_func() to decorate and Later
we be Calling the Regular_func() Again to display his own
definition...:


Being Direct( implementing @decorator Above on a Regular_func() ) Is Not
A Better Approach:
	@decorator
	def Regular_func():

As We Can Recall It, What would happen If We Call The Regular_func()
Again ( it would display the Decoration as we use @decorator 
just above on Regular_func())	
		
		
To Get Out Of This Situation We must Create a object(variable) and
Assing the value as :
	obj = decorator(Regular_func)
	print(obj())                |
	          |                 |
	          |                 |---> NOTE: No braces
              |
              |
              |---> NOTE: Use Braces for object


Now, We Can Free To Call Regular_func() Again To Display his own defintion
without being Decorated!
"""


# Decorator
def mul(l_n):
	
	def wrapper():
		new_l = []
		for i in l_n():
			new_l.append(i * 2)
		return new_l
		
	return wrapper


# Regular_func()
def l_numbers():
	l = []
	for i in range(7):
		l.append(i)
	return l



single_use = mul(l_numbers)
print(single_use())

print( mul(l_numbers)() )

print(l_numbers())
