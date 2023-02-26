import random

secret_number = random.randint(1, 100)
num_guesses = 10

for i in range(num_guesses):
    guess_num = int(input("Guess a number between 1 and 100: "))

    if guess_num == secret_number:
        print("Congratulations! You guessed the number in", i+1, "guesses.")
        break
    else:
        if guess_num < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
            
if guess_num != secret_number:
    print("Sorry, you ran out of guesses. my number  was", secret_number)
    
    
    