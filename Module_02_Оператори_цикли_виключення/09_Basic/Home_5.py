import random

print("Welcome to game:\'Rock, paper, scissiors'")
print('The game will go agains the computer')
print('Use big letters to select:')
print('[R]-rock')
print('[P]-paper')
print('[S]-scissiors')

user_score = 0
user_choice = 0
bot_score = 0
bot_choice = 0

print('---GAME STARTING---')
num = ""
while num != 'no':
    for i in range(3):
        print('--- ROUND #', str(i+1), '----')
        bot_choice = random.choice(['R', 'S', 'P'])
        # print(bot_choice)
        user_choice = input('Your choise\n')
        print('You:', user_choice, "& Bot:", bot_choice)
        if user_choice == bot_choice:
            print('Draw')
        elif user_choice == 'R':
            if bot_choice == 'S':
                user_score += 1
                print('Player is win')
            else:
                bot_score += 1
                print('Bot won round')
        elif user_choice == 'S':
            if bot_choice == 'P':
                user_score += 1
                print('Plaer won round')
            else:
                bot_score += 1
                print('Bot won round')
        elif user_choice == 'P':
            if bot_choice == 'R':
                user_score += 1
                print('Plaer won round')
            else:
                bot_score += 1
                print('Bot won round')
        else:
            print('Error')

    if bot_score > user_score:
        print('Bot won, bot score = ', bot_score, 'you score = ',  user_score)
    elif bot_score < user_score:
        print('You won, you score = ',  user_score, 'bot score = ', bot_score)
    else:
        print('Draw')

    num = input("do you want to play again? [yes], [no] \n")


    # for i in range(3):
    #     print('--- ROUND #', str(i + 1), '----')
    #     bot_choice = random.choice([R, S, P])
    #     # print(bot_choice)
    #     user_choice = input('Your choise')
    #     print('You:', user_choice, "& Bot:", bot_choice)
    #     R = 'R'
    #     S = 'S'
    #     P = 'P'
    #     R<P<S
