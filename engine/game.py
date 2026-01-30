from direct.showbase.ShowBaseGlobal import globalClock
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from panda3d.core import loadPrcFile, AntialiasAttrib, LVector4, TextNode
from direct.gui.OnscreenText import OnscreenText
from engine.instance import set_instance_game
from engine.set_inputs import set_inputs
from config.states import *
from game.load_scenes import load_scenes
from engine.editor import camera_move, display_camera_position

loadPrcFile('config/config.prc')

class Game(ShowBase):
    def __init__(self):
        super().__init__()
        
        self.editor = False
        self.debug_text = OnscreenText(
            text="",
            pos=(-1.75, 0.95),
            scale=0.04,
            fg=(1, 1, 1, 1),
            align=TextNode.ALeft,
            mayChange=True
        )
        self.debug_text.hide()
        self.accept('f12', self.editor_mode)
        set_instance_game(self)
        set_inputs(self)
        self.disable_mouse()
        self.render.set_antialias(AntialiasAttrib.MMultisample)
        self.render.setShaderAuto()
        self.win.setClearColor(LVector4(0.2, 0.2, 0.2, 1))
        self.paused = False
        self.scenes = load_scenes()
        self.current_scene = None
        self.taskMgr.add(self.update, "update")
        self.set_scene("main")
    
    def update(self, task):
        dt = globalClock.getDt()
        
        if self.current_scene.loaded and not self.paused and not self.editor:
            self.current_scene.update(dt)
            
        if self.editor and DEBUG:
            camera_move(self, dt)
        
        return Task.cont
    
    def set_scene(self, scene_name):
        if self.current_scene is not None: self.current_scene.destroy()
        self.current_scene = self.scenes[scene_name]
        self.current_scene.pre_load()
        self.current_scene.create()
        self.current_scene.loaded = True
        
    def editor_mode(self):
        if DEBUG:
            self.editor = not self.editor
        display_camera_position(self)

game = Game()
game.run()