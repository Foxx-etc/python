"""This Program eliminates the same files (copied files)

It Is based on filesize and hashing.

To make It work all the files must be under a single directory.
It takes the filesize(regardless filename.ext), hash the content
using file_digest() -- shake_256(200) and eliminate all the
same(copy) files by leaving single file.

As the Contents are read in binary mode

It may work for any file such as jpg, mp3, m4a, png, mp4
"""

__author__ = "Reshim Aditya"
__version__ = 0.1

import time
import os.path as op
import hashlib as hl
import os
from collections import defaultdict

# util.py has 2 functions
import util

MIN_SLEEP = 0.4
AVG_SLEEP = 1
MAX_SLEEP = 2


print("It is required that to prevent unexpected removal of \
files all the files must be under a single folder\n")

# ===Directory Path Validation before commencing===
time.sleep(MIN_SLEEP)
folder_path = input("Enter Folder path : ")

if not folder_path.startswith("/"):
	folder_path = "/" + folder_path
		
if not (op.exists(folder_path) and op.isdir(folder_path)):
	time.sleep(MIN_SLEEP)
	exit(f"\nInvalid folder name : {folder_path}")


# ===Optional===
time.sleep(MIN_SLEEP)
print("\nAre you willing to Inspect Deleting Files?")
time.sleep(AVG_SLEEP)
user_choice = input("Enter y/n : ").upper()

if user_choice not in ('Y','N'):
	user_choice = 'N'


# ================
file_size_and_name: list[list[int, str]] = []

for file in os.listdir(folder_path):
	
	size = op.getsize(op.join(folder_path, file))
	filename = op.join(folder_path, file)
	
	nested_li: list[int, str] = [size, filename]
	
	file_size_and_name.append(nested_li)


# =============
# defaultdict will produce
# key=size, value=[str, ...]
# If len(value) > 1 then I catched the same sized file(in key)
# with different filename(in value)
d = defaultdict(list)

for size,name in file_size_and_name:
	d[size].append(name)


same_size = {}

for size,name in d.items():
	if len(name) > 1:
		same_size[size] = name

#print(same_size)



# ==============
deleted_files: list[str] = []
		
for names_list in same_size.values():
	li_dict: list[dict[str: str]] = util.image_hash(names_list)
	
	filepath_and_hash = util.rm_same(li_dict)
	
	for filepath in filepath_and_hash.same.keys():
		os.remove(filepath)		
		deleted_files.append(filepath)		

if deleted_files:
	time.sleep(AVG_SLEEP)
	print(f"\n{len(deleted_files)} FILES DELETED!")
else:
	time.sleep(AVG_SLEEP)
	exit("\nNo Same File Detected; No Files Deleted..")	



# ===Displaying deleted files based on user_choice===
if (user_choice == 'Y'):
	
	time.sleep(MAX_SLEEP)
	print("\nDELETED FILES WITH PATH : \n")
	time.sleep(MAX_SLEEP)
	
	for file in deleted_files:
		print(file.rjust(len(file) + 4) )
	
	time.sleep(AVG_SLEEP)
	print("\nDONE")
		

