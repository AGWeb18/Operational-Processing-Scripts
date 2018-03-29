from os import listdir

files_in_directory = listdir(r"C:\Users\<username>\Desktop\FILE_PATH_GOES_HERE")

for item in files_in_directory:
    print(item)
