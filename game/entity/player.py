from engine.instance import Game
from direct.actor.Actor import Actor

class Player:
    def __init__(self):
        self.game = Game()
    
    def pre_load(self):
        self.model = Actor("assets/player/player")
        self.model.setHpr(180, 0, 0)
        self.model.reparentTo(self.game.render)
        
    def create(self):
        ...
        
    def update(self, dt):
        ...
        
    def destroy(self):
        self.model.remove_node()