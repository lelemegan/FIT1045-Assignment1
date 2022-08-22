"""
Group name: F4
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
  raise NotImplementedError


def display_round_stats(round, players):
  """
  Print the round statistics provided a list of players.

  Arguments:
    - round: Integer for round number
    - players: A list of player-dictionary objects
  """
  raise NotImplementedError


def roll_dice(num_of_dice=1):
  """
  Rolls dice based on num_of_dice passed as an argument.

  Arguments:
    - num_of_dice: Integer for amount of dice to roll

  Returns the following tuple: (rolls, display_string)
    - rolls: A list of each roll result as an int
    - display_string: A string combining the dice art for all rolls into one string
  """
  die_art = {
    1: ["┌─────────┐", "│         │", "│    ●    │", "│         │", "└─────────┘"],
    2: ["┌─────────┐", "│  ●      │", "│         │", "│      ●  │", "└─────────┘"],
    3: ["┌─────────┐", "│  ●      │", "│    ●    │", "│      ●  │", "└─────────┘"],
    4: ["┌─────────┐", "│  ●   ●  │", "│         │", "│  ●   ●  │", "└─────────┘"],
    5: ["┌─────────┐", "│  ●   ●  │", "│    ●    │", "│  ●   ●  │", "└─────────┘"],
    6: ["┌─────────┐", "│  ●   ●  │", "│  ●   ●  │", "│  ●   ●  │", "└─────────┘"]
  }

  raise NotImplementedError


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
  raise NotImplementedError


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
  raise NotImplementedError


main()



