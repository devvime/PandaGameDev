game = None

def set_instance_game(instance):
    global game
    game = instance
    
def Game():
    return game