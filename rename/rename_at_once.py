"""
Suppose you want to rename all the files with the same name
and followed by distinct number:
	
park1.png
park2.png
park3.jpeg
park4.png

It adds distinct number automatically start from 1.
All you have to type Is the file name (from above e.g.
'park')
It also takes care of your unnamed file's extension.


You must start by here!
This Program Is only for you If your motive is to rename all
the file In short Time..

When would you use this?
If the content of your unnamed file Is similar to other unnmaed file

Cautions:
It renames all the files at once!
Once renamed, If you add some other unnamed files In between this
the older one may assign different name.
(for e.g. The above four files were already renamed. If I attempt
to add two more unnamed files the previous one may get different name.
This Is Bad.)


Solution:
I made another Program which ensures the previous renamed filename won't
change with newer, which Is a Good Practice.

rename_with_previous.py
"""

import os
import pathlib as p
import holi


num = 1
parent_dir = "/sdcard/changer/"


print(holi.bcyan)
print("This Program Rename All The Unnamed Files At Once")

print(holi.bred)
print("This Program Does Not Reserve The filename That were Already Renamed, In short this is Bad..")

print(holi.bgreen)
print("For A Perfect One Use Another Script, Programmed By Me")

print("It's Named", holi.bmagenta, "rename_at_once_safer.py")
print(holi.resetAll)

print(f'You Are In {parent_dir} Set The Name To All File At Once. All The File Will Have Same Name With Distinct Number') 
print()

rename = input("Enter File Name : ")


for file in os.listdir(parent_dir):
	
	stem = p.Path(file).stem
	suffix = p.Path(file).suffix
	
	old = parent_dir + file
	new_num_file = parent_dir + rename + str(num) + suffix
	
	os.rename(old , new_num_file)
	num += 1
	
