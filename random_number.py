import random

def guess(x):
    ranNum = random.randint(1,x)
    guess = 0
    while guess != ranNum:
        guess = int(input(f"guess a number between 1 and {x} "))
        if guess > ranNum:
            print("oops, too high! try again")
        if guess < ranNum:
            print("opps, too low! try again")
        if guess == ranNum:
            print("Congratulations! you guessed the correct number")
guess()

def computer_guess():
    
    h = int(input("choose a high number: "))
    l = int(input("choose a low number: "))
    secretNum = int(input(f"Choose a random number between {l} and {h}: "))
    guess = random.randint(l,h)
    answer = input(f"Is your secret number {guess}? Yes (y) or No (n): ")
    while answer == 'n':
        q = input(f"is {guess} too high (h) or too low (l): ")
        if q == 'h':
            h = guess
            guess = random.randint(l,h-1)
            answer = input(f"Is your secret number {guess}? Yes (y) or No (n): ")
        if q == 'l':
            l = guess
            guess = random.randint(l+1,h)
            answer = input(f"Is your secret number {guess}? Yes (y) or No (n): ")
    if guess == secretNum:
        print(f"the number you chose is {guess}")
        

computer_guess() 