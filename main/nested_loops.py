


rows = int(input("How many rows? "))
colums = int(input("How many columns? "))
symbol = input("What symbol do you want to use")

##outer for loops
for row in range(0,rows):
    for col in range(0, colums):
      print(symbol , end=" ")
    print("\n")  
