# weight = input('what weight do you want? Kilo or pounds? type K or P ')
# if weight == 'K' or 'k':
#     kilo = float(input('how many kilos?'))
#     print ("thats "+ str(kilo/2.2)+" pounds.")

# elif weight == 'P' or 'p':
#     pounds = input('how many pounds?')
#     print("thats ", str(pounds*2.2), "kilos.p")
# else:
#     print('please type k or p')


# email = input("what is your email?")

# index = email.index('@')

# username = email[:index]

# domain = email[index + 1:]

# print(f"your username is {username} and your domain is {domain}.")


# money = 0
# rate = 0
# time = 0

# while True:
#     investment = float(input('How much money do you want to invest?'))
#     if investment < 0: print("type something reasonable.")
#     else:
#         break
# while True:
#     rate = float(input('How high of an interest do you want for your investment?'))
#     if rate < 0: print("type something reasonable.")
#     else:
#         break
# while True:
#     time = int(input('How long do you want to invest?'))
#     if time < 0: print("type something reasonable.")
#     else:
#         break

# earnings = investment*pow((1+rate/100), time)

# print(f'your earnings amount to {earnings: .2f}')

# import time


# timer= int(input('how many seconds?'))

# for i in range(0, timer):
#     if timer == i:
#         print('times up')
#     time.sleep(1)
#     print(timer-int(i))
   
# timer = int(input('how many seconds?'))

# for i in reversed(range(0, timer,+1)):
#     seconds = (i+1) % 60
#     minutes = int(i/60) % 60
#     hours =  int(i/3600)
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")
#     time.sleep(1)

# print('times up')

# foods = []
# prices = []
# total = 0

# while True:
#     try:
#         food = input('what food do you want q to quit: ')
#         if food == "q":
#             break
#         else:
#             price = float(input(f"what does {food} cost"))
#             foods.append(food)
#             prices.append(price)
#     except ValueError:
#         print('Please type the price.')
#         break


# for food in foods:
#     print(food, end=' ')

# for price in prices:
#     total = total + price


# print(f"your total adds up to {round(total, 2)} euros.")

# (("What is the highest mountain?"),
#              ("What is the biggest animal?"),
#              ("What is the most populated country?"),
#              ("What is the biggest country?"))

# questions = ("What is the highest mountain?",
#              "What is the biggest animal?",
#              "What is the most populated country?",
#              "What is the biggest country?")

# options = (("A: vogelberg", "B: dog", "C: cat", "D: mount everest"),
#            ("A: ant", "B: cat", "C:lion", "D: whale"),
#            ("A: germany", "B: india", "C: usa", "D: china"),
#            ("A: usa", "B:russia", "C:chile", "D:china"))

# answers = ("D", "D", "B", "B")

# guesses = []
# score = 0
# question_num = 0


# for question in questions:
#     print("------------------------")
#     print(question)
#     for option in options[question_num]:
#         print(option)
#     guess = input(f"What is your guess?").upper()
#     guesses.append(guess)
#     if guess == answers[question_num]:
#         score += 1
#         print("Correct answer!")
#     else:
#         print('Sadly wrong answer...')
#         print(f"{answers[question_num]} is the correct answer")
#     question_num += 1



# score_end = (score/len(questions))*100



# print('-----------------------------------')
# print(f"you got {score} out of {(len(questions))} questions right which is {score_end}%!")
# print('----------------------------------------------')

# for option in options[1]:
#     print(option)
#     print('--------------------------------')


# menu = {'piza': 3.5,
#         'hotdog': 2.5,
#         'apple': 1.5,
#         'pinapple': 2,
#         'lasagne': 5,
#         'doener': 7}

# cart= []
# total = 0


# for food, price in menu.items():
#     print(f"{food:10}: {price:.2f}")


# while True:
#     food = input('What do you want in your cart? (q to quit): ').lower()
#     if food == 'q':
#         break
#     elif menu.get(food) is not None:
#         cart.append(food)

# for food in cart:
#     total = total + menu.get(food)
#     print(food, end= ' ')

