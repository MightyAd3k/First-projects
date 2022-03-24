from random import randint

print('Enter your 6 lucky numbers')


def check_input():
    """
       Check if number provided by user has correct type and if is in within the range.

       :rtype : int
       :return checked number:
       """
    while True:
        try:
            user_number = int(input())
        except (TypeError, ValueError):
            print("It's not a number")
            continue

        if user_number < 1 or user_number > 49:
            print('Number not in range')
            continue

        return user_number


def list_of_numbers():
    """
        Add all numbers typed by user to the list.

    :return: list of user's numbers
    """
    typed_numbers = []

    while len(typed_numbers) < 6:
        typed_number = check_input()
        if typed_number not in typed_numbers:
            typed_numbers.append(typed_number)

    return typed_numbers


def draw():
    """Main function of this program."""

    winning_numbers = []
    user_types = list_of_numbers()

    while len(winning_numbers) < 6:
        num = randint(1, 49)
        winning_numbers.append(num)

    hits = 0
    for i in user_types:
        if i in winning_numbers:
            hits += 1

    print(f'\nWinning numbers are: {winning_numbers}')
    print(f"User's lucky numbers: {user_types}")
    print(f'\nDear user, you have hit {hits} ' + ('numbers' if hits > 1 or hits == 0 else 'number'))


if __name__ == '__main__':
    draw()
