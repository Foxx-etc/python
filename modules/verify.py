# True If all elements in container are Integers False otherwise
# If floatAsInt is True, then floats are treated as Integers
def isall_int(c, floatAsInt = True):
	for i in c:
		if type(i) is int:
			continue
		
		elif type(i) is float:
			if floatAsInt == True:
				continue
			else:
				return False
		
		else:
			return False
	return True




# True If all elements in List are string False otherwise
def isall_str(s):
	for i in s:
		if type(i) is str:
			continue
		else:
			return False
	return True 



def isall_bool(b):
	for i in b:
		if type(i) is bool:
			continue
		else:
			return False
	return True



# True If all elements in container are Float False otherwise
# If intAsFloat is True, then integers are treated as floats
def isall_float(c, intAsFloat = True):
	for i in c:
		if type(i) is float:
			continue
		
		elif type(i) is int:
			if intAsFloat == True:
				continue
			else:
				return False
			
		else:
			return False
	return True


# Parameter must be a string otherwise a TypeError is raised
# Removes Everything except alphabets
# If parameter preserve_space is True, then it won't removes spaces
def stay_str(s , preserve_space = True):
	if type(s) is not str:
		raise TypeError("Argument must be a string")
	
	ss = ""	
	for i in s:
		if i.isalpha():
			ss += i
			
		elif i == " ":
			if preserve_space == True:
				ss += i
			else:
				continue
			
		else:
			continue	
	return ss




# Parameter must be a string otherwise a TypeError is raised
# Removes Everything except Numbers
# If parameter preserve_space is True, then it won't removes spaces
def stay_int(n, preserve_space = True):
	if type(n) is not str:
		raise TypeError("Argument must be a string")
	
	si = ""	
	for i in n:
		if i.isnumeric():
			si += i
			
		elif i == " ":
			if preserve_space == True:
				si += i
			else:
				continue
			
		else:
			continue	
	return si	



# Removes Negative Integers
def drop_neg_int(c) -> list:
	if type(c) is str:
		raise TypeError("parameter must not be a string")
	
	pos = []
	for i in c:
		if i < 0:
			continue
		else:
			pos.append(i)	
	return pos


# Removes Positive Integers
def drop_pos_int(c) -> list:
	if type(c) is str:
		raise TypeError("parameter must not be a string")
	
	neg = []
	for i in c:
		if i > 0:
			continue
		else:
			neg.append(i)		
	return neg



