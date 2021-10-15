#Accepting user inputs and making decisions based on them 

 
try:
  name = input("What is your name\n")
  age = input("How old were you last year \n")
  print("Welcome to the best program ever "+ name + "\n")
  
  #add one to the age 
  age = int(age) + 1

  print("You are "+  str(age) + " years old")
except:
  print('An exception occurred')