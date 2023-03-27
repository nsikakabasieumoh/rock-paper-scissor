from utils import functions

# Printing Rules
rules = "Enter R for Rock, P for Paper and S for Scissor. Enjoy!"
print(rules)

# Prevent entry of int or float
try:
    player = input("Enter choice: ").upper()
except:
    print("Check your entry.")
    quit()

# Check if entry is either R, P or S
if not functions.verified(player):
    print("Check your entry.")
    exit()

computer = functions.computer()

print(functions.compare(player, computer))
