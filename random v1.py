def start_game(money_for_game):
    money_to_return = -1
    while money_for_game >= 1:
        print(f"You currently have ${money_for_game} in the game")
        quit_chance = input("Do you want to spend $1 to start the game?(Y/N): ").upper()
        if quit_chance == 'Y':
            money_for_game -= 1
            money_for_game = chance_part(money_for_game)
            money_to_return = money_for_game
        elif quit_chance == 'N':
            money_to_return = money_for_game
            money_for_game = 0
        else:
            print("That is not an answer")
    return money_to_return


start_game()
