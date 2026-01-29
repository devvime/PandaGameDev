from config.inputs import inputs

def set_inputs(game):
    for input in inputs:
        game.accept(input, update_keys, [input, True])
        game.accept(f"{input}-up", update_keys, [input, False])

def update_keys(controlName, controlState):
    inputs[controlName] = controlState