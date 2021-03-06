from game_class import Game
from player_class import RandomPlayer
from player_class import CustomPlayer
players = [CustomPlayer(), CustomPlayer()]
game = Game(players)
game.state['players']
{
    1: {
        'scout_coords': (4, 1),
        'home_colony_coords': (4, 1)
    },
    2: {
        'scout_coords': (4, 7),
        'home_colony_coords': (4, 7)
    }
}

game.complete_movement_phase()
assert game.state['players'] == {
    1: {
        'scout_coords': (4, 2),
        'home_colony_coords': (4, 1)
    },
    2: {
        'scout_coords': (4, 6),
        'home_colony_coords': (4, 7)
    }
}

assert game.complete_combat_phase() == 'Nothing changes since no units occupy the same location'

game.complete_movement_phase()
assert game.state['players'] == {
    1: {
        'scout_coords': (4, 3),
        'home_colony_coords': (4, 1)
    },
    2: {
        'scout_coords': (4, 5),
        'home_colony_coords': (4, 7)
    }
}

assert game.complete_combat_phase() == 'Nothing changes since no units occupy the same location'

game.complete_movement_phase()
assert game.state['players'] == {
    1: {
        'scout_coords': (4, 4),
        'home_colony_coords': (4, 1)
    },
    2: {
        'scout_coords': (4, 4),
        'home_colony_coords': (4, 7)
    }
}

game.complete_combat_phase()

assert game.state['players'] == {
    1: {
        'scout_coords': None,
        'home_colony_coords': (4, 1)
    },
    2: {
        'scout_coords': (4, 4),
        'home_colony_coords': (4, 7)
    }
} or {
    1: {
        'scout_coords': (4, 4),
        'home_colony_coords': (4, 1)
    },
    2: {
        'scout_coords': None,
        'home_colony_coords': (4, 7)
    }
}


num_wins = {1: 0, 2: 0}
for _ in range(200):
        players = [CustomPlayer(), CustomPlayer()]
        game = Game(players)
        game.run_to_completion()
        winner = game.state['winner']
        num_wins[winner] += 1
print(num_wins)