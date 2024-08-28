file = open('example.txt', 'r')  # Opens the file in read mode
----------------------------------------------------
READING
with open('example.txt', 'r') as file:
  print(file.read())
----------------------------------------------------
with open('reddy.txt','r'):
  print(file.read())
--*-*-*-*-*-*-*-*-*--*-*-*-*-*-*---**-*-*-*-***---*-*
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())  # strip() removes any extra newline characters
-----------------------------------------------------
with open('example.txt', 'r') as file:
    content = file.read(10)  # Reads the first 10 characters
    print(content)
-----------------------------------------------------
with open('example.txt', 'r') as file:
    lines = file.readlines()  # Returns a list of all lines in the file
    print(lines)
---------------------------------------------------
WRITING
with open('example.txt', 'w') as file:
    file.write("Hello, World!\n")


---------------------------------------------------
with open('example.txt', 'a') as file:
    file.write("Appending this text.\n")
---------------------------------------------------
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open('example.txt', 'w') as file:
    file.writelines(lines)
---------------------------------------------------
CLOSING
file = open('example.txt', 'r')
# Perform file operations
file.close()  # Closes the file
---------------------------------------------------
When using the with statement, the file is automatically closed after the block finishes executing:
with open('example.txt', 'r') as file:
    content = file.read()
# File is automatically closed here
---------------------------------------------------
File Handling with Binary Files:

with open('example.jpg', 'rb') as file:  # Reading a binary file
    data = file.read()
---------------------------------------------------
Checking if a File Exists:

from pathlib import Path
file_path = Path('example.txt')
if file_path.exists():
    with open(file_path, 'r') as file:
        content = file.read()
else:
    print("File does not exist!")
************************************************

from pathlib import path
cc=path("manju.txt")
if cc.exists():
  with open(cc,'r') as file :
    pp=file.read()

else:
  print("doesnot exists")

**************************************************
try:
    with open('input.txt', 'r') as infile:
        content = infile.read()

    with open('output.txt', 'w') as outfile:
        outfile.write(content)
except FileNotFoundError:
    print("One of the files does not exist.")
except IOError as e:
    print(f"An I/O error occurred: {e}")
*-*-*-*-*-*-*-*-*-*-*-**-*-*-*-*-*-*-***-****--**-********/**/*/*/-*-
import csv

# Reading from a CSV file
with open('data.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)
*-*-***-*-**-**-*-*****/*-*/-***
import csv

# Writing to a CSV file
with open('data.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['Name', 'Age', 'City'])
    csv_writer.writerow(['Alice', '25', 'New York'])
    csv_writer.writerow(['Bob', '30', 'Los Angeles'])
********************************************************
  JSON
import json

# Reading from a JSON file
with open('data.json', 'r') as file:
    data = json.load(file)
    print(data)

import json

# Writing to a JSON file
data = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}

with open('data.json', 'w') as file:
    json.dump(data, file)



