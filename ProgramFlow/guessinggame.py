import random

highest = 1000
high = highest
low = 1
answer = random.randint(1,highest)

print("Please guess a number between 1 to {}: ".format(highest))
while True:
    mid = low + (high - low) // 2
    guess = int(input())
    if guess == 0:
        print("Quitting")
        break
    elif guess != answer:
        if guess < answer:
            print("Please guess higher")
        else: # guess must be greater than answer
            print("Please guess lower")
    else:
        print("You got it correctly")
        break
