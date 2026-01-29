from engine.gui import GUI
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectGui import DirectButton

class MainMenu(GUI):
    def __init__(self):
        super().__init__()

    def pre_load(self):
        return super().pre_load()

    def create(self):
        self.objects["title"] = OnscreenText(text='Panda Game Framework', pos=(0, 0.2), scale=0.07, fg=(1, 1, 1, 1))
        self.objects['start_button'] = DirectButton(
            text="Start game", scale=0.1, pos=(0, 0, 0.05), command=self.start_game
        )
        self.objects['exit_button'] = DirectButton(
            text="Exit", scale=0.1, pos=(0, 0, -0.13), command=self.exit_game
        )
        
        return super().create()

    def update(self, dt):        
        return super().update(dt)
    
    def start_game(self):
        self.game.set_scene("gameplay")
        
    def exit_game(self):
        self.game.userExit()
