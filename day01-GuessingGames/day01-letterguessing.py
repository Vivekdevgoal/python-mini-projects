import random

letter = random.choice('abcdefghijklmnopqrstuvwxyz')
attempt = 0

while True:
    guess = input("Guess a letter from a to z: ").lower()
    attempt += 1

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue

    if guess == letter:
        print(f"🎉 You guessed it right! The letter was '{letter}'.")
        print("Number of attempts:", attempt)
        break

    elif guess < letter:
        print("Your guess is lower. Try a higher letter.")

    else:
        print("Your guess is higher. Try a lower letter.")

    if attempt == 5:
         print("❌ Game Over! The letter was:", letter)
         break

