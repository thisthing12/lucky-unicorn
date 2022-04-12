def main():
    while True:
        yes_no = input("Have you played Lucky Unicorn before? ").lower()
        if yes_no == 'y' or 'yes':
            welcome()
            exit()
        elif yes_no == 'n' or 'no':
            instructions()
            exit()
        else:
            print("That is not an answer")


def instructions():
    print("""* How to play *
    
    Choose a starting amount to play with - must be between $1 and $10
    
    Then press <enter> to play. You will get a random token which might be a horse, a zebra, a donkey, or a lucky unicron.
    
    It costs $1 to play each round but, depending on your prize, you could win some of your money back. These are the payout amounts:
    \tLucky Unicorn: $5 (balance increases by $4
    \tHorse: $0.50 (balance decreases by $0.50
    \tZebra: $0.50 (balance decreases by $0.50
    \tDonkey: $0.00 (balance decreases by $1
    \nSee if you can avoid donkeys, get the lucky unicorns, and finish with more money than you started with.
    
    """)
    print("*" * 50)
    welcome()

main()
