import os

file_path="test_file_demo.txt" # since its in the same folder specifying relative file path

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists'")
    if os.path.isfile(file_path): #checking if the file is actually a file˜
        print("This is a file")
else:
    print("that location doesnt exist")

outer_file_path="/Users/skizhake/Desktop/Python-revision/test_file_outside_directory.txt" #diff directory
#if u hav a path with '\' then use either '/' or u put a double '\\'
if os.path.exists(outer_file_path):
    print(f"The location '{outer_file_path}' exits")
else:
    print("The location doesnt exist")