
"""
Better approach to use property method.

We have to ensure that the value while assiging in the __init__()
method must be verified before, so, we use propertymethod to make
it easier..

We required to be precise while naming the attribute in __init__()
method as well as to the property method:
	1. Use same method name to the property method as used in 
	   __init__() method to name instance attribute
	2. In the setter of property method, use different attribute
	   to set the value (if used the same name may get RecurrsionError)
	   and use the same attribute name to get the value from getter
	   of property method.

What Is the purpose of this?
All we have to verify each attribute during Initalizing into __init__()
method at beggining as well as whenever the user attempts to change the
instance attribute value.		
"""



class A:
	def __init__(self, a, b):
		self.a1 = a 
		self.b1 = b
	
	@property
	def a1(self):
		return self._a
	
	@a1.setter
	def a1(self, value):
		print("seta")
		if not isinstance(value, int):
			raise ValueError
		self._a = value


	@property
	def b1(self):
		return self._b
	
	@b1.setter
	def b1(self, value):
		print("setb")
		if not isinstance(value, int):
			raise ValueError
		self._b = value

obj = A(3,8)
print(obj.b1)
