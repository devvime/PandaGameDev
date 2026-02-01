from engine.entity import Entity
from direct.actor.Actor import Actor
from panda3d.core import KeyboardButton

class Player(Entity):
    def __init__(self):
        super().__init__()
    
    def pre_load(self):
        self.model = Actor("assets/player/player", {
            "idle": "assets/player/player-idle",
            "walk": "assets/player/player-walk",
            "run": "assets/player/player-run",
            "fall": "assets/player/player-fall"
        })
        self.model.setShaderOff()
        self.model.setHpr(180, 0, 0)
        self.model.setScale(0.5, 0.5, 0.5)
        self.model.reparentTo(self.game.render)
        
        self.current_anim = None
        self.model.loop("idle")
        self.current_anim = "idle"
        
        self.camera_pivot = self.model.attachNewNode("camera_pivot")
        self.camera_pivot.setPos(0, 0, 0)
        self.game.cam.setPos(-0.997,5.87, 4.45)
        self.game.cam.setHpr(171, -10.5, 0)
        self.game.cam.reparentTo(self.camera_pivot)
        
        env = self.game.loader.load_model("models/environment")
        env.setScale(0.5,0.5,0.5)
        env.reparentTo(self.game.render)
        
    def create(self):
        ...
        
    def update(self, dt):
        self.movement(dt)
        
    def movement(self, dt):
        is_down = self.game.mouseWatcherNode.isButtonDown
        
        speed = 5 * dt
        rot_speed = 120 * dt

        anim_states = {
            "moving": False,
            "running": False
        }
        
        if is_down(KeyboardButton.shift()):
            anim_states["running"] = True
            speed = 15 * dt

        if is_down(KeyboardButton.asciiKey('w')):
            anim_states["moving"] = True
            self.model.setPos(self.model, 0, -speed, 0)

        if is_down(KeyboardButton.asciiKey('a')):
            self.model.setH(self.model.getH() + rot_speed)
        if is_down(KeyboardButton.asciiKey('d')):
            self.model.setH(self.model.getH() - rot_speed)

        self.animate(anim_states)
            
    def set_anim_state(self, anim):            
        if self.current_anim == anim:
            return
        self.model.stop(self.current_anim)
        self.model.loop(anim)
        self.current_anim = anim
        
    def animate(self, anim_states):
        if anim_states["moving"] and not anim_states["running"]:
            self.set_anim_state("walk")
        elif anim_states["moving"] and anim_states["running"]:
            self.set_anim_state("run")
        else:
            self.set_anim_state("idle")