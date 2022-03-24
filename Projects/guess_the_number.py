print('Guess the number.\nChoose one from 1 - 100')


def check_input():
    """
    Check if number provided by user is correct type and if is in within the range
    :return checked number:
    """
    while True:
        try:
            user_guess = int(input())
        except (TypeError, ValueError):
            print('It is not a number')
            continue
        return user_guess


a = check_input()
print(a)
