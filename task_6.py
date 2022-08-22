def multiplayer_game(num_of_players):
  """
  This function defines a game loop for a local multiplayer game of Twenty One, 
  where each iteration of the while loop is a round within the game. 
  """
  
  round_num = 0
  player_template = {
    'name': '',
    'score': 0,
    'stayed': False,
    'at_14': False,
    'bust': False
  }

  #generate players
  players = {}
  for i in range(1, num_of_players+1):
    player = dict(player_template)
    new_name = f"Player {i}"
    player["name"] = new_name
    players[new_name] = player
  
  # game loop
  while True:
    display_round_stats(round_num, players)
    # each loop, every player will get a turn except "stayed" and "busted"
    for player_name in players.keys():
      player = players[player_name]

      # skip the player's turn if they are true for "bust" or "stayed"
      if (player["bust"] or player["stayed"]):
        continue
      
      display_game_options(player)
      game_options = [1,2]
      if (player["at_14"]):
        game_options.append(3)
      option = int_input("Please enter an option: ", restricted_to=game_options)
      player = execute_turn(player, option)
      
      

    round_num += 1