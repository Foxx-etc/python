		
import os
import time
from pathlib import Path

# ===Utility function===
def replace_in_list(li: list, old: str, new: str):
	if not all( [isinstance(old, str), isinstance(new, str)] ):
		raise ValueError(f"required string")
	
	#if len(new) == 0:
#		new = ' '
#		
#	elif len(new) != 1:		
#		raise ValueError("length of 'new' argument must be exactly one")
	
	new_li = []
	
	for element in li:
		if element == old:
			new_li.append(new)
			
		else:
			new_li.append(element)
	
	return new_li


def customize_list(li, meth, new_name):
	new_li = []
	
	for row in li:
		each_row = []
		
		for data in row:
			if data == new_name:
				each_row.append(data)
			else:
				each_row.append(getattr(data, meth)())
		
		new_li.append(each_row)
	
	return new_li


# ===File Validation===
filename = input("Enter Filename : ")

if not Path(filename).exists():
	print("No Such File")
	quit()


# =========
with open(filename) as f:
	temp = f.readlines()
	read = []
	
	# removing suffix '\n'
	for row in temp:
		read.append(row[:-1])


# ====Enhancing to make aftermath easier=====
new_read = []

for row in read:
	if row.startswith(' '):
		continue
	new_read.append(row)
	
#print(new_read)
#print()


# =============
num_headings = len(read[0].split(' ')) #0-3


empty: str = input("Empty Data fill with : ")
keyword: str = input("What Represent Empty Data : ")

# =========
max_len: list[list[int]] = []

# read is a list
# row is still a string
for row in new_read:
	particular_row = []
	
	for data in row.split(' '):
		# data is not a particular string among a row
		if len(data) == 0:
			continue
			
		# data == 'None' will become space 
		if data == keyword:
			particular_row.append(0)
		
		else:
			particular_row.append( len(data) )
		
	max_len.append(particular_row)



# =========
if [] in max_len:
	max_len.remove([])

#print(max_len)
#print()

max_len_in_col: list[int] = []

for num in range(num_headings):
	each_row = []
	
	for row in max_len:
		each_row.append( row[num] )
	
	max_len_in_col.append( max(each_row) )
	
#print(max_len_in_col)
#print()



# =========
rows_of_names: list[str] = []

for row in new_read:
	particular_row = row.split()
	replace = replace_in_list(particular_row, keyword, empty)
	
	rows_of_names.append(replace)

rows_of_names = customize_list(rows_of_names, 'title', empty)


# ==========
user_choice = input("Left or Right : ").upper().strip()
os.system("clear")
time.sleep(0.3)

if not (user_choice == 'RIGHT' or user_choice == "LEFT"):
	print("Invalid Answer! Try Again..")
	quit()


# =========
for (enumber,row) in enumerate(rows_of_names):
	for (data,num) in zip(row, max_len_in_col): #(0,(0,1))
	
		# Adding a single empty row just below the heading
		if (user_choice == "LEFT"):
			if (enumber == 0) and (row[-1] == data):
				print(data)
			else:
				print(data.ljust(num+1), end=' ')
		
		# Adding a single empty row just below the heading
		elif user_choice == "RIGHT":
			if (enumber == 0) and (row[-1] == data):
				print(data.rjust(num))
			else:
				print(data.rjust(num+1), end=' ')
			
	print()



