team_name = 'Team better than you' 
strategy_name = 'backstab'
strategy_description = 'betrays the last turn'


def move(my_history, their_history, my_score, their_score):
    if len(my_history)==0:
        return 'c'
    elif ('b' in their_history) or len(my_history)==99:
        return 'b' 
    else:
        return 'c' 
