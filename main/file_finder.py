import os


print('\033[92m', end="")
path = "/Users/newuser/Desktop/test.txt"

if os.path.exists(path):
    print("Path exists")
    if os.path.isfile(path):
        print("File exists")
        #read the file if it exists
        with open(path) as file:
            print(file.read())
else :
    print("Path does not exist")

# write a text to a file