# print(f"your total is {total:.2f} euros. ")

# print(menu.get("piza"))



# import random
# lowest_num = 1
# highest_num = 100

# random_num = random.randint(lowest_num, highest_num)
# print(random_num)
# guesses = 0
# is_running = True

# while is_running is True:
#     guess = input(f"What is your guess? Number between {lowest_num} and {highest_num}: ")
#     if guess.isdigit():
#         guesses += 1
#         guess = int(guess)
#         if guess == random_num:
#             is_running = False
#             print(f"{guess} is right! It took you {guesses} tries.")
#         elif guess < lowest_num or guess > highest_num:
#             print('number out of range')
#         elif guess < random_num:
#             print('your guess is too low')
#         elif guess > random_num:
#             print('your guess is too high')
#     else:
#         print('please type an integer.')


# import random

# options = ('rock', 'paper', 'scissor')
# run_it = True

# while run_it:
#     player_input = None
#     random_guess = random.choice(options)
#     while player_input not in options:
#         player_input = input("Rock, paper or scissor?").lower()
#     if random_guess == player_input:
#         print('its a tie')
#     elif player_input == 'rock' and random_guess == 'scissor':
#         print('you win')
#     elif player_input == 'paper' and random_guess == 'rock':
#         print('you win')
#     elif player_input == 'scissor' and random_guess == 'paper':
#         print('you win')
#     else:
#         print('you lose')
#     if not input('you you want to continue? (y/n)').lower() == "y":
#         run_it = False
    
# import random

# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518 ")

#  ●┌ ─ ┐ │ └ ┘ 

# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"


# dice_art = {
#     1: ("┌─────────┐",
#         "│         │",
#         "│    ●    │",
#         "│         │",
#         "└─────────┘"),
#     2: ("┌─────────┐",
#         "│   ●     │",
#         "│         │",
#         "│      ●  │",
#         "└─────────┘"),
#     3: ("┌─────────┐",
#         "│  ●      │",
#         "│    ●    │",
#         "│      ●  │",
#         "└─────────┘"),
#     4: ("┌─────────┐",
#         "│  ●    ● │",
#         "│         │",
#         "│  ●    ● │",
#         "└─────────┘"),
#     5: ("┌─────────┐",
#         "│ ●     ● │",
#         "│    ●    │",
#         "│ ●     ● │",
#         "└─────────┘"),
#     6: ("┌─────────┐",
#         "│  ●   ●  │",
#         "│  ●   ●  │",
#         "│  ●   ●  │",
#         "└─────────┘")
# }


# dice = []
# total = 0

# num_dice = int(input("how many dice?: "))

# random.randint(1, 6)


# for die in range(num_dice):
#     dice.append(random.randint(1, 6))


# # for die in range(num_dice):
# #     for line in dice_art.get(dice[die]):
# #         print(line)

# for line in range(5):
#     for die in dice:
#         print(dice_art.get(die)[line], end = '')
#     print()



# for die in dice:
#     total = total + die

# print(f"your total is {total} ")



# import string
# import random

# chars = " " + string.punctuation + string.ascii_letters + string.digits
# chars = list(chars)
# # print(chars)

# key = chars.copy()

# random.shuffle(key)
# # print(key)

# message_true = input("What is your messsage?  ")
# encrypted_message = ""

# for letter in message_true:
#     index = chars.index(letter)
#     encrypted_message += key[index]

# print(message_true)
# print(encrypted_message)
    
    

# encrypted_message = input('whats to decrypt? ')
# message_true = ""

# for letter in encrypted_message:
#     encryption = key.index(letter)
#     message_true = message_true + chars[encryption]

# print(encrypted_message)
# print(message_true)



# circleradius = 30

# area_circle = 3.14 * pow(circleradius, 2)
# print(area_circle)

# circum_of_circle = 2 * circleradius * 3.14
# print(circum_of_circle)


# def get_user_input():
#     get_user_radius = int(input("What is the radius of the circle? "))
#     print(pow(get_user_radius, 2) * 3.14)

