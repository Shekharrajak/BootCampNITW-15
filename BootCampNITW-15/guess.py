import random

solution= random.randint(0,100000)
print("Guess the number\n")

guess = int(input("enter ur no"))

while (guess!=solution):
    if guess<solution:
        print("number is less than the real no\n")
    elif guess>solution:
        print("number is greatr")
    guess=int(input("enter ur choice"))

print ("yeah correct!!!")
