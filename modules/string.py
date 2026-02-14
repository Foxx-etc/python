# Removes The Space In String And Joins The Characters
def drop_space(s) -> str:
	new_str = ""
	for i in s:
		if i==" ":
			continue
		else:
			new_str += i
	return new_str


# Return True If Spaces In String
def is_space(s) -> bool:
	for i in s:
		if i==" ":
			return True
		else:
			continue
	return False


# Counts The Number Of String In Iterables and Return Int value
def count_str(s) -> int:
	number=0
	for i in s:
		if type(i) is str:
			number += 1
		else:
			continue
	return int(number)

# Counts The Nunber Of Integer Values In Iterables and Return Int value
def count_int(n) -> int:
	number=0
	for i in n:
		if type(i) is int:
			number += 1
		else:
			continue
	return int(number)



