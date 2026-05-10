import re

class OnlyIterable:
	def __set_name__(self, owner, name):
		self.name = name
	
	def __set__(self, obj, value):
		if not isinstance(value, (list,set,tuple)):
			raise TypeError("iterable required")
		
		for i in value:
			if not isinstance(i, str):
				raise TypeError("In Iterable string Iterator is required")
			elif re.match("[a-z]", i):
				pass
			else:
				raise ValueError("In string first charachter alphabet is expected")
			
		obj.__dict__[self.name] = value
	
	def __get__(self, obj, obj_type=None):
		return obj.__dict__[self.name]



class Search:
	value = OnlyIterable() 
	
	_iter = ("hs","e8","ns")	
	def __init__(self, value=_iter):
		self._value = value
	
	@property
	def value(self):
		return self._value
	
	@value.setter
	def value(self, value):
		raise NotImplementedError("cannot assign after initalized")

	def __call__(self, item):
		return True if item in self.value else False


search = Search(("ge","oe","aa"))

print(search("a"))

print(search("ge"))
print(search("oe"))

