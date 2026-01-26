#True If all elements in List are Integer
def isall_int(l):
	check= str()
	for i in l:
		if type(i) is int:
			continue
		else:
			check= "yes"
			break
			
	return False if check =="yes" else True 



#True If all elements in List are string
def isall_str(s):
	check= str()
	for i in s:
		if type(i) is str:
			continue
		else:
			check= "yes"
			break
			
	return False if check =="yes" else True 




#True If all elements in List are bool
def isall_bool(b):
	check= str()
	for i in b:
		if type(i) is bool:
			continue
		else:
			check= "yes"
			break
			
	return False if check =="yes" else True 


#True If all elements in List are float
def isall_float(f):
	check= str()
	for i in f:
		if type(i) is float:
			continue
		else:
			check= "yes"
			break
			
	return False if check =="yes" else True 

