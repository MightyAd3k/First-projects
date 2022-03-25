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
print(DICES)
print('Pick 2 dices from the list')


def check_input():
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





if __name__ == '__main__':
    check_input()