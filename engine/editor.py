from config.inputs import inputs
from panda3d.core import Vec3

def camera_move(game, dt):
    speed = 10 * dt
    rot_speed = 60 * dt

    if inputs["w"]:
        game.cam.setPos(game.cam, 0, speed, 0)
    if inputs["s"]:
        game.cam.setPos(game.cam, 0, -speed, 0)
    if inputs["a"]:
        game.cam.setPos(game.cam, -speed, 0, 0)
    if inputs["d"]:
        game.cam.setPos(game.cam, speed, 0, 0)
    if inputs["control"]:
        game.cam.setPos(game.cam, 0, 0, -speed)
    if inputs["shift"]:
        game.cam.setPos(game.cam, 0, 0, speed)

    if inputs["arrow_up"]:
        game.cam.setP(game.cam.getP() + rot_speed)
    if inputs["arrow_down"]:
        game.cam.setP(game.cam.getP() - rot_speed)
    if inputs["arrow_left"]:
        game.cam.setH(game.cam.getH() + rot_speed)
    if inputs["arrow_right"]:
        game.cam.setH(game.cam.getH() - rot_speed)
