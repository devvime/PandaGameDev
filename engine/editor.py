from config.inputs import inputs

def display_camera_position(game):
    if game.editor:
        game.debug_text.show()
    else: game.debug_text.hide()

def camera_move(game, dt):
    speed = 5 * dt
    rot_speed = 30 * dt

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
    
    game.cam.setR(0)
    
    pos = game.cam.getPos()
    hpr = game.cam.getHpr()
    game.debug_text.setText(
        f"Camera Pos: ({pos.x:.2f}, {pos.y:.2f}, {pos.z:.2f})\n"
        f"Camera HPR: ({hpr.x:.1f}, {hpr.y:.1f}, {hpr.z:.1f})"
    )
