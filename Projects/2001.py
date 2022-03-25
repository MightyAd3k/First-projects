from random import randint, choice

DICES = (
    'D3',
    'D4',
    'D6',
    'D8',
    'D10',
    'D12',
    'D20',
    'D100'
)
print('Rules of the game. If sum of points you rolled is equal to 7, the total sum of your points will be divided by 7,'
      'if sum of points you rolled is equal to 11, the total sum of your points will be multiplied by 11.\n'
      'Have fun :)\n')
print(DICES)
print('Pick 2 dices from the list\n')


def check_input():
    """
    Input validator
    :return validated user's choice:
    """

    while True:
        try:
            user_input = input()
        except (TypeError, ValueError):
            print('Wrong input')
            continue

        if user_input not in DICES:
            print('Wrong input')
            continue

        return int(user_input[1:])


def user_throw():
    """
    Throws user's dices
    :return sum of 2 dices:
    """

    user_dice1 = check_input()
    user_dice2 = check_input()
    user_result = randint(0, user_dice1) + randint(0, user_dice2)
    return user_result


def computer_throw():
    """
    Throws computer's dices
    :return sum of 2 dices:
    """
    computer_dice = int(choice(DICES)[1:])
    computer_dice1 = int(choice(DICES)[1:])
    computer_result = randint(0, computer_dice) + randint(0, computer_dice1)
    return computer_result


def user_points(points):
    """
    Calculate user's points according to the rules.
    :param points:
    :return user's points:
    """
    throw_result = user_throw()
    if throw_result == 7:
        points //= 7
    elif throw_result == 11:
        points *= 11
    else:
        points += throw_result
    return points


def computer_points(points):
    """
    Calculate computer's points according to the rules.
    :param points:
    :return computer's points:
    """
    throw_result = computer_throw()
    if throw_result == 7:
        points //= 7
    elif throw_result == 11:
        points *= 11
    else:
        points += throw_result
    return points


def game():
    """The main body of the program"""
    points_user = 0
    points_computer = 0

    points_user += user_throw()
    points_computer += computer_throw()

    while points_user < 2001 and points_computer < 2001:
        print(f'User points: {points_user} | Computer points: {points_computer}')
        points_user += user_points(points_user)
        points_computer += computer_points(points_computer)

    print(f'User points: {points_user} | Computer points: {points_computer}')
    if points_user > points_computer:
        print('You win')
    elif points_user < points_computer:
        print('Computer win')
    else:
        print('Tie')


if __name__ == '__main__':
    game()
