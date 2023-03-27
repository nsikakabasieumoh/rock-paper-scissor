import random

# Necessary data
choices = ['R', 'P', 'S']
assigned = {'R': 1, 'P': 2, 'S': 3}

# Possible wins scenarios
p_wins = (1, -2)
c_wins = (-1, 2)

def computer() -> str:
    """ Computer plays

    :return: This is the computer random choice
    """
    return random.choice(choices)

def verified(param1):
    """ Check if players entry is choices

    :param1: player's entry
    :return: bool
    """
    if param1 in choices:
        return True
    else:
        return False
    
def compare(param1, param2):
    """ Check winner

    :param1: player's choice
    :param2: computer's choice
    :return: 
    """
    diff = assigned[param1] - assigned[param2]

    if diff in p_wins:
        return 'Player Wins'
    elif diff in c_wins:
        return 'Computer Wins'
