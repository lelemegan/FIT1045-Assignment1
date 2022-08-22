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