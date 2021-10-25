import time

def loop_one():
   name = ""
   while len(name) == 0:
       #first get the name of the user
       name = input("What is your name?\n")                     
   pass  
   print("Welcome to this program " + name)

def loop_two():
    #Printing a list of numbers in steps
    for item in range(10, 0,-1):
        time.sleep(2)
        print(item)

loop_two()

