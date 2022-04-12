import random


def main():
    while True:
        yes_no = input("Have you played Lucky Unicorn before? (Y/N): ").upper()
        if yes_no == 'Y':
            welcome()
            exit()
        elif yes_no == 'N':
            instructions()
            exit()
        else:
            print("That is not an answer")


def instructions():
    print()
    print("""* How to play *
    Choose a starting amount to play with - must be between $1 and $10
    Then press <enter> to play. You will get a random token which might be a
    horse, a zebra, a donkey, or a lucky unicorn.
    It costs $1 to play each round but, depending on your prize, you could
    win some of your money back. These are the payout amounts:
    \tLucky Unicorn: $5 (balance increases by $4
    \tHorse: $0.50 (balance decreases by $0.50
    \tZebra: $0.50 (balance decreases by $0.50
    \tDonkey: $0.00 (balance decreases by $1
    \nSee if you can avoid donkeys, get the lucky unicorns, and finish
    with more money than you started with.
    """)
    print("*" * 50)
    print("p.s. Make sure to have fun")
    welcome()


def welcome():
    money_to_return = -1
    print("""
    ----------------------------------------------------------
    Welcome to lucky unicorn
    ----------------------------------------------------------
    """)
    start = input("Press enter if you want to play: ")
    if start == '':
        money_to_return = check_money()
    else:
        print("Goodbye")

    if money_to_return > 0:
        print(f"A refund of ${money_to_return} is due. Have a good day")
    elif money_to_return == 0:
        print("Sorry you lost your money, have a good day")


def check_money():
    money_to_return = -1
    correct_money_amount = False
    while not correct_money_amount:
        try:
            money_for_game = float(input("How much do you want to spend "
                                         "between $1 and $10: $"))
            if 1 <= money_for_game <= 10:
                correct_money_amount = True
                money_to_return = start_game(money_for_game)
            else:
                print(f"You entered ${money_for_game}, which isn't between "
                      f"$1 and $10!")
        except ValueError:
            print("You didn't enter a number between $1 and $10!")
    return money_to_return


def start_game(money_for_game):
    money_to_return = -1
    while money_for_game >= 1:
        print(f"You currently have ${money_for_game} in the game")
        quit_chance = input("Do you want to spend $1 to start the game?(Y/N): "
                            "").upper()
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


def chance_part(money_for_game):
    random_choice = random.randint(1, 16)
    if random_choice == 1:
        print("You got a lucky Unicorn and won $5!")
        money_for_game += 5
    elif random_choice <= 9:
        if random_choice % 2:
            print("You got a Horse and won $0.50!")
            money_for_game += 0.5
        elif not random_choice % 2:
            print("You got a Zebra and won $0.50!")
            money_for_game += 0.5
    else:
        print("You got a Donkey and didn't win anything!")
    return money_for_game


main()
