# This encapsulates logging of game information.
# It may be more fleshed out later.

def game_log(text):
    global log
    # Create the log if it does not exist
    try:
        log
    except NameError:
        log = []
    log.append(text)

def get_game_log_html():
    return '<br>'.join(log)
