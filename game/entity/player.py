from engine.entity import Entity
from engine.instance import Game
from direct.actor.Actor import Actor

class Player(Entity):
    def __init__(self):
        super().__init__()
    
    def pre_load(self):
        self.model = Actor("assets/player/player", {
            "idle": "assets/player/player-idle"
        })
        self.model.setHpr(180, 0, 0)
        self.model.reparentTo(self.game.render)
        self.model.loop("idle")
        
    def create(self):
        ...
        
    def update(self, dt):
        ...