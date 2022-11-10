import random

cards = [6, 7, 8, 9, 10, 11, 2, 3, 4, 11] * 4
random.shuffle(cards)

print("Lets play BlackJack")
count = 0
count_bot = 0

while True:
    choice = input("Take card y/n\n")
    if choice == 'y':
        current = cards.pop()
        current_bot = cards.pop()
        print("You take", current)
        count += current
        count_bot += current_bot
        if count > 21 or count_bot > 21:
            if count_bot > 21 and count < 21:
                print("Bot loose. Bot have", count_bot, "You have", count)
                choice = input("Would you like to play again? y/n\n")
                if choice == 'y':
                    cards = [6, 7, 8, 9, 10, 11, 2, 3, 4, 11] * 4
                    print("Lets play BlackJack")
                    count = 0
                    count_bot = 0
                else:
                    break
            elif count > 21 and count_bot < 21:
                print("You loose. You have", count, "Bot have", count_bot)
                choice = input("Would you like to play again? y/n\n")
                if choice == 'y':
                    cards = [6, 7, 8, 9, 10, 11, 2, 3, 4, 11] * 4
                    print("Lets play BlackJack")
                    count = 0
                    count_bot = 0
                else:
                    break
            elif count > 21 and count_bot > 21:
                print("You loose and Bot loose. You have", count, "Bot have", count_bot)
                choice = input("Would you like to play again? y/n\n")
                if choice == 'y':
                    cards = [6, 7, 8, 9, 10, 11, 2, 3, 4, 11] * 4
                    print("Lets play BlackJack")
                    count = 0
                    count_bot = 0
                else:
                    break
        elif count == 21 or count_bot == 21:
            if count == 21:
                print("You win. You have", count, "Bot have", count_bot)
                choice = input("Would you like to play again? y/n\n")
                if choice == 'y':
                    cards = [6, 7, 8, 9, 10, 11, 2, 3, 4, 11] * 4
                    print("Lets play BlackJack")
                    count = 0
                    count_bot = 0
                else:
                    break
            elif count_bot == 21:
                print("Bot win. Bot have", count, "You have", count)
                choice = input("Would you like to play again? y/n\n")
                if choice == 'y':
                    cards = [6, 7, 8, 9, 10, 11, 2, 3, 4, 11] * 4
                    print("Lets play BlackJack")
                    count = 0
                    count_bot = 0
                else:
                    break
        else:
            print("You score:", count)
    elif choice == 'n':
        print('Count', count)
        break
print('Good luck')