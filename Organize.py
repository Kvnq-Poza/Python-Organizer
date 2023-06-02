import os
import shutil

#The path of the directory to be sorted
path = 'C:\\users\\kvnq Poza\\downloads'
#This populates a list with the file names in the directory
list_ = os.listdir(path)

#Traverses every file
for file_ in list_:
	name,ext = os.path.splitext(file_)
	print(name)
	#Stores the extension type
	ext = ext[1:]
	#if it is directory, it forces the next interation
	if ext == '':
		continue
	#if a directory with the name 'ext' exists, it moves the file to that directory

	if os.path.exists(path+'/'+ext):
		shutil.move(path+'/'+file_,path+'/'+ext+'/'+file_)
	#If the director does not exist, it creates a new directory

	else:
		os.makedirs(path+'/'+ext)
		shutil.move(path+'/'+file_,path+'/'+ext+'/'+file_)
