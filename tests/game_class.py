import random 
import math
class Game:
    def __init__(self, players, board_size=[7,7]):
        self.players = players
        self.set_player_numbers()

        board_x, board_y = board_size
        mid_x = (board_x + 1) // 2
        mid_y = (board_y + 1) // 2

        self.state = {
            'turn': 1,
            'board_size': board_size,
            'players': {
                1: {
                    'scout_coords': (mid_x, 1),
                    'home_colony_coords': (mid_x, 1)
                },
                2: {
                    'scout_coords': (mid_x, board_y),
                    'home_colony_coords': (mid_x, board_y)
                }
            },
            'winner': None
        }

    def set_player_numbers(self):
        for i, player in enumerate(self.players):
            player.set_player_number(i+1)

    def check_if_coords_are_in_bounds(self, coords):
        x, y = coords
        board_x, board_y = self.state['board_size']
        if 1 <= x and x <= board_x:
            if 1 <= y and y <= board_y:
                return True
        return False

    def check_if_translation_is_in_bounds(self, coords, translation):
        max_x, max_y = self.state['board_size']
        x, y = coords
        dx, dy = translation
        new_coords = (x+dx,y+dy)
        return self.check_if_coords_are_in_bounds(new_coords)

    def get_in_bounds_translations(self, coords):
        translations = [(0,0), (0,1), (0,-1), (1,0), (-1,0)]
        in_bounds_translations = []
        for translation in translations:
            if self.check_if_translation_is_in_bounds(coords, translation):
                in_bounds_translations.append(translation)
        return in_bounds_translations

    def complete_movement_phase(self):
        
        for player in self.players:
          #find in bound translations

          coords = self.state['players'][player.player_number]['scout_coords']
          if coords != None:
            in_bounds_translations = self.get_in_bounds_translations(coords)

            best_choice = player.choose_translation(self.state, in_bounds_translations)

            scout_coord_x = self.state['players'][player.player_number]['scout_coords'][0]

            scout_coord_y = self.state['players'][player.player_number]['scout_coords'][1]

            new_x = scout_coord_x + best_choice[0]
            new_y = scout_coord_y + best_choice[1]
         
            self.state['players'][player.player_number]['scout_coords'] = (new_x, new_y)
        
        self.state['turn'] += 1


    def complete_combat_phase(self):
      if self.state['players'][1]['scout_coords'] == self.state['players'][2]['scout_coords']:
        losser = random.randint(1,2)
        self.state['players'][losser]['scout_coords'] = None
      else:
        return 'Nothing changes since no units occupy the same location'



    def run_to_completion(self):

        while self.state['winner'] == None:
          self.complete_movement_phase()
          self.complete_combat_phase()
          for player in self.players:
            for opposing_player in self.players:
              if player.player_number != opposing_player.player_number:
                player_scout = self.state['players'][player.player_number]['scout_coords']
                opposing_base = self.state['players'][opposing_player.player_number]['home_colony_coords']
                if player_scout == opposing_base:
                  if self.state['winner'] != None:
                    self.state['winner'] = 'Tie'
                  else:
                    self.state['winner'] = player.player_number

        # YOUR CODE HERE
        # complete turns until there is a winner

    # you can add more helper methods if you want
