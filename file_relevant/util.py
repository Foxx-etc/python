
import os.path as op
import hashlib as hl
from collections import namedtuple

# ===Below Utility functions for same_file_eliminate.py===

def image_hash(iterable: list[str]) -> list[dict[str:str]]:
	"""Only single hash method will be used file_digest() -- shake_256(200)
	
	Returns [{file_path:hashed}, ...]
	"""
	
	if not isinstance(iterable, list|tuple):
		raise TypeError("iterable required")
	
	for file_name in iterable:
		if not (op.exists(file_name) and op.isfile(file_name)):
			raise FileNotFoundError(file_name)
	
	hashed_file: list[str] = []
	
	for file_name in iterable:
		with open(file_name, "rb") as f:
			hashing = hl.file_digest(f, "shake_256")
			hashed = hashing.hexdigest(200)
		
			hashed_file.append({file_name : hashed})
	
	return hashed_file


def rm_same(li_di: list[dict]) -> dict:
	"""Removes key:value pair If value repeats In other key:value pair
	
	Returns namedtuple with two new fields as dictionary object:
		(distinct, same)
	
	>>> rm_same( [{
	"a": 1,
	"b": 2,
	"c": 1,
	"d": 1,
	"e": 3,
	"f": 4,
	}] )
	...
	file_with_hash(
	distinct={"a": 1, "b": 2, "e": 3, "f": 4},
	same={"c": 1, "d": 1}
	)
	
	"""
	same = {}
	distinct = {}
		
	for di in li_di:
		for file,hash in di.items():
			
			if hash in distinct.values():
				same[file] = hash
			
			else:
				distinct[file] = hash
	
	file_with_hash = namedtuple("file_with_hash", "distinct, same")
	
	return file_with_hash(distinct, same)


if __name__ == '__main__':
	li_di = [{
	"a": 1,
	"b": 2,
	"c": 1,
	"d": 6,
	"e": 1,
	"f": 2,
	"g": 2
	}]
	
	for i in rm_same(li_di).same:
		print(i)
	
	
	
