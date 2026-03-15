import holi , os , pathlib as p

print(holi.lcyan)
print("This Program Is Designed If You Moved Some Unnamed files Under Belonging files And Want To Rename By Caring The Number") 
print(holi.lred)
print("Precaution : Enter The Existing filename You Want To Rename Otherwise This Leads To Replaces The filenames To One-Another!")
print()
print("If You Mistakenly Enter Wrong filename To Rename, I Am Not Responsible! Although, It Ask Again To You To Verify")
print(holi.lgreen)
print("The filename must be in lowercase else it may replace the existing filenames")
print(holi.reset)

# making this user friendly
path = input("Enter Path To Directory : ")
if not path.startswith('/'):
	path = '/' + path
	if not path.endswith('/'):
		path = path + '/'
		if not p.Path(path).is_dir():
			print("Entered The Wrong Path! Try Again..")
			pass

print()

# loading all the files belongs to specified path
all_files = []
for file in os.listdir(path):
	all_files.append(file)


old_name = input("Enter Old Filename : ").lower()
old_name_again = input("Enter Old Filename Again : ").lower()
if old_name != old_name_again:
	print()
	print("Try Again..")
	pass
		
old_name_li = []
else_name_li = []


# existing filename shall not overwrite so i decide to append them in separate list : old_name_li
# if distinct filename appears shall move to : else_name_li
for file in all_files:
	if file.startswith(old_name):
		old_name_li.append(old_name)
	else:
		else_name_li.append(file)

# my program aims to rename the distinct filenames. Underneath code is responsible to rename
num = 1
for file in else_name_li:
	while True:
		suffix = p.Path(file).suffix
		new_name = path + old_name + str(num) + suffix
		
		try:
			if p.Path(new_name).exists():
				raise FileExistsError(f'{new_name} already exists')
			
			os.rename(path + file, new_name)
			break
		except FileExistsError:
			num += 1
		
