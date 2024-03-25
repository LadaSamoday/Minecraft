from direct.showbase.ShowBase import ShowBase
from map_manager import MapManager
from hero import Hero

class Game(ShowBase):
    def __init__(self):
        super().__init__()
        map = MapManager()
        hero = Hero(map)
        base.camLens.setFov(90)


game = Game()


game.run()

