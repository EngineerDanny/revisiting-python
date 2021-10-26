#This is a function with no arguments
def function_one():
   
 print('This is a new function')

# function_one()

#This is a function with arguments

def function_two(args):
 if args is str:
    print('Argument is a string')
 else:   
    print('Argument is not a string')
 

# function_two("asdf")



# function with positional parameters and named parameters
# optional parameters are those that are not required by the user to provide

def para_fun(name,age):
    print(name + " "+ str(age))

para_fun( name= "Danny", age= 90) #This is a named argument
para_fun( "Danny", 90) #This is a postional argument

# *args is a parameter that contains tuple that has a list of varying arguments
# could be any variable name in place of the args
def sum(*numbers):
   total = 0
   for number in numbers:
      total+=number
   print("The sum of the numbers is " + str(total) )





sum(5,90,212,2434,54,23,12,32,54,65,76)   
    
