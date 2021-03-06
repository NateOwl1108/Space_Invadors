
from random import random
import math

class RandomPlayer():
    def __init__(self):
        self.player_number = None

    def set_player_number(self, n):
        self.player_number = n

    def choose_translation(self, game_state, choices):
        # `choices` is a list of possible translations,
        # e.g. [(0,0), (-1,0), (0,1)] if the player's
        # scout is in the bottom-right corner of the board

        random_idx = math.floor(len(choices) * random())
        return choices[random_idx]

class CustomPlayer():
    def __init__(self):
        self.player_number = None

    def set_player_number(self, n):
        self.player_number = n

    def get_opponent_player_number(self):
        if self.player_number == None:
            return None
        elif self.player_number == 1:
            return 2
        elif self.player_number == 2:
            return 1

    def choose_translation(self, game_state, choices):
        # `choices` is a list of possible translations,
        # e.g. [(0,0), (-1,0), (0,1)] if the player's
        # scout is in the bottom-right corner of the board

        myself = game_state['players'][self.player_number]
        opponent_player_number = self.get_opponent_player_number()
        opponent = game_state['players'][opponent_player_number]

        my_scout_coords = myself['scout_coords']
        opponent_home_colony_coords = opponent['home_colony_coords']

        # FOR YOU TO DO:
        # you need to use `my_scout_coords` and
        # `opponent_home_colony_coords` to return the
        # translation that will bring you closest to
        # the opponent
        shortest_distance = 99999
        best_choice = (99,99)
        for choice in choices:
          distance = ((opponent_home_colony_coords[0]-(my_scout_coords[0] + choice[0]))**2 +    (opponent_home_colony_coords[1] - (my_scout_coords[1] + choice[1]))**2)**0.5
          if distance < shortest_distance:
            best_choice = choice
            shortest_distance = distance
        return best_choice

        