# get_user_input()


# list = ["kiwi", 'banana', 'apple']

# list.append("dog")

# print(list)


# diction = {
#     'firstkey': "value1",
#     'secondkey': "value2",
#     'thirdkey': "value3",
#     'fourthkey': {
#         'firstkeyoffourthkey': ["kiwi", 'banana', 'apple']
#     }
# }

# keyofdict = diction.get('fourthkey')
# print(keyofdict)

# diction.pop('firstkey')
# diction.popitem()
# print(diction)



# diction.get('fourthkey').get('firstkeyoffourthkey').append('dog')


# print(diction.get("fourthkey").get('firstkeyoffourthkey'))


#hangman_game


# import random

# words_for_guessing = ['Apple', 'Banana', 'Kiwi', 'Pinapple', 'Dog']

# hangman_art = { 0: (" ",
#                    " ",
#                    " "),
#             1:(" o ",
#                "   ",
#                "   "),
#             2:(" o ",
#                " | ",
#                "   "),
#             3:(" o ",
#                "/| ",
#                "   "),
#             4:(" o ",
#                "/|\\ ",
#                "   "),
#             5:(" o ",
#                "/|\\",
#                "/  "),
#             6:(" o ",
#                "/|\\",
#                "/ \\")}

# for x in  range(0, 7):
#     for line in hangman_art[x]:
#         print(line)
# # for y in range(1, 7):
# #     print(y)


# def game_intro():
#     print('-----WELCOME!!!------')
#     random_word = words_for_guessing[random.randrange(0, 5)]
#     while True:
#         input("Guess a letter")


# random_word = words_for_guessing[random.randrange(0, 5)]

# print(random_word)

#vier gewinnt

# spielfeld = {
#    1: [0,0,0,0,0,0,0],
#    2: [0,0,0,0,0,0,0],
#    3: [0,0,0,0,0,0,0],
#    4: [0,0,0,0,0,0,0],
#    5: [0,0,0,0,0,0,0],
#    6: [0,0,0,0,0,0,0]
# }


# print(spielfeld.get(1)[1])
# print(len(spielfeld))

# navigation1 = ['a', 'b', 'c', 'd', 'e', 'f']
# navigation2 = [ '1', '2', '3', '4', '0', '6', '7']

# print('  ', end='')
# for nav in range(len(navigation2)):
#     print('', end='')
#     print(navigation2[nav], end= ' ')
# print('')
# for spielfeldreihe in range(0, len(spielfeld)):
#     print(navigation1[spielfeldreihe], end= ' ')
#     for einzelfeld in range(0, len(spielfeld.get(1))):
#         print('O', end= ' ')
#     print('')

import string
import stringprep

# def check_winner():
#     # horizontal
#     for row in range(len(spielfeld), 0, -1):
#         for col in range(1, 8):
#             if col >= 4:
#                 player_1 = 0
#                 player_2 = 0
#                 for x in range(col, col-4, -1):
#                     if spielfeld.get(row)[x-1] == 1:
#                         player_1 += 1
#                         if player_1 == 4:
#                             return 1
#                     if spielfeld.get(row)[x-1] == 2:
#                         player_2 += 1
#                         if player_2 == 4:
#                             return 2
    
#     # for vertical

#     for row_for_vertical in range(1, len(spielfeld)+1):
#         for column in range(0, 7):
#             if row_for_vertical <= 3:
#                 player_1_vertical = 0
#                 player_2_vertical = 0
#                 for going_vertical in range(row_for_vertical, row_for_vertical+4):
                    
#                     if spielfeld.get(going_vertical)[column] == 1:
#                         player_1_vertical += 1
#                         if player_1_vertical == 4:
#                             return 1
#                     if spielfeld.get(going_vertical)[column] == 2:
#                         player_2_vertical += 1
#                         if player_2_vertical == 4:
#                             return 2
    
    
#     for diag1_row in range(1, len(spielfeld)+1):
#         for diag1_column in range(0, len(spielfeld.get(1))):
#             if diag1_column >= 4:
#                 player_1_diag_1 = 0
#                 player_2_diag_1 = 0
                
