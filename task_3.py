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
