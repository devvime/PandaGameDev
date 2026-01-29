from engine.instance import Game

class Scene:
    def __init__(self):
        self.game = Game()
        self.loaded = False
        self.objects = {}
        
    def pre_load(self):
        for obj in self.objects:
            if self.objects[obj].pre_load:
                self.objects[obj].pre_load()

    def create(self):
        for obj in self.objects:
            if self.objects[obj].create:
                self.objects[obj].create()

    def update(self, dt):
        for obj in self.objects:
            if self.objects[obj].update:
                self.objects[obj].update(dt)

    def destroy(self):
        for obj in self.objects:
            self.objects[obj].destroy()