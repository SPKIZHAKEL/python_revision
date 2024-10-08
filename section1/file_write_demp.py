# python writing files (.txt, .json, .csv)

txt_data="I like pizza"

file_path="output.txt"

try:

    with open(file=file_path,mode="x") as file: # u can also use "x" if the file doesnt exist or "a" to append
        file.write(txt_data) #the open fucntion retruns a file object to us we give it a name as file
        print(f"txt file '{file_path}' was created")

except FileExistsError:
    print("That file already exists")


employees=['jake','take','bob','beth']

file_path_1="output_1.txt"
try:
    with open(file_path_1,"w") as file:
        for emp in employees:
            file.write(emp + "\n")
        print(f"Output 1 txt exists, '{file_path_1}'")

except FileExistsError:
    print("File already exists")


# in json format u need take dumps first
import json
file_path_3="output_2.json"
employee={
"name":"Sponegbob",
"age":30,
"job":"Cook",
}


try:
    with open(file_path_3,"w") as file:
        json.dump(employee,file,indent=4) # we cant use write for json object so we use dump
        #indent is spaces
        print("Wrote json content to the file")

except FileExistsError:
    print("File already exists")


#similarly to write to a csv

import csv

employees3=[["Name","Age","Job"],
            ["Spongebob","30","Cook"],
            ["patrcik","37","engineer"],
            ["squid","38","lol"]]

file_path_4="ouput_4.csv"

try:
    with open(file_path_4,"w") as file:
        writer=csv.writer(file)
        for row in employees3:
            writer.writerow(row)
        print(f"csv file '{file_path_4}' was created")
except FileExistsError:
    print("That file already exists")