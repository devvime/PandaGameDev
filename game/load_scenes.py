from game.scenes.main_scene import MainScene
from game.scenes.game_scene import GameScene

def load_scenes():
    return {
        "main": MainScene(),
        "gameplay": GameScene()
    }