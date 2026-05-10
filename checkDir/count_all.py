import carnival as crn

# whenever param: sort is False param: rev(reverse) override as False either
def countAll(iterable , sort=True , rev=False):	
	if not all(iterable) :
		raise TypeError("must be an iterable object")
		
	elif type(iterable) is str:
			raise TypeError("string object cannot be interpreted as iterable")
		
	elif type(iterable) is set:
		raise TypeError("<class 'set'> always has single unqiue element")

	iterable = list(iterable)
	
	# stores unique element same has set(), but making it ordered in future
	list_singleElement = []
	# creating set object to remain elements unordered everytime it Runs, will be using when param: sort in function is False
	set_singleElement = set( iterable.copy() )
	
	# Total count
	total = 0
	for i in iterable:
		total += 1
		
	# appending only unqiue elements in list_singleElement
	for i in iterable:
		if i in list_singleElement:
			continue
		else:
			list_singleElement.append(i)
	
	
	if sort == True:
		list_singleElement = sorted(list_singleElement , reverse = rev)
		d = {}
		for i in list_singleElement:
			d[i] = iterable.count(i)
	
	# when param: sort is False then no use of reverse to be True
	else:
		d = {}
		for i in set_singleElement:
			d[i] = iterable.count(i)
	
					
	print(crn.DictWork.show(d),'\n\n')
	return f'TOTAL : {total}'	 					
		

if __name__ == '__main__':
	a = ["aa","ab","ba","bb","ca","cb","da","db","aa","ab"]
	b = 6,5,4,6,9,4,4
	print(countAll(a))
    
