import random

def dice_roll_game(player_name):
    # Roll dice for the player and the computer
    player_roll = random.randint(1, 6)
    computer_roll = random.randint(1, 6)

    # Determine the winner
    if player_roll > computer_roll:
        winner = f"{player_name} wins! (Player: {player_roll}, Computer: {computer_roll})"
    elif player_roll < computer_roll:
        winner = f"Computer wins! (Player: {player_roll}, Computer: {computer_roll})"
    else:
        winner = f"It's a tie! (Player: {player_roll}, Computer: {computer_roll})"

    return winner

# Let's test the game with the player name "საბა"
dice_roll_game("საბა")
