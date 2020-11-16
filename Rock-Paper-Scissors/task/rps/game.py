import random
WEAPONS = ('scissors', 'paper', 'rock')
RULES = dict(scissorspaper='win',
             scissorsrock='loose',
             paperscissors='loose',
             paperrock='win',
             rockscissors='win',
             rockpaper='loose',
             scissorsscissors='draw',
             paperpaper='draw',
             rockrock='draw')

# print(comp_turn)
# print(player_turn+comp_turn)

# print(result)
while True:
    player_turn = input()
    if player_turn == '!exit':
        print('Bye!')
        break
    elif player_turn not in WEAPONS:
        print('Invalid input')
        continue
    comp_turn = random.choice(WEAPONS)
    result = RULES[player_turn + comp_turn]
    if result == 'win':
        print('Well done. The computer chose {} and failed'.format(comp_turn))
    elif result == 'loose':
        print('Sorry, but the computer chose {}'.format(comp_turn))
    elif result == 'draw':
        print('There is a draw ({})'.format(comp_turn))