#                 for going_diag1 in range(diag1_column-3, diag1_column+1):
#                     for i in range(4):
#                         if spielfeld.get(diag1_row+i)[going_diag1] == 1:
                        
#                             player_1_diag_1 += 1
#                             if player_1_diag_1 == 4:
#                                 return 1
#                     if spielfeld.get(diag1_row)[going_diag1] == 2:
#                         player_2_diag_1 += 1
#                         if player_2_diag_1 == 4:
#                             return 2
                    
         

#     return 0
    


def check_winner_version2():

    row = len(spielfeld)
    column = len(spielfeld[1])
   

    for ro in range(1, row+1):
        for col in range(column):
            if col >= 3 and ro <= 3:
                if all(spielfeld.get(ro+i)[col-i] == 1 for i in range(4)):
                    return 1
                elif all(spielfeld.get(ro+i)[col-i] == 2 for i in range(4)):
                    return 2
    


    for ro in range(1, row+1):
        for col in range(0, column):
            if col <= 3 and ro <= 3:
                if all(spielfeld.get(ro+i)[col+i] == 1 for i in range(4)):
                    return 1
                elif all(spielfeld.get(ro+i)[col+i] == 2 for i in range(4)):
                    return 2

    
    for ro in range(1, row+1):
        for col in range(column):
            if col <= 4:
                if all(spielfeld.get(ro)[col+i] == 1 for i in range(4)):
                    return 1
                elif all(spielfeld.get(ro)[col+i] == 2 for i in range(4)):
                    return 2
    
    for ro in range(1, row+1):
        for col in range(column):
            if ro <= 3:
                if all(spielfeld.get(ro+i)[col] == 1 for i in range(4)):
                    return 1
                elif all(spielfeld.get(ro+i)[col] == 2 for i in range(4)):
                    return 2



    return 0
                




spielfeld = {
   1: [0,0,0,0,0,0,0],
   2: [0,0,0,0,0,0,0],
   3: [0,0,0,0,0,0,0],
   4: [0,0,0,0,0,0,0],
   5: [0,0,0,0,0,0,0],
   6: [0,0,0,0,0,0,0]
}


# print(spielfeld)

# spielfeld.get(1)[1] = 1

# print(spielfeld.get(1))
i = 0
while True:
    for a in range(0, len(spielfeld)):
        print(spielfeld[a+1])
    


    x = check_winner_version2()
    if x == 0:
        pass
    elif x == 2:
        print('player 2 won')
        break
    elif x == 1:
        print('player 1 won')
        break
    

    
    column_player1 = (input("player 1 which column? 1-7: "))
   
    if column_player1== 'quit':
        break
    elif column_player1.isnumeric() is True:
        column_player1 = int(column_player1)-1

        if column_player1 >= 8:
            print('number is too high')
            break
        if column_player1 < 0:
            print('number is too low')
            break
        else:
            pass
    else:
        print("Please type a valid column")
        break
    
    for row in range(len(spielfeld), 0, -1):
        if spielfeld.get(row)[column_player1] == 0:
            spielfeld.get(row)[column_player1] = 1
            break



    for a in range(0, len(spielfeld)):
        print(spielfeld[a+1])





    x = check_winner_version2()
    if x == 0:
        pass
    elif x == 2:
        print('player 2 won')
        break
    elif x == 1:
        print('player 1 won')
        break






    
    column_player2 = (input("player 2 which column? 1-7: "))
    if column_player2 == 'quit':
        break
    elif column_player2.isnumeric() is True:
        column_player2 = int(column_player2)-1
        if column_player2 >= 7:
            print('number is too high')
            break
        if column_player2 < 0:
            break
    else:
        print("Please type a valid column")
        break
    

    
    for row_ in range(len(spielfeld), 0, -1):
        if spielfeld.get(row_)[column_player2] == 0:
            spielfeld.get(row_)[column_player2] = 2
            break


    
           
    

