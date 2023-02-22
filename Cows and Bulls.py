import random
from itertools import permutations


# Used to calculate all possible choices that suit the given Cows and Bulls
def scorecalc(guess, chosen):
    bulls = 0
    cows = 0
    for g,c in zip(guess, chosen):
        if g == c:
            bulls += 1
        elif g in chosen:
            cows += 1
    return bulls, cows

# Used to check if the Cows or Bulls input is correct
def valid_computer_input(the_input):
    value = int(the_input) if the_input.isnumeric() else -1

    if value > 4 or value < 0:
        return valid_computer_input(input("Invalid input. Please type a number between 0 and 4:\n>"))
    return int(the_input)

# Used to check if the input has 4 unique digits
def valid_human_input(the_input):
    if not the_input.isnumeric() or len(set(the_input)) != 4:
        return valid_human_input(input("Invalid input. Please type 4 UNIQUE digits:\n>"))
    return the_input

# Used to display the rules of the game
def show_rules():
    print("""\n\nThe player must write a 4-digit secret number (on a piece of paper or on your computer somewhere).
The digits must be all different. Then, in turn, the player try to guess their opponent's number
who gives the number of matches.
If the matching digits are in their right positions, they are "bulls", if in different positions,
they are "cows".

Example:
Secret number: 4271
Opponent's try: 1234
Answer: 1 bull and 2 cows. (The bull is "2", the cows are "4" and "1".)

The first player to reveal the other's secret number wins the game.\n\n""")




print("Wellcom to bulls and cows.")
rules = input("If you want to see the rules of the game please type 'yes'.\nIf you alredy know the rules please type 'no'.\n>").strip().lower()
if rules.startswith("y"):
    show_rules()

# Generates a list of all possible permutations of 4-digit numbers (0-9) and shuffles them
choices = list(permutations('0123456789', 4))
random.shuffle(choices)

answers, scores = [], []
# Chooses a random number from the list of permutations as the computer's secret number
computer_number = ''.join(random.sample("0123456789", 4))

print("Ready to try it out?")
while True:
    # Gets the human's guess and validates it
    human_guess = valid_human_input(input("\nTry to guess my number:\n>").strip())
    human_cows = 0
    human_bulls = 0

    # If the human's guess is correct, the game ends and the human wins
    if human_guess == computer_number:
        print(f"\nGood job! You correctly guessed my number: {computer_number}\nYou WIN!")
        break

    # Calculates the Bulls and Cows for the human's guess
    for i in range(4):
        if human_guess[i] == computer_number[i]:
            human_bulls += 1
        elif human_guess[i] in computer_number:
            human_cows += 1


    print(f"You have {human_bulls} bulls and {human_cows} cows")

    # Chek if there are no more choice left except the correct human number
    if len(choices) == 1:
        print (f"\nThere are no other options available, so your number is {''.join(choices[0])}")
        print("\nThanks for playing :)")
        break
    
    # Computer gets a guess from the shuffled choices
    computer_guess = "".join(choices[0])
    answers.append(choices[0])
    print(f"\nMy guess is {computer_guess}")

    # Get the number of Bulls for the computer's guess and validates it
    computer_bulls = valid_computer_input(input("Tell me how many Bulls I have:\n>").strip())
    if computer_bulls >= 3:
        print("\nYay. I guessed your number.")
        print("Thanks for playing :)")
        break

    # Get the number of Cows for the computer's guess and validates it
    computer_cows = valid_computer_input(input("Tell me how many Cows I have:\n>").strip())

    # Validates if Cows and Bulls are correctly entered
    while computer_cows + computer_bulls > 4:
        print(f"\nInvalid input for Bulls: {computer_bulls} and Cows: {computer_cows}.")
        print("Please check again and tell me the actual number of Bulls and Cows I have.")
        computer_bulls = valid_computer_input(input("\nHow many Bulls I have:\n>").strip())
        computer_cows = valid_computer_input(input("How many Cows I have:\n>").strip())

    score = (computer_bulls, computer_cows)
    scores.append(score)
    # The choices list is filtered based on the score calculated by the scorecalc function
    choices = [choice for choice in choices if scorecalc(choice, computer_guess) == score]

    # If the filtered choices list is empty, it means something is wrong with the Bulls and Cows values provided
    if not choices:
        print("\nSomething is wrong.. Nothing fits those Bulls and Cows you gave:")
        print('  ' + '\n  '.join(f"{''.join(answer)} -> Bulls: {score[0]} Cows: {score[1]}" for answer,score in zip(answers, scores)))
        break