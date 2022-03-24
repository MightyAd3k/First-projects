from random import randint

print('Guess the number.\nChoose one from 1 - 100')


def check_input():
    """
    Check if number provided by user has correct type and if is in within the range.

    :rtype : int
    :return checked number:
    """
    while True:
        try:
            user_guess = int(input())
        except (TypeError, ValueError):
            print('It is not a number')
            continue

        if user_guess < 1 or user_guess > 100:
            print('Number not in requested range')
            continue

        return user_guess


def game():
    """Main function of the game"""

    secret_number = randint(1, 100)
    user_number = check_input()
    counter = 0

    while user_number != secret_number:
        counter += 1
        if user_number < secret_number:
            print('Your number is too small')

        elif user_number > secret_number:
            print('Your number is too big')
        user_number = check_input()
    print(f'You win! You did it in {counter} times.')


if __name__ == '__main__':
    game()
