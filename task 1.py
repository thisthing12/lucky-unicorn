"""
"""


def main():
    print("""
    ----------------------------------------------------------
    Welcome to lucky unicorn
    ----------------------------------------------------------
    """)
    start = input("Write enter if you want to play: ").lower()
    if start == 'enter':
        start_game()
    else:
        print("Goodbye")


def start_game():
    money_for_game = []
    money_for_game = int(input("How much do you want to spend between 1 and 10: "))
    while money_for_game >= 1:
        quit_chance = input("Do you want to continue?(Y/N): ").upper()
        if quit_chance == 'Y':
            chance_part(money_for_game)
        elif quit_chance == 'N':
            money_for_game.remove
            print(f"You have {money_for_game} left in the game")
        else:
            print("That is not an answer")


def chance_part(money_for_game):
    return



main()
