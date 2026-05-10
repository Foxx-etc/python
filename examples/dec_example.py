

def dec(func):
	def wrapper(num):
		for i in func(num):
			yield i.upper()
	return wrapper


@dec
def loop(num):
	for i in range(num):
		yield "Aditya"


for i in loop(10):
	print(i)

