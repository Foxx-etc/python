import pathlib as p
from emptyDir import show_empty
from os import system
from time import sleep


def allEmptyDir( full_path=True, sort=True, rev=False):
	"""
	Sorting Is Done Alphabatically From CAPITAL Letters to small Letters\n") 
	
	But, The cwd(current working directory) Don't Obey the Rule
	It First, Displays From cwd So No Sorting for thier
	
	param: path, is where it begins
	param: full_path will display absolute path
	param: sort, displays Ascending to Descending
	param: rev(reverse) displays From Descending to Ascending
	"""
	path = input("Enter The Path Name : ")
	all = p.Path(path).rglob("*")
	
	if sort == True:		
		print("For Sorting.. It May Consume Time!")
		print("Remeber! Sorting Is Done Alphabatically From CAPITAL LETTERS to small letters\n") 
		print("wait...\n")
		
		sorting = []
		sorting.append(path)
		for i in all:
			if p.Path(i).is_dir():
				sorting.append( str(i) )
				
		sorting = sorted(sorting, reverse = rev)
				
		print("Done!")		
		sleep(2)
		system("clear")
		
		for order in sorting:
			try:
				show_empty(order, full_path)							
			except PermissionError:
				os.chdir('..')		
	
	
	else:
		show_empty(path, full_path)
		for i in all:
			if p.Path(i).is_dir():
				try:
					show_empty(i, full_path)							
				except PermissionError:
					os.chdir('..')

if __name__ == '__main__':
	allEmptyDir()

