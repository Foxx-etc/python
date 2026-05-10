import time

# -----------------
def rmbyindex(d, num):
	if num >= len(d):
		raise ValueError

	dict_to_list = list(d)	
	index = dict_to_list.pop(num)

	return index
# -----------------




# --------------------
# Decorator with parameters
# --------------------

class cache:
	# __init__ = dec_args_here
	def __init__(self, max):
		self.max = max
		self.cached = {}
	
	# __call__ = func_name_here
	def __call__(self, func):
		
		def func_args_here_and_dec_starts_here(num):
			if num not in self.cached:
				self.cached[num] = func(num)
			
			if len(self.cached) > self.max:
				self.cached.pop(rmbyindex(self.cached, 0))
			
			return self.cached[num]
		return func_args_here_and_dec_starts_here

			
@cache(4)
def fact(num):
	result = 1
	for i in range(1, num+1):
		result *= i
	time.sleep(1)	
	return result


print(fact(5))
print(fact(5))

print(fact(6))

print(fact(7))
print(fact(7))

print(fact(8))

print(fact(9))

print(fact(10))

print(fact(5))

print(fact(8))

print(fact(9))



# ----------------------
# Decorator without parameters
# ----------------------

class cache:
	# __init__ = func_name_here
	def __init__(self, func):
		self.func = func
		self.cached = {}
	
	# __call__ = func_args_here_and_dec_starts_here
	def __call__(self, num):
		if num not in self.cached:
			self.cached[num] = self.func(num)
			
		if len(self.cached) > 4:
			self.cached.pop(rmbyindex(self.cached, 0))
			
		return self.cached[num]
			

@cache
def fact(num):
	result = 1
	for i in range(1, num+1):
		result *= i
	time.sleep(1)	
	return result


print(fact(5))
print(fact(5))

print(fact(6))

print(fact(7))
print(fact(7))

print(fact(8))

print(fact(9))

print(fact(10))

print(fact(5))

print(fact(8))

print(fact(9))

