import random
low = 1
high = 10
#mid = low + (highest - low)//2
answer = random.randint(low,high)
print(answer)
print("Please guess a number between 1 to {}: ".format(high))
input("Please press ENTER to start")
guesses = 1
while True:
    guess = low + (high-low) // 2
    high_low = input("My guess is {}. Should I guess higher or lower?"
                     "Enter h or l, or c if my guess was correct"
                     .format(guess)).casefold()
    if high_low == "h":
         #Gues higher. The low end of the range becomes 1 greater than the guess.
        low = guess + 1
    elif high_low == "l":
        #Gues lower. The high end of the range becomes 1 less than the guess.
        high = guess - 1
    elif high_low == "c":
        print("I got it in {} guesses!".format(guesses))
        break
    else:
        print("Please enter h, l or c")
    guesses = guesses + 1
