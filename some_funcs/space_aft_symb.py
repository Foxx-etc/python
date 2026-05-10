

def space_aft_symb(a, symbols=':;!?,.'):
	"""Adds single whitespace after every symbols also removes if more than one whitespace found after every symbols.
	
	:param symbols: can be iterable. Default is ':;!?,.'
	
	It also remove the whitespace before joining the symbol:
	
	>>> space_after_symb("Who is it ? No one")
	>>> "Who is it? No one"
		
	>>> space_after_symb("Who is it ?No one")
	>>> "Who is it? No one"
		
		
	"""	
	a = a.strip()
	
	b = ''
	for letter in a:		
		# Adding whitespace after every symbols in :if condition:
		if letter in symbols:
			b += letter
			b += ' '
		else:
			b += letter
	
	# The purpose of creating this function is to remove trailing whitespace charachter 
	def rm_space(a):
		"""It removes only last string charachter"""
		return a[0:-1]

	# Suppose after every whitespace we added explicitly there may be more than one whitespace
	# I have to remove if there are more than once,
	c = ''
	for letter in b:		
		# :if cond 2: It checks if whitespace is already added it won't add more
		if (letter==' ') and (c[-1] == ' '): 
			continue
			
		elif (letter in symbols) and (c[-1] == ' '):
			# Removing space before adding the symbol
			c = rm_space(c)
			c += letter
		
		else:
			c += letter
	
	return c


if __name__ == '__main__':
	a =  "    aditya !bs;dkk3 hjj).Ajsj jdj ?ei reshim. dn"
	print(space_after_symb(a, ':;!?,.'))
	
	print()
	
	b =  " Today I turning 20 .When   I was young boy, I was \
playing in garden ,fall asleep. I woke Up ? i Walk after a \
Walking duck;Relaized Something Unnatural ,   Goodbye  !"
	print(space_after_symb(b, ':;!?,.'))
	
	

