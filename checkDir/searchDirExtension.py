import pathlib as p
import countAll as c
"""
Currently, sorting for Number of occurences remain unsupported
"""

print("This Will Only search for Directory where the file.extension is resided It Never walk in Unpermitted Directory...\n")
	

def countDirs( ext, path = p.Path().cwd() ):
	if p.Path(path).is_dir() == False:
		raise NotADirectoryError
		
	search = p.Path(path).rglob(f'*{ext}')
	tupled_parts = []
	for i in search:
		# 'parts' is a method belongs to pathlib module
		tup = i.parts
		# param: stop in slicing, excludes the value
		tupled_parts.append( tup[1 :-1] )
	
	# Ignore This! It's Only adding the Slashes between Every Part
	slashed = []
	for i in tupled_parts:
		slashed.append('/'.join(i))
	print(c.countAll(slashed))
	
	return ''



while True:
	path = input("Enter Path Name Or Leave It Black : ").strip()
	if path == '':
		path = p.Path().cwd()
		print(f'Your cwd : {p.Path().cwd()}')

	extension = input("\nEnter file extension : ").lower()
	
	print("This may take Time...\n")
	try:
		# No extension found, it raises ValueError which belongs to
		# module carnival.DictWork.show() when dict is empty.
		# Obviously, when no extension appended to list then considered no appending to dict
		print(countDirs(extension , path))
		break
	
	except ValueError:
		print("No extension found!\n")
	except NotADirectoryError:
		print("No Such Directory!\n")
        
