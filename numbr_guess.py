import random

secret_numbr = random.randint(1,100)

tries = 0
MAX_TRIES = 5

while tries < MAX_TRIES:
    tries +=1
    
    guess = int(input("Enter your guess: "))
    
    if guess < secret_numbr:
        print("Too low..")
    elif guess > secret_numbr:
        print("Too High..")
    else:
        print(f"Congratulations! you hava guess the secret Number is {secret_numbr}")
        break
else:
    print(f"you hava used all yours tries and secret number is{secret_numbr}. ")