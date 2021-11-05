import random

mlist = ['rock', 'paper', 'scissor']
score = 100
print("Enjoy this game\n")

while True:
 answer = random.choices(mlist)
 print("This is the answer {}".format( answer))
 choice = input("Choose between rock, paper and scissor\n")

 if choice == answer:
    break
 score -=1

print("Great job, you scored {}%".format(score))


 


