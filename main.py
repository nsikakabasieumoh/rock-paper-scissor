from utils import functions

# Printing Rules
rules = "Enter R for Rock, P for Paper and S for Scissor. Enjoy!"
print(rules)

# Play three rounds
rounds = 0
limit = 3

while rounds < limit:
    # control the rounds
    rounds += 1
    r_left = limit - rounds

    # play the game
    player = functions.player()
    if player is None:
        print(f'Wrong entry. You have {r_left} rounds left.')
        continue
    else:
        computer = functions.computer()
        result = functions.compare(player, computer)
        print(f'{result}. You have {r_left} rounds left.')
