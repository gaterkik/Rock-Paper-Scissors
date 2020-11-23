import random

DEFAULT_WEAPONS = ('rock', 'paper', 'scissors')
WEAPONS = DEFAULT_WEAPONS

user_name = input('Enter your name:')
user_rating = 0


def greeting():
    print('Hello,', user_name)


def new_weapons():
    global WEAPONS
    new_weapon = input().split(',')
    if len(new_weapon) > 2:
        WEAPONS = new_weapon
    else:
        WEAPONS = DEFAULT_WEAPONS


def who_is_win(weapon_one, weapon_two):
    global WEAPONS
    temp_list = WEAPONS[WEAPONS.index(weapon_one) + 1::] + WEAPONS[:WEAPONS.index(weapon_one):]
    if weapon_one == weapon_two:
        return 'draw'
    elif weapon_two in temp_list[:int((len(temp_list) / 2))]:
        return 'loose'
    else:
        return "win"


def get_rating():
    global user_rating
    rating_file = open('rating.txt', 'r')
    rating = dict()
    for item in rating_file.read().split('\n'):
        rating.update({item.split()[0]: item.split()[1]})
    if user_name in rating:
        user_rating = int(rating[user_name])
    rating_file.close()


def game():
    print("Okay, let's start")
    while True:
        global user_rating
        global WEAPONS
        player_turn = input()
        if player_turn == '!exit':
            print('Bye!')
            break
        elif player_turn == '!rating':
            print('Your rating:', user_rating)
            continue
        elif player_turn not in WEAPONS:
            print('Invalid input')
            continue
        comp_turn = random.choice(WEAPONS)
        result = who_is_win(player_turn, comp_turn)
        if result == 'win':
            print('Well done. The computer chose {} and failed'.format(comp_turn))
            user_rating += 100
        elif result == 'loose':
            print('Sorry, but the computer chose {}'.format(comp_turn))
        elif result == 'draw':
            print('There is a draw ({})'.format(comp_turn))
            user_rating += 50


greeting()
new_weapons()
get_rating()
game()
