from engine.scene import Scene
from game.gui.menu.main_menu import MainMenu

class MainScene(Scene):
    def __init__(self):
        super().__init__()
        
        self.objects["main_menu"] = MainMenu()
        
    def pre_load(self):
        return super().pre_load()
        
    def create(self):
        return super().create()        
        
    def update(self, dt):
        return super().update(dt)
        
    def destroy(self):
        return super().destroy()