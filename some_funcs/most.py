from typing import Any
import carnival as crn


def most(iterable):
	"""Returns an element from Iterable which appears
	the most"""
	li: list[Any] = []
	for i in iterable:
		li.append(i)
		
	single: set = set(iterable)
	
	di: dict = {}
	for i in single:
		di[i] = li.count(i)
	
	check = sorted(di.values(), reverse=True)
		
	if check[0] == check[1]:
		raise ValueError("Same Elements Appeared")
		
	return crn.DictWork(di).getkey(check[0])

if __name__ == '__main__':
	print(most([3,3,7,7,7,7,7,7,7,99,99,3,56,7,5,47,99,99]))

