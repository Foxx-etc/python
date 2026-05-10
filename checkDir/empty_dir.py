import os
import pathlib as p


def show_empty(path='.' , absolute=True):
	"""
	Displays which directory is Empty
	
	Only Lists From Current Working Directory
	
	Additional parameter added : absolute, If True
	then displays full path, otherwise only the Directory Name
	"""	
	os.chdir(path)
	
	for i in os.listdir():	
		
		if p.Path(i).is_dir():
			os.chdir(i)
			content = []
			
			for j in os.listdir():
				content.append(j)
				break
			os.chdir("..")
			
			if absolute == True:
				if len(content) == 0:
					print(p.Path(i).absolute())
			
			else:
				if len(content) == 0:
					print(i)
						
		else:
			continue
						
		
if __name__ == '__main__':
	show_empty("/sdcard/Download")
	
	
