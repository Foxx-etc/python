
import time

# ===Utility functions===
def rmbyindex(d, num):
	if num >= len(d):
		raise ValueError

	dict_to_list = list(d)	
	index = dict_to_list.pop(num)
	
	return index


# ==========
# :param max: maximum length in cache memory 
def dec_args_here(max, min):
	
	def func_name_here(fact):		
		cached = {}
		
		def func_args_here_and_func_dec_start_here(num):			
			if num not in cached:
				cached[num] = fact(num)
			if len(cached) > max:
				cached.pop(r.rmbyindex(cached, 0))
									
			return cached[num]			
		return func_args_here_and_func_dec_start_here
	return func_name_here


@dec_args_here(4, 2)
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

