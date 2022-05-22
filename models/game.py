def get_winner(player_1, player_2):
    if player_1 == player_2:
        return "It's a draw!"

    elif player_1 == "rock" and player_2 == "scissors":
        return "Player 1 wins!"    

    elif player_1 == "paper" and player_2 == "rock":
        return "Player 1 wins!"

    elif player_1 == "scissors" and player_2 == "paper":
        return "Player 1 wins!"  

    else:
        return "Player 2 Wins!"