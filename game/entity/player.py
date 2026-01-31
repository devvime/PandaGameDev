from engine.entity import Entity
from direct.actor.Actor import Actor
from config.inputs import inputs

class Player(Entity):
    def __init__(self):
        super().__init__()
    
    def pre_load(self):
        self.model = Actor("assets/player/player", {
            "idle": "assets/player/player-idle",
            "walk": "assets/player/player-walk"
        })
        self.model.setShaderOff()
        self.model.setHpr(180, 0, 0)
        self.model.setScale(0.5, 0.5, 0.5)
        self.model.reparentTo(self.game.render)
        
        self.current_anim = None
        self.model.loop("idle")
        self.current_anim = "idle"
        
    def create(self):
        ...
        
    def update(self, dt):
        self.movement(dt)
        
    def movement(self, dt):
        speed = 5 * dt
        rot_speed = 90 * dt

        moving = False

        if inputs["w"]:
            moving = True
            self.model.setPos(self.model, 0, -speed, 0)
        if inputs["s"]:
            moving = True
            self.model.setPos(self.model, 0, speed, 0)

        if inputs["a"]:
            self.model.setH(self.model.getH() + rot_speed)
        if inputs["d"]:
            self.model.setH(self.model.getH() - rot_speed)

        if moving:
            self.set_anim_state("walk")
        else:
            self.set_anim_state("idle")
            
    def set_anim_state(self, anim):            
        if self.current_anim == anim:
            return

        self.model.stop(self.current_anim)
        self.model.loop(anim)
        self.current_anim = anim