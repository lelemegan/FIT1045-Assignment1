"""
Group name:
Authors:
"""

import time
import random

def display_rules():
  print("""
  _____________________________________________________________________________
  Twenty One is a game of chance where players take turns rolling two dice every 
  round until they decide to stop rolling and lock in their score or end up 
  going bust with a total over 21. The objective is to be the closest to 21 
  when everyone is done rolling.

  Rules are as per follows:
    - Players begin with a score of 0.
    - Each player has one turn to either roll or stop rolling each round.
    - Players can only do a regular roll of two dice until they 
      reach a score of at least 14.
    - Players with a score >= 14 have the option to only roll one dice.
    - If a player scores more than 21 they go bust and are out of the game.
    - The winning player is the one with the score closest to 21 when everyone 
      has finished rolling.
    - If all players go bust, no one wins.
    - If more than one player has the winning score, no one wins.
  _____________________________________________________________________________
  """)

  input("Press enter to go back")
  return


def display_main_menu():
    print("------------Main Menu------------")
    print("Welcome to Twenty One!")
    print("1. Solo")
    print("2. Local Multiplayer")
    print("3. Rules")
    print("4. Exit")
    print("---------------------------------")


def int_input(prompt="", restricted_to=None):
  """
  Helper function that modifies the regular input method,
  and keeps asking for input until a valid one is entered. Input 
  can also be restricted to a set of integers.

  Arguments:
    - prompt: String representing the message to display for input
    - restricted: List of integers for when the input must be restricted
                  to a certain set of numbers

  Returns the input in integer type.
  """
  while True:
    player_input = input(prompt)
    try:
      int_player_input = int(player_input)
    except ValueError:
      continue
    if restricted_to is None:
      break
    elif int_player_input in restricted_to:
      break

  return int_player_input


def cpu_player_choice(score):
  """
  This function simply returns a choice for the CPU player based
  on their score.

  Arguments:
    - score: Int

  Returns an int representing a choice from 1, 2 or 3.
  """
  time.sleep(2)
  if score < 14:
    return 1
  elif score < 17:
    return 3
  else:
    return 2


def display_game_options(player):
    """
    Prints the game options depending on if a player's score is
    >= 14.
    
    Arguments:
        - player: A player dictionary object
    """
    name = player['name']
    score = player['score']
    print('---------', name, '\'s turn', '-----------')
    print(name, '\'s score:', score)
    print('1.Roll')
    print('2.Stay')
    if score >= 14:
        print('3.Roll One')
    return True



def display_round_stats(round, players):
    """
    Print the round statistics provided a list of players.

    Arguments:
        - round: Integer for round number
        - players: A list of player-dictionary objects
    """
    round+=1
    print('---------Round', round, '-----------')
    for player in players:
        print(player['name'], 'is at', player['score'])

    round = 0

    player_1 = {'name': 'Player 1', 'score': 16, 'stayed': False, 'at_14': True, 'bust': False}
    if display_game_options(player_1):
         round += 1

    player_2 = {'name': 'player 2', 'score': 100, 'stayed': False, 'at_14': False, 'bust': False}
    if display_game_options(player_2):
        round += 1

    player_3 = {'name': 'Player 3', 'score': 11, 'stayed': False, 'at_14': False, 'bust': False}
    if display_game_options(player_3):
        round += 1

    players = [player_1, player_2,player_3]
    display_round_stats(round, players)


def roll_dice(num_of_dice):
  """
  Rolls dice based on num_of_dice passed as an argument.

  Arguments:
    - num_of_dice: Integer for amount of dice to roll

  Returns the following tuple: (rolls, display_string)
    - rolls: A list of each roll result as an int
    - display_string: A string combining the dice art for all rolls into one string
  """
  # Pick random number form the die
  
  roll_results = []
  for i in range(num_of_dice):
    roll = random.randint(1, 6)
    roll_results.append(roll)

  # Generate the Diagram of Dice Faces
  die_art = {
      1: ["┌─────────┐", "│         │", "│    ●    │", "│         │", "└─────────┘"],
      2: ["┌─────────┐", "│  ●      │", "│         │", "│      ●  │", "└─────────┘"],
      3: ["┌─────────┐", "│  ●      │", "│    ●    │", "│      ●  │", "└─────────┘"],
      4: ["┌─────────┐", "│  ●   ●  │", "│         │", "│  ●   ●  │", "└─────────┘"],
      5: ["┌─────────┐", "│  ●   ●  │", "│    ●    │", "│  ●   ●  │", "└─────────┘"],
      6: ["┌─────────┐", "│  ●   ●  │", "│  ●   ●  │", "│  ●   ●  │", "└─────────┘"]
    }
  dice_row = []
  dice_row_to_str =''
  show_dice_face = ''
  # Go thought each row of dice
  for row_of_dice in range(5):
      temporary_storage = []
      # Go thought each dice
      for number_of_dice in range(len(roll_results)):
          x = roll_results[number_of_dice]
          temporary_storage.append(die_art[x][row_of_dice])
      # Combine same row for all dice
      dice_row_to_str = ' '.join(temporary_storage)
      dice_row.append(dice_row_to_str)
  # Combin final result
  show_dice_face = '\n'.join(dice_row)
  #print(show_dice_face)
  return show_dice_face, roll_results


def execute_turn(player, player_input):
  """
  Executes one turn of the round for a given player.

  Arguments:
    - player: A player dictionary object

  Returns an updated player dictionary object.
  """
  raise NotImplementedError


def end_of_game(players):
  """
  Takes the list of all players and determines if the game has finished,
  returning false if not else printing the result before returning true.

  Arguments:
    - players: A list of player-dictionary objects

  Returns True if round has ended or False if not. If true results are
  printed before return.
  """
  raise NotImplementedError


def solo_game():
  """
  This function defines a game loop for a solo game of Twenty One against 
  AI.
  """
  


def multiplayer_game(num_of_players):
  """
  This function defines a game loop for a local multiplayer game of Twenty One, 
  where each iteration of the while loop is a round within the game. 
  """
  raise NotImplementedError
      

def main():
    """
    Defines the main loop that allows the player to start a game, view rules or quit.
    """
    score = 0
    score_p = 0
    skip_C = False
    skip_P = False
    # Code will opreater until CPU score bigger than 21
    while score < 21:
        # If CPU choice roll dice
        if skip_C == False:
            cpu_returen = cpu_player_choice(score)
            # Roll two dice
            if cpu_returen == 1:
                num_of_dice = 2
                roll_results = roll_dice(num_of_dice)
                print(roll_results[0])
                score += sum(roll_results[1])
                print("Computer score",score)
            # Roll one dice
            elif cpu_returen == 3:
                num_of_dice = 1
                roll_results = roll_dice(num_of_dice)
                print(roll_results[0])
                score += sum(roll_results[1])
                print("Computer score",score)
            # Skip
            else:
                print('Skip')
                skip_C =  True
                continue
        # Play choice roll dice
        if skip_P == False:
            # Player input
            num_of_dice_p = int(input("Please enter the number of dice: "))
            # Player choice skip
            if num_of_dice_p > 2:
                skip_P = True
                continue
            # Roll dice returen score
            roll_results_p = roll_dice(num_of_dice_p)
            print(roll_results_p[0])
            score_p += sum(roll_results_p[1])
            # Play lose
            if score_p > 21:
                skip_P = True
                print("CPU win!!")
                break
            # once at 21 can not roll again
            elif score_p == 21:
                skip_P = True
            print("Player score", score_p)
        # If both skip end game
        if skip_P == True & skip_C == True:
            if score > score_p:
                print("CPU win!!")
                break
            elif score == score_p:
                print("Draw")
            else:
                print("You win")
                break

main()
