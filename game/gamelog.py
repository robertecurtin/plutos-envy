# This encapsulates logging of game information.
# It may be more fleshed out later.
log = [] 

def game_log(text):
    log.append(text)

def get_game_log_html():
    return '<br>'.join(log)
