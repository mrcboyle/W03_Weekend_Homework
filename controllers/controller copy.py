from app import app
# from flask import render_template
from models.game import get_winner
# from models.player import Player

@app.route('/')
def index():
    return "Lets play Rock, Paper, Scissors!"

@app.route("/<player_1>/<player_2>")
def play_game(player_1, player_2):
    return get_winner(player_1, player_2)
