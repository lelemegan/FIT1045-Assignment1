playersss = [{'name': 'Player 1', 'score': 20, 'stayed': False, 'at_14': True, 'bust': False},
           {'name': 'Player 2', 'score': 17, 'stayed': True, 'at_14': True, 'bust': False},
           {'name': 'Player 3', 'score': 19, 'stayed': True, 'at_14': True, 'bust': False},
           {'name': 'Player 4', 'score': 19, 'stayed': True, 'at_14': True, 'bust': False}]

def end_of_game(players):
    """
    Takes the list of all players and determines if the game has finished,
    returning false if not else printing the result before returning true.

    Arguments:
    - players: A list of player-dictionary objects

    Returns True if round has ended or False if not. If true results are
    printed before return.
    """
    #raise NotImplementedError
    #one winner
    #Player 1 is the winner

    #draw

    #bust
    stayed_and_not_busted = []
    who_busted = []
    for x in players:
        if x["stayed"] == True: #if anyone decides to stay, return True 
            return True
        elif x["bust"] == False: #if anyone decides not to stay and is not busted, store score into list
            stayed_and_not_busted.append(x["score"])
        elif x["bust"] == True:
            who_busted.append(x["name"])

    highest_score = max(stayed_and_not_busted)
    who_has_highest_score = []
    for x in stayed_and_not_busted:
        if x["score"] == highest_score:
            who_has_highest_score.append(x["name"])
    
    if len(who_has_highest_score)==1:
        print(who_has_highest_score[0]+"is the winner!")
        return True
    elif len(who_has_highest_score)>1:
        print("The game is a draw! No one wins :(")
        return True
    elif len(who_busted)==len(players):
        print("The game is a draw! No one wins :(")
        return True

    return False

end_of_game(playersss)