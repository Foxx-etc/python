"""
Must Read the document of rename_at_once.py

Suppose You have Identical renamed files (exculding extension):

waterpark1.jpg
waterpark2.png
waterpark3.png
waterpark4.jpeg

|------------------------|
|Screenshot_23-11-....jpg|
|Screenshot_23-19-....jpg|
|------------------------|

Now you add 2 more unnamed files In between them to rename same as
'waterpark', without changing the name of already renamed one,
This Program Is for you!

Don't care of extension It preserves the same as it was before.

This Program Is safe.
It asks for path, where the files are resided to be renamed,
and Filename of the already renamed once, that is, 'waterpark' and
not 'Screenshot_23-11-....jpg'

It will change the name of 'Screenshot_23-11-....jpg' to 'waterpark5.jpg'


Suggestion:
I Hardly suggest you to create a separate directory
In which you shall operate and same directory path must be 
specified here.
(for e.g. /sdcard/changer/ )

Cautions:
If entered wrong path, It's too late!
"""


import os
import pathlib as p
import holi

print(holi.lcyan)
print("This Program Is Designed If You Moved Some Unnamed files Under Belonging files And Want To Rename By Caring The Number") 

print(holi.bred)
print("Precaution : Enter The Existing filename You Want To Rename Otherwise This Leads To Replaces The filenames To One-Another!")
print()
print("If You Mistakenly Enter Wrong filename To Rename, I Am Not Responsible! Although, It Ask Again To You To Verify")

print(holi.resetAll)

print(holi.lgreen)
print("The filename must be in lowercase else it may replace the existing filenames")

print(holi.resetAll)

# ---------------------------------

# making this user friendly
path = input("Enter Path To Directory : ").strip()
if not path.startswith('/'):
	path = '/' + path
	
	if not path.endswith('/'):
		path = path + '/'
		
		if not p.Path(path).is_dir():
			raise SystemExit("You Entered the wrong Path!")
print()

# loading all the files belongs to specified path
all_files = []
for file in os.listdir(path):
	all_files.append(file)

# Ensure here, I am only asking for filename(stem) not extension(suffix)
old_name = input("Enter Old Filename : ").lower()
old_name_again = input("Enter Old Filename Again : ").lower()

if old_name != old_name_again:
	print()
	print("Try Again later..")
	pass

# ----------------------------

#already renamed files will be coming here..
#file name but without suffix(extension)		
old_name_li = []

#newly added unnamed files will be coming here
#and will be renamed!
else_name_li = []   


# Existing filename shall not overwrite so i decided to append them in separate list without suffix(extension) : old_name_li
# If distinct filename appears they shall move to separate list with suffix(extension): else_name_li
for file in all_files:
	if file.startswith(old_name):
		stem = p.Path(file).stem
		old_name_li.append(stem)
	else:
		else_name_li.append(file)


# ------------------------------------

# My program aims to rename the newly added files. Underneath code is responsible to rename
num = 1
for file in else_name_li:
	while True:
		suffix = p.Path(file).suffix
		new_name = f'{path}{old_name}{num}{suffix}'
		
		try:
			#Verification
			new_name_without_suf = f'{path}{old_name}{num}'
		
			for tempfile in old_name_li:
				tempname = f'{path}{tempfile}'
				
				if new_name_without_suf == tempname:
					raise FileExistsError

		except FileExistsError:
			num += 1
			
		else:
			os.rename(path+file, new_name)
			num += 1
			break
			

print("Done!")

