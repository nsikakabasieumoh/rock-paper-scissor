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

def not_verified(param1):
    """ Check if players entry is choices

    :param1: player's entry
    :return: bool
    """
    if param1 not in choices:
        return True
    else:
        return False
    
def player():
    # Prevent entry of int or float
    try:
        player = input("Enter choice: ").upper()
    except:
        return None
    
    # Check if entry is either R, P or S
    if not_verified(player):
        return None
    
    return player
    
def compare(param1, param2) -> str:
    """ Check winner

    :param1: player's choice
    :param2: computer's choice
    :return: str
    """
    diff = assigned[param1] - assigned[param2]

    if diff in p_wins:
        return 'Player Wins'
    elif diff in c_wins:
        return 'Computer Wins'
    else:
        return "It's a Draw!"
