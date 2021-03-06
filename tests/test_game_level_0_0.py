from game_class import Game
from player_class import RandomPlayer
from player_class import CustomPlayer
players = [RandomPlayer(), CustomPlayer()]
game = Game(players)
game.state
{
    'turn': 1,
    'board_size': [7,7],
    'players': {
        1: {
            'scout_coords': (4, 1),
            'home_colony_coords': (4, 1)
        },
        2: {
            'scout_coords': (4, 7),
            'home_colony_coords': (4, 7)
        }
    },
    'winner': None
}

game.complete_turn()
print(game.state)
'''{
    'turn': 2,
    'board_size': [7,7],
    'players': {
        1: {
            'scout_coords': (will vary),
            'home_colony_coords': (4, 1)
        },
        2: {
            'scout_coords': (4, 6),
            'home_colony_coords': (4, 7)
        }
    },
    'winner': None
}
'''
game.run_to_completion()
print(game.state)
{
    'turn': 7,
    'board_size': [7,7],
    'players': {
        1: {
            'scout_coords': (10),
            'home_colony_coords': (4, 1)
        },
        2: {
            'scout_coords': (4, 1),
            'home_colony_coords': (4, 7)
        }
    },
    'winner': 2
}