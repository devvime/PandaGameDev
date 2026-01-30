from engine.instance import Game

class Scene:
    def __init__(self):
        self.game = Game()
        self.loaded = False
        self.objects = {}

    def _call_if_exists(self, obj, method_name, *args):
        method = getattr(obj, method_name, None)
        if callable(method):
            method(*args)

    def pre_load(self):
        for obj in self.objects.values():
            self._call_if_exists(obj, "pre_load")

    def create(self):
        for obj in self.objects.values():
            self._call_if_exists(obj, "create")

    def update(self, dt):
        for obj in self.objects.values():
            self._call_if_exists(obj, "update", dt)

    def destroy(self):
        for obj in self.objects.values():
            self._call_if_exists(obj, "destroy")
