from engine.instance import Game

class Entity:
    def __init__(self):
        self.game = Game()
        self.model = None
        
    def pre_load(self):
        ...
        
    def create(self):
        ...
        
    def update(self, dt):
        ...
        
    def destroy(self):
        if self.model is not None: 
            self.model.cleanup()
            self.model.remove_node()