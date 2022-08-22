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
        break

    # for each round, round number incremnts by 1
    round_num += 1