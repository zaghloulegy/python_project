import random

def play():
    user = input(" what is your choice? 'r' for rock, 'p' for paper, 's' for scissors")
    computer = random.choice(['r', 'p', 's'])


    if user == computer:
        return 'tie'

    if is_win(user, computer):
        return 'you won'
    return 'you lost'

def is_win(player, opponent):
    if (player == 'r' and opponent == 'o') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'rock'):
        return True


print(play())