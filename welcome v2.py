def welcome():
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


welcome()
