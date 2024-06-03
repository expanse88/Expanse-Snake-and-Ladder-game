def board(l):
    turn = 2
    for i in range(0, 100):
        l.insert(i, i + 1)
    for j in range(99, -1, -10):
        if turn % 2 == 0:
            print('|'.join(str(l[j - k]) for k in range(10)))
            print("----------------------------------------------------------------------")
            turn -= 1
        else:
            print('|'.join(str(l[j - 9 + k]) for k in range(10)))
            print("----------------------------------------------------------------------")
            turn += 1

def ladderandsnake():
    print("LADDERS\n 3-24\n 14-42\n 30-86\n 37-57\n 50-96\n 66-74\n")
    print("SNAKES\n 95-18\n 77-45\n 60-28\n 34-10\n 20-2\n")

def climb(x):
    ladders = {3: 24, 14: 42, 30: 86, 37: 57, 50: 96, 66: 74}
    return ladders.get(x, x)

def fall(y):
    snakes = {95: 18, 77: 45, 60: 28, 34: 10, 20: 2}
    return snakes.get(y, y)

def accept_from_user(move_1, move_2):
    import random
    dice = [1, 2, 3, 4, 5, 6]
    whoo = input("Enter Player 1 name in the game!-\n")
    wh = input("Enter Player 2 name in the game!-\n")
    who = int(input("Enter who wants to start the game!- Enter 1 or 2...\n"))
    while move_1 < 100 and move_2 < 100:
        if who == 1:
            chance_1 = int(input(f"{whoo} Enter 1 Roll the die!"))
            if chance_1 == 1:
                player_1 = random.choice(dice)
                move_1 += player_1
                print(f"{move_1} before climb")
                move_1 = climb(move_1)
                print(f'{whoo} is at position {move_1}')
                move_1 = fall(move_1)
                print(f"{move_1} After fall")
                print(f"{whoo} is at position {move_1}")
            else:
                print("Enter 1 to PROCEED!...")
            who = 2
        else:
            chance_2 = int(input(f"{wh} Enter 1 Roll the die!"))
            if chance_2 == 1:
                player_2 = random.choice(dice)
                move_2 += player_2
                print(f"{move_2} before climb")
                move_2 = climb(move_2)
                print(f'{wh} is at position {move_2}')
                move_2 = fall(move_2)
                print(f"{move_2} After fall")
                print(f"{wh} is at position {move_2}")
            else:
                print("Enter 1 to PROCEED!...")
            who = 1
    else:
        if move_1 >= 100:
            print(f"Congrats {whoo}!!")
        elif move_2 >= 100:
            print(f"Congrats {wh}!!")

l = []
board(l)
ladderandsnake()
accept_from_user(move_1=1, move_2=1)


