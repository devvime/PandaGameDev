from engine.instance import Game

class GUI:
    def __init__(self):
        self.game = Game()
        self.objects = {}

    def pre_load(self):
        ...

    def create(self):
        ...

    def update(self, dt):
        ...

    def destroy(self):
        for obj in self.objects:
            self.objects[obj].destroy()