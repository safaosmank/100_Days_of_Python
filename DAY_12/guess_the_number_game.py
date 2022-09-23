from random import randint
from number_art import Logo

print(Logo)


number_answer = randint(1,100)


def number_guesser():
    print("Welcome to the NUmber Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    mode = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    print(number_answer)

    attempts_hard = 5
    attempts_easy = 10

    end_game = False
    if mode == "hard":
        print("You have 5 attempts remaining to guess the number.")
        while not end_game:
            guess=int(input("Make a guess: "))
            if guess == number_answer:
                print("you won")
                end_game = True
            elif guess > number_answer:
                print("Too high.")
                attempts_hard -=1
                print(f"You have {attempts_hard} attempts remaining to guess the number")
            else:
                print("Too low")
                attempts_hard -=1
                print(f"You have {attempts_hard} attempts remaining to guess the number")
            if attempts_hard == 0:
               end_game = True
               print("You lose.")

    if mode == "easy":
        print("You have 10 attempts remaining to guess the number.")
        while not end_game:
            guess=int(input("Make a guess: "))
            if guess == number_answer:
                print("you won")
                end_game = True
            elif guess > number_answer:
                print("Too high.")
                attempts_easy -=1
                print(f"You have {attempts_easy} attempts remaining to guess the number")
            else:
                print("Too low")
                attempts_easy -=1
                print(f"You have {attempts_easy} attempts remaining to guess the number")
            if attempts_easy == 0:
                end_game = True
                print("You lose.")

    continue_game = input("This round is over, run again? Y or N: ").upper()

    if continue_game == "Y":
        number_guesser()

number_guesser()
