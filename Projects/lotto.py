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


if __name__ == '__main__':
    check_input()
