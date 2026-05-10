

import space_aft_syms as s

# TODO: require upgrade
def sentence(a):
	"""
	Capitalizes every letter In a sentence.
	
	This function don't add fullstop mark at very last of the sentence for a reason
	(If Sentence ends with Question/Exclamation mark Then why to add fullstop mark?).
	
	It uses space_after_symb() function to arrange the words In best possible way.
	"""
	
	stripped = [sentence.strip() for sentence in a.split('.')]
	stripped = [sentence for sentence in stripped if not sentence=='']

	b = []	
	for sentence in stripped:
		result = sentence[0].upper()
		b.append(result + sentence[1:])		
	
	# The space_after_sym() func adds spaces after every symbols again
	return s.space_after_symb('.'.join(b))


if __name__ == '__main__':
	a =  "aditya, bs;dkk3 hjj.Ajsj!jdj ei reshim.  dn"
	b = "   my ?name. is aditya,living .in a strret: of! nallasopara; therfore .no?"
	
	print(sentence(a))


