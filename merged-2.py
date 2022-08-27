"""
Group name: F4
Authors: 
    - Xuanao Zhao 33332835
    - Tiong Le Megan 33332053
    - Jinwei Liang 30741424
    - Xinrong Cai 33048118

The function body of the following function 

 - "display_game_options"
 - "display_round_stats" 
 - "roll_dice"
 - "execute_turn"
 - "end_of_game"
 - "solo_game"
 - "multiplayer_game"
 - "main"

has the following license applied:

 Copyright (c) 2022 Xuanao Zhao, Tiong Le Megam, Jinwei Liang, Xinrong Cai

 Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

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
  The purpose of the function is to define the value of player dictionery
  
  Argument:
    - name is equal to the name value in player dictionary
    - score is equal to the score value in play dictionary

  Return value:
    - System will return Roll one if player score is equal or greater than 14
    - System will return stay if play score is less than 14

  Implemented by Xinrong Cai 33048118
  """

  # The purpose of the function is to define the value of player dictionary.
  name = player['name']
  score = player['score']
  turn='\'s turn'
  a=str('---------')+str(name)+str(turn)+str('---------') # Print dashed lines as required by task instruction
  print(a)
  print('1.Roll')
  print('2.Stay')
  if score >= 14: # The purpose of this function is to check the score value in each player dictionery.
    print('3.Roll One') # If player score value is equal or greater than 14, player has an option of "Roll one".
  return True


def display_round_stats(round,players):
    """
    The purpose of the function is to count the number of rounds for each player

    Argument:
     - Round initially starts with 0
     - round+=1 indicates that the times of round will increase by 1 if player's player dictionary is identified

    Return:
     - It will return player name and player score.

    Implemented by Xinrong Cai 33048118
    """

    b='---------round'
    c=str(round)+str('---------')
    print(b,c) # Print line17 and line18 at the same line
    for player in players:
        print(player['name'], 'is at', player['score']) # Print player name and player's score value in player dictionery.


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
    dice_row_to_str = ''.join(temporary_storage)
    dice_row.append(dice_row_to_str)
  # Combin final result
  if row_of_dice == 4:
    show_dice_face = '\n'.join(dice_row) + '\n'
  else:
    show_dice_face = '\n'.join(dice_row)

  return [roll_results,show_dice_face]


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

    Returns Value:
        - Boolean
          True if round has ended or False if not. If true results are
          printed before return.

    Implemented by:
        - Tiong Le Megan 33332053
    """

    stayed_and_not_busted = []
    who_busted = []
    for x in players:
        #if anyone decides not to stay(continue playing)
        #and this person is not busted
        #return False (not end of game yet) 
        if x["stayed"] == False and x["bust"] == False: 
            return False
        #if anyone decides to stay and is not busted
        #store the score into list
        elif x["stayed"] == True and x["bust"] == False: #if anyone decides not to stay and is not busted, store score into list
            stayed_and_not_busted.append(x["score"])
        elif x["bust"] == True:
            who_busted.append(x["name"])

    if len(who_busted)==len(players):
        print("The game is a draw! No one wins :(")
        return True

    highest_score = max(stayed_and_not_busted)
    who_has_highest_score = []
    for x in players:
        if x["score"] == highest_score:
            who_has_highest_score.append(x["name"])
    
    no_of_highest_score_players = len(who_has_highest_score)
    if no_of_highest_score_players==1:
        print(who_has_highest_score[0]+" is the winner!")
        return True
    elif no_of_highest_score_players>1:
        print("The game is a draw! No one wins :(")
        return True

    return False


def solo_game():
    """
    This function defines a game loop for a solo game of Twenty One against 
    AI.

    Arguments:
        - None

    Return Value:
        - None

    Implemented by:
        - Jinwei Liang 30741424
    """
    # define the round number and initalize it to 0
    round = 0
    # define a template player to generate players
    player_list = [ 
        {'name': 'Player 1', 'score': 0, 'stayed': False,'at_14': False, 'bust': False},
        {'name': 'CPU Player', 'score': 0, 'stayed': False,'at_14': False, 'bust': False}
    ]
    # Code will opreater until CPU score bigger than 21
    while True:
        # Show the information of players
        display_round_stats(round,player_list)
        # Player roll dice
        if player_list[0]['stayed'] == False:
            # display play game options
            display_game_options(player_list[0])
            # Roll dice and update to dictionary
            if  player_list[0]['at_14'] == True:
                num_op = [1,2,3]
            else:
              num_op = [1,2]
            player_list[0] = execute_turn(player_list[0], int_input('Please enter an option: ',num_op))

        # CPU roll dice
        if player_list[1]['stayed'] == False:
            # display play game options
            display_game_options(player_list[1])
            # Roll dice and update to dictionary
            player_list[1] = execute_turn(player_list[1], cpu_player_choice(player_list[1]['score']))


        # test if it is end of game
        if end_of_game(player_list) == True:
            break
        # if not go next round
        round += 1 


def multiplayer_game(num_of_players):
  """
  This function defines a game loop for a local multiplayer game of Twenty One, 
  where each iteration of the while loop is a round within the game.

  Arguments:
    - num_of_players: accepts an integer. Represent the number of players.

  Return Value:
    - None

  Implemented by:
    - Xuanao Zhao 33332835
  """
  
  # define the round number and initalize it to 0
  round_num = 0
  # define a template player to generate players
  player_template = {
    'name': '',
    'score': 0,
    'stayed': False,
    'at_14': False,
    'bust': False
  }

  # generate players
  players = {} # this dict contains a list of players with it's name being the key
  for i in range(1, num_of_players+1):
    # create a new dict object based on the template
    player = dict(player_template)
    # update the player name and store them into the players dict
    new_name = f"Player {i}"
    player["name"] = new_name
    players[new_name] = player
  
  # game loop
  while True:
    display_round_stats(round_num, list(players.values()))
    # each loop, every player will get a turn except "stayed" and "busted"
    for player_name in players.keys():
      # get the player
      player = players[player_name]

      # skip the player's turn if they are true for "bust" or "stayed"
      if (player["bust"] or player["stayed"]):
        continue
      
      # display the game options for a player
      display_game_options(player)

      # define a list of acceptable options
      game_options = [1,2]
      # append option 3 to the acceptable options
      if (player["at_14"]):
        game_options.append(3)
      
      # get user input for options
      option = int_input("Please enter an option: ", restricted_to=game_options)

      # display and update the player object after executing each turn
      players[player["name"]] = execute_turn(player, option)
      
      # check for "end-of-gae", prints who won or draw if EOG
      if (end_of_game(list(players.values()))):
        return

    # for each round, round number incremnts by 1
    round_num += 1


def main():
  """
  Defines the main loop that allows the player to start a game, view rules or quit.

  Implemented by:
   - Xinrong Cai 33048118
   - Xuanao Zhao 33332835
  """

  while True:
    # dipslay main menu until game ends
    display_main_menu()
    input_value = int_input("Please select a choice: ", restricted_to=[1,2,3,4])
    if input_value == 2:
      # if user choose local multiplayer, prompt for user count
      player_count = int_input("Please enter the number of players (Enter -1 to go back): ")
      # if negative number, go back to main menu
      if (player_count < 0):
        continue
      # run multiplayer game loop if not negative number
      multiplayer_game(player_count)
      # end game after game is complete
      return
    elif input_value == 1:
      # if user choose solo game, run solo_game game loop
      solo_game()
      # end game after game is complete
      return
    elif input_value == 3:
      display_rules()
      # do not end game if user choose to display rules
    else:
      # if user chooses exit, exit main loop
      return

main()