from random import randint

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


def dice_roller(dice_code):
    """Simple dice roller"""

    for dice in DICES:
        if dice in dice_code:
            dices, points = dice_code.split(dice)
            try:
                dice = int(dice[1:])
            except ValueError:
                return 'Wrong input'
            break
    else:
        return 'Wrong input'

    try:
        dices = int(dices) if dices else 1
    except ValueError:
        return 'Wrong input'

    try:
        points = int(points) if points else 0
    except ValueError:
        return 'Wrong input'

    return sum([randint(0, dice) for _ in range(dices)]) + points


if __name__ == '__main__':
    print(dice_roller("2D10+10"))
    print(dice_roller("D6"))
    print(dice_roller("2D3"))
    print(dice_roller("D12-1"))
    print(dice_roller("DD34"))
    print(dice_roller("4-3D6"))
