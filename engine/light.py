from panda3d.core import AmbientLight, DirectionalLight
from panda3d.core import Vec3, Vec4

def ambient_light(game, color=Vec4(0.2, 0.2, 0.2, 1)):
    ambientLight = AmbientLight("ambient light")
    ambientLight.setColor(color)
    ambientLightNodePath = game.render.attachNewNode(ambientLight)
    game.render.setLight(ambientLightNodePath)
    
def directional_light(game, hpr=Vec3(45, -45, 0)):
    mainLight = DirectionalLight("directional light")
    mainLight.setShadowCaster(True, 512, 512)
    mainLightNodePath = game.render.attachNewNode(mainLight)
    mainLightNodePath.setHpr(hpr)
    game.render.setLight(mainLightNodePath)