import random
import time

DIGITS = 4  # number of digits guessed


def generate_number(digits):
    numbers = list(range(0, 10))
    return random.sample(numbers, digits)  # list of integers


def get_user_input():
    """Returns a list of numbers entered by user."""
    while True:
        usrinput = input('Guess a {}-digit number: '.format(DIGITS))
        if usrinput.isdigit() and len(usrinput) == DIGITS:
            lst = []
            for i in usrinput:
                lst.append(int(i))
            return lst
        else:
            print('Invalid input.')


def evaluate(user_list, guessed_list):
    bulls = 0
    cows = 0
    for i in range(0, DIGITS):
        if user_list[i] == guessed_list[i]:
            bulls += 1
        elif user_list[i] in guessed_list:
            cows += 1
    return bulls, cows


def print_score(*score):
    print('{0} bulls, {1} cows'.format(*score))


def main():
    print('Welcome to the game Bulls & Cows!\n')

    num_list = generate_number(DIGITS)  # guessed numbers
    guess = []  # user guess
    no_attempts = 0
    start_time = time.time()

    while guess != num_list:
        guess = get_user_input()
        score = evaluate(guess, num_list)
        print_score(*score)
        no_attempts += 1

    print('Correct, you\'ve guessed the right number in {} attempts and {:.1f} minute(s)!'.format(
          no_attempts, (time.time()-start_time)/60))


main()
