from engine.scene import Scene
from game.entity.player import Player

class GameScene(Scene):
    def __init__(self):
        super().__init__()
        self.game.accept('f1', self.return_to_main_menu)
        
    def pre_load(self):
        self.objects["player"] = Player()
        return super().pre_load()
        
    def create(self):
        self.game.camera.setPos(0, -5, 1)
        return super().create()        
        
    def update(self, dt):
        return super().update(dt)
        
    def destroy(self):
        return super().destroy()
    
    def return_to_main_menu(self):
        self.game.set_scene("main")