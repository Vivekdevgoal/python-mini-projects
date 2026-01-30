import random

number = random.randint(1, 100)
attempts = 0

while True:
    try:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1

        if guess == number:
            print(f"🎉 Correct! You guessed it in {attempts} attempts.")
            print("number of final attempts: ",attempts)
            break
        elif guess < number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

        if attempts == 5:
            print("❌ Game Over! The number was:", number)
            break

    except ValueError:
        print("Please enter a valid number.")
