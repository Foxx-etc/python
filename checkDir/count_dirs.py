"""Searches for the specified [extension] In Directories
and Displays the number of file.[extension] resided In
Directories


# --------
>>> .py
sdcard/python/functions | 8
sdcard/program          | 12
sdcard/archive          | 18
	
TOTAL : 38
# --------


Currently, sorting for Number of occurences remain unsupported
"""

import pathlib as p
import os

import countAll as c


disclaimer = "This Will Only search for Directory where the \
file.extension is resided It Never walk in Unpermitted Directory...\n"
print(disclaimer)

def countDirs(ext, path):
	if not p.Path(path).is_dir():
		raise NotADirectoryError
		
	search = p.Path(path).rglob(f'*{ext}')
	
	tupled_parts = []
	for i in search:
		# 'parts' is an atrribute belongs to pathlib module
		tup = i.parts
		# :param stop: in slicing, excludes the value
		tupled_parts.append( tup[1 : -1] )
	
	# Ignore This! It's Only adding the Slashes between Every Part
	slashed = []
	for i in tupled_parts:
		slashed.append('/'.join(i))
	print(c.countAll(slashed, False))



while True:
	path = input("Enter Path Name Or Leave It Blank (will considered the directory, where this file is saved) : ").strip()
	if path == '':
		path = p.Path().cwd()
		print(f'Your cwd : {p.Path().cwd()}')

	extension = input("\nEnter file extension : ").lower()
	
	print("\nThis Process may consume Time...\n")
	os.system("clear")
	try:
		# No extension found, it raises ValueError which belongs to
		# module carnival.DictWork.show() when dict is empty.
		# Obviously, when no extension appended to list then considered no appending to dict
		countDirs(extension , path)
		break
	
	except ValueError:
		print("No extension found!\n")
	except NotADirectoryError:
		print("No Such Directory!\n")

