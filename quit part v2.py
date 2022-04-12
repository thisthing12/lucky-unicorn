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
        print(f"You got ${money_to_return} left. Have a good day")
    elif money_to_return == 0:
        print("Sorry you lost your money")


welcome()
