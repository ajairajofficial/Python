import os
###########################################################################################
# Key Concepts Demonstrated:
# ** Directory operation
# os.getcwd() - Get current working directory
# os.listdir() - List directory contents
# os.chdir() - Change directory
# ** Path manipulation
# os.path.join() - Create proper file paths
# Path manipulation using both os.path and pathlib
# ** Path verification
# os.path.exists() - Check path existence
# os.path.isfile() - Verify if path is a file

##########################################################################################
print(os.getcwd()) # get the current working directory c:/Users/ajair/Desktop/Python/
print(os.listdir()) # list the files in the current working directory
os.chdir('Python') # change the current working directory c:/Users/ajair/Desktop/Python/Python/
print(os.getcwd()) # change the current working directory
os.chdir('core_concepts') # add the path to the current working directory 
print(os.getcwd()) # get the current working directory c:/Users/ajair/Desktop/Python/Python/core_concepts
list_filename =os.listdir() # Create a list of files in the core_concepts folder
os.chdir('..') # change the current working directory to the parent directory c:/Users/ajair/Desktop/Python/Python
print(os.getcwd()) # get the current working directory c:/Users/ajair/Desktop/Python/Python

print(list_filename) # list the file names in the core_concepts folder
for x,y in enumerate(list_filename): # enumerate the list of files in the core_concepts folder
    print(x,y)

new_path = os.path.join(os.getcwd(),'core_concepts') # join the current working directory with the core_concepts folder
print(new_path)
new_path_list = [os.path.join(new_path, x) for x in list_filename] #using list comprehension to create a list of paths to the files in the core_concepts folder
full_paths = list(map(lambda x: os.path.join(os.getcwd(), x), list_filename)) # same thing using map function

for x,y in enumerate(new_path_list): # enumerate the list of paths to the files in the core_concepts folder
    print('new_path',x,y) 

for x,y in enumerate(full_paths): # enumerate the list of paths to the files in the core_concepts folder
    print('full_path -',x,y)

# checking the path exist 
print(os.getcwd())
print(os.path.exists('core_concepts')) # checking there is a folder/file exist
print(os.path.exists('core_concepts/7os_functions.py')) # checking osfunctions.py exist
print(os.path.isfile('core_concepts/7os_functions.py')) # works only for files not folder
# another approach for checking the path exist
#########################################################
from pathlib import Path
file_path = Path('core_concepts')
exists = file_path.exists()
print("Test",exists)
########################################################
print(os.getcwd())
# Practical example with full path with error handling

full_path = os.path.join(os.getcwd(), "core_concepts/osfunctions.py")
if os.path.exists(full_path):
    print(f"Found file at: {full_path}")
else:
    print("File not found")


####################################################################3
# playing in desktop
os.chdir(r'C:\Users\ajair\Desktop') # using raw string to avoid escape characters
# In python \n menas newline and \t means tab and \means literal backlash
# using raw string to avoid escape characters
os.chdir('C:\\users\\ajair\\Desktop') # without raw string
print(os.getcwd())
# each time you run this code it will create during the first run and remove the folder the second run 
if os.path.exists('python_test_folder'):
    print("folder exist and removing now")
    print("removing the folder. the function returns  ", os.rmdir('python_test_folder')) # remove the folder
else:
    print("folder does not exist and making a new folder now")
    print("making new folder. the function returns ", os.mkdir('python_test_folder')) # making a new folder
# create a folder

print("is new created folder exist? ",os.path.exists("python_test_folder")) # check if the folder exists

#  Directory Walking
for root, dirs, files in os.walk(r'C:\Users\ajair\Desktop'):
   print(f"Current Directory: {root}")
   print(f"Subdirectories: {dirs}")
   print(f"Files: {files}")
   break  # Added break to show only first level otherwise it will print all the files in the directory
#
# ################################################################
#  2 ways of searching files
import os
import string
from time import time

def find_file_anywhere(filename):
    drives = [f"{d}:\\" for d in string.ascii_uppercase if os.path.exists(f"{d}:")]
    start_time = time()
    print(f"Starting search for {filename}")
    
    for drive in drives:
        print(f"Searching in drive: {drive}")
        try:
            for root, dirs, files in os.walk(drive):
                print(f"Checking: {root}")  # Shows current folder being searched
                if filename in files:
                    end_time = time()
                    print(f"\nFound in {end_time - start_time:.2f} seconds")
                    return os.path.join(root, filename)
        except PermissionError:
            print(f"Skipping some restricted folders in {drive}")
            continue
    
    end_time = time()
    print(f"\nCompleted in {end_time - start_time:.2f} seconds")
    return "File not found"

# Usage
search_file = '1basics_print.py'
print(f"Searching for: {search_file}")
result = find_file_anywhere(search_file)
print(f"Result: {result}")

'''

# using glob module - great for pattern matching.
from glob import glob
import os

# Search for all .txt files
files_1 = glob('C:\\**\\*.txt', recursive=True)

# Search for specific filename pattern
files_2 = glob('C:\\**\\*config*.ini', recursive=True)

print("search using glob -all txt ",files_1)
print("search using glob - specific filename pattern -",files_2) '''
