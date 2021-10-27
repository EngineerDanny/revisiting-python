# This program takes two inputs from the user and divides the numerator by the denominator




print('\033[92m' + 'This is the best division program ever\n')

try:
    numerator = int(input("Enter the numerator: \n"))
    denominator = int(input("Enter the denominator: \n"))
    answer = numerator / denominator
    print("The result of the division is " + str(answer))
except ZeroDivisionError:
    print("Sorry u cant divide by zero") 
except:
    print("Oops the inputs were not valid")    





