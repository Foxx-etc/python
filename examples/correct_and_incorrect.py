

# CORRECT ANSWERS
items = []
def average(num):		
		if not isinstance(num, (int,float)):
			raise ValueError("integer required")		
		items.append(num)
		return round(sum(items) / len(items), 2)

print(average(10))
print(average(12))
print(average(1))
print(average(9))


print()


# INCORRECT ANSWERS
def average(num):
		items = []		
		if not isinstance(num, (int,float)):
			raise ValueError("integer required")		
		items.append(num)
		return round(sum(items) / len(items), 2)

print(average(10))
print(average(12))
print(average(1))
print(average(9))

