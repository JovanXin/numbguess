#setting variables
min = 1
max = 1000
steps = 0
#importing math for math.ceil function
import math
#loops the program
while True:
  bestGuess = math.ceil((min + max - 1) / 2)
  userGuess = ""
  while userGuess != ("y", "l", "h"):#"y" or userGuess != "l" or userGuess != "y":
    userGuess = input("is "+str(bestGuess)+" your number? (y), too high(h) or too low(l): ")
    #adds one to stepp
    steps +=1
    print(min, max)
    if userGuess == ("y"):
      print("yes good job")
      exit()
    if userGuess == ("l"):
      min = bestGuess + 1
      break
    if userGuess == ("h"):
      max = bestGuess - 1
      break
