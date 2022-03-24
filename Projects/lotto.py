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
    print(typed_numbers)


if __name__ == '__main__':
    list_of_numbers()
