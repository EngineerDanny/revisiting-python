


rows = int(input("How many rows? "))
colums = int(input("How many columns? "))
symbol = input("What symbol do you want to use ")

##outer for loops
for row in range(0,rows):
    for col in range(0, colums):
      print(symbol , end=" ")
    print("\n")  

#control of flow in loops
### break : Used to terminate from the loop entirely
### continue : Used to skip to the next iteration of the loop if it exists
### pass : does nothing but acts as a placeholder

