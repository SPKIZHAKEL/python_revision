file_path="test_file_demo.txt";

try:
    with open(file_path,"r") as file:
        content=file.read()
        print(content)

except FileNotFoundError:
    print("ayayo")

except PermissionError:
    print("u dont have sufficient permission")


file_path2="output_2.json"
import json

try:
    with open(file_path2,"r") as file:
        content=json.load(file)
        print(content['name'])

except FileNotFoundError:
    print("File doesnt exist")

#now to read csv

import csv

file_path3="ouput_4.csv"
try:
    with open(file_path3,"r") as file:
        content=csv.reader(file) # u need to iterate over rows else ull only get memory address
        for row in content:
            print(row)
            print(row[0])

except FileNotFoundError:
    print("File doesnt exist")