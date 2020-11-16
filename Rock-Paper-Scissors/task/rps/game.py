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
player_turn = input()
comp_turn = random.choice(WEAPONS)
# print(comp_turn)
# print(player_turn+comp_turn)
result = RULES[player_turn+comp_turn]
# print(result)
while True:
    if result == 'win':
        print('Well done. The computer chose {} and failed'.format(comp_turn))
    elif result == 'loose':
        print('Sorry, but the computer chose {}'.format(comp_turn))
    elif result == 'draw':
        print('There is a draw ({})'.format(comp_turn))
    elif result == '!exit':
        print('Bye!')
        break
    else:
        print('Invalid input')
