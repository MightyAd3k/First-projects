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

print('Choose your dice')
print(DICES)


def input_validator():
    """
    Check if user picked correct dice.

    :rtype: str
    :return: checked dice
    """

    while True:
        try:
            user_choice = input()
        except (TypeError, ValueError):
            print("What's that?")
            continue

        if user_choice not in DICES:
            print('Pick dice from the list')
            continue

        return user_choice


if __name__ == '__main__':
    input_validator()
