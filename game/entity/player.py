from engine.instance import Game
from direct.actor.Actor import Actor

class Player:
    def __init__(self):
        self.game = Game()
    
    def pre_load(self):
        self.model = Actor(
            "models/panda-model",
            { "walk": "models/panda-walk4" }
        )
        self.model.setScale(0.005, 0.005, 0.005)
        self.model.reparentTo(self.game.render)
        self.model.loop("walk")
        
    def create(self):
        ...
        
    def update(self, dt):
        ...
        
    def destroy(self):
        self.model.remove_node()