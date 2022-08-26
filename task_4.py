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
