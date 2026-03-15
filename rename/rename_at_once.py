import holi , os , pathlib as p

num = 1
parent_dir = "/sdcard/just/"

print(holi.bcyan)
print("This Program Rename All The Unnamed Files At Once")
print(holi.bred)
print("This Program Does Not Reserve The filename That were Already Renamed, In Short This Bad..")
print(holi.bgreen)
print("For A Perfect One Use Another Script Programmed By Me")
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
	


