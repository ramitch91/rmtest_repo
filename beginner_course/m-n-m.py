import random

print("-----------------------------")
print("      M&M Guessing Game!")
print("-----------------------------")

mm_count = random.randint(1, 100)
attempt_limit = 5
attempts = 0

print("Guess the number of M&Ms and you get lunch on the house!")
print()

while attempts < attempt_limit:
    guess_text = input("How many M&Ms are in the jar? ")
    guess = int(guess_text)
    attempts += 1

    if mm_count == guess:
        print(f"You got a free lunch! It was {guess}.")
        break
    elif mm_count < guess:
        print("Sorry, that is too HIGH!")
    else:
        print("Sorry, that is too LOW!")

print(f"Bye, you're done in {attempts}!")
