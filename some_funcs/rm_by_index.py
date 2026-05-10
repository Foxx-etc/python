
def rm_by_index(di: dict, index: int):
	"""Function related to Dict object
	
	Removes the key from the dict object. Use this 
	function, If you don't remember key, but know
	index
	"""
	
	if num >= len(d):
		raise ValueError

	dict_to_list = list(d)	
	index = dict_to_list.pop(index)
	
	return index
	

