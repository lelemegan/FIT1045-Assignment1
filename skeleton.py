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
    name = player['name']
    score = player['score']
    print('---------', name, '\'s turn', '-----------')
    print(name, '\'s score:', score)
    print('1.Roll')
    print('2.Stay')
    if score >= 14:
        print('3.Roll One')
    return True


def display_round_stats(round,players):
    round+=1
    print('---------Round', round, '-----------')
    for player in players:	
        print(player['name'], 'is at', player['score'])


def roll_dice(num_of_dice=1):
  """
  Pick random numbers based on the number of dice being inputted

  Arguments:
    - num_of_dice: Accepts int. This is the number of dice to be rolled.

  Return Value:
    - A list of 2 elements, 
      - roll result as a list of integer in position 0, 
      - Ascii art for dice face in string in position 1

  Implemented by:
    - Jinwei Liang 30741424
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


  return [roll_results, show_dice_face]


def execute_turn(player, player_input):
  """
  Executes one turn of the round for a given player. Maintain player object to be synced (For example: score attribute and at_14 or bust attribute to be synced)

  Arguments:
    - player: A player dictionary object. Player data before executing the turn.
    - player_input: A player dictionary object. Player data before executing the turn.

  Return Value:
    - A player dictionary object. An updated player dictionary object.

  Implemented by:
    - Xuanao Zhao 33332835
  """
  
  # Define message for different player input
  messages = {
    1: "Rolling both...",
    2: "{name} has stayed with a score of {score}",
    3: "Rolling one...",
  }

  # Gets the respective message string from messages with the index the same as player input.
  # Formats the string with required information.
  message = messages[player_input].format(name=player["name"], score=player["score"])

  # Display message using print
  print(message)

  # Check if the player choose to skip (Choice #2). If no, skip to the next step.
  if player_input == 2:
    # Generate updated player to have stayed to "True"
    updated_player = dict(player) # get a new object with same values by using the dict constructor
    updated_player["stayed"] = True
    
    # Return the updated player
    return updated_player

  # Determins the amount of dice to be rolled.
  # Roll 2 times if player chooses 1, or else 1 time
  # Using short hand if
  dice_amount = 2 if player_input == 1 else 1

  # Roll dice(s)
  dice_result = roll_dice(num_of_dice=dice_amount)

  # Display dice result
  print(dice_result[1])

  # Get sum of dice result
  dice_sum = sum(dice_result[0])

  # Generate updated player
  updated_player = dict(player) # get a new object with same values by using the dict constructor
  updated_player["score"] += dice_sum
  updated_player["at_14"] = updated_player["score"] >= 14
  updated_player["bust"] = updated_player["score"] > 21

  # Display player status (and respective message if bust)
  print("{name} is now on {score}".format(name=updated_player["name"], score=updated_player["score"]))
  if updated_player["bust"]:
    print("{name} goes bust!".format(name=updated_player["name"]))

  # Return the updated player dict object
  return updated_player


def end_of_game(players):
  """
  Takes the list of all players and determines if the game has finished,
  returning false if not else printing the result before returning true.

  Arguments:
    - players: A list of player-dictionary objects

  Returns True if round has ended or False if not. If true results are
  printed before return.
  """
  for i in players:
    if (not i["stayed"]) and (not i["bust"]):
        return True
  return False


def solo_game():
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
                print(roll_results[1])
                score += sum(roll_results[0])
                print("Computer score",score)
            # Roll one dice
            elif cpu_returen == 3:
                num_of_dice = 1
                roll_results = roll_dice(num_of_dice)
                print(roll_results[1])
                score += sum(roll_results[0])
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
            print(roll_results_p[1])
            score_p += sum(roll_results_p[0])
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
  solo_game()


main()



