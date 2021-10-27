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
para_fun( "Danny", 90) #This is a positional argument

# *args is a parameter that contains tuple that has a list of varying arguments
# could be any variable name in place of the args
def sum(*numbers):
   total = 0
   for number in numbers:
      total+=number
   print("The sum of the numbers is " + str(total) )

# sum(5,90,212,2434,54,23,12,32,54,65,76)   


# **args is a parameter that contains the dictionaries of the varying arguments
# this is suitable for named paramters

def subtract(**numbers):
   result = numbers['a']-numbers['b']
   print(result)

# subtract(a=10,b=1)

#using .format() function to help get more control over string manipulation
print("My name is {} and my number is {}".format("Danny" , "05482153455"))  #positional argument
print("My name is {0} and my number is {1}".format("Danny" , "05482153455")) #positional argument
print("My name is {name} and my number is {number}".format(name = "Danny" , number ="05482153455")) #keyword or named argument
