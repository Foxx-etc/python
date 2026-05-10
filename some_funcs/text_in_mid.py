import os

def mid(word, ldesign = " ", rdesign = " "):
	"""
	The Text Comes In Middle Of The Screen, Changes In Screen Size Will Worsen The View
	It imports a func called os.get_terminal_size()
	
	param: word is the text to come in middle of the screen
	param: ldesign defaults to single whitespace, Is the design on left side of the word
	param: rdesign defaults to single whitespace, Is the design on right side of the word
	"""
	
	if not isinstance(word, str):
		raise TypeError("applies for <class str>")	
		
	if len(ldesign) % 2 != 0:
		if len(ldesign) == 1:
			pass
		else:
			raise ValueError("length of parameter ldesign must be even")
		
	if len(rdesign) % 2 != 0:
		if len(rdesign) == 1:
			pass
		else:
			raise ValueError("length of parameter rdesign must be even")

				
	column = os.get_terminal_size().columns	
	len_word = len(word)	
	remaining_space_around = column - len_word
	
	left = int(remaining_space_around / 2)
	right = int(remaining_space_around / 2)

	if (left + right + len_word) != column:
		# At first, I thought, using math.ceil() is same as +1
		# but, outer 'if' condition, The variable 'right' is already having int(), which will not imply math.ceil() 
		right += 1
	
	len_ldes = int(left / len(ldesign))
	len_rdes = int(right / len(rdesign))
			
	return (ldesign * len_ldes) + word + (rdesign * len_rdes)



if __name__ == '__main__':
	print(mid("ADYA", "- "," -"))
  
