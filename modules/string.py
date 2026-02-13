# Removes The Space In String And Joins The Characters
def drop_space(s):
	new_str = ""
	for i in s:
		if i==" ":
			continue
		else:
			new_str += i
	return new_str

# Return True If Spaces In String
def is_space(s):
	for i in s:
		if i==" ":
			return True
		else:
			continue
	return False

# Counts The Number Of String In Iterables and Return Int value
def count_str(s):
	number=0
	for i in s:
		if type(i) is str:
			number += 1
		else:
			continue
	return int(number)

# Counts The Nunber Of Integer Values In Iterables and Return Int value
def count_int(n):
	number=0
	for i in n:
		if type(i) is int:
			number += 1
		else:
			continue
	return int(number)


# Removes The Negative Integer & Ignores the String
def drop_neg_int(l):
	pos = []	
	for i in l:
		if type(i) is str or i < 0:
			continue	
		else:
			pos.append(i)	
	return pos



# Removes The Positive Integer & Ignores the String
def drop_pos_int(l):
	neg = []
	for i in l:
		if type(i) == str or i > 0:
			continue
		else:
			neg.append(i)
	return neg


