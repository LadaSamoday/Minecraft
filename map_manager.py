class MapManager():
    def __init__(self):
        self.land = render.attachNewNode('Land')
        self.create_map('stone.png')


    def add_block(self, pos, texture):
        self.model = loader.loadModel('block.egg')
        self.model.reparentTo(self.land)
        self.model.setPos(pos)
        self.model.setTexture(loader.loadTexture(texture))
        self.model.setColor((0.1, 0.9, 0.6, 1))
        self.model.setTag('pos', str(pos))


    def find_blocks(self, pos):
        print(pos)
        return self.land.findAllMatches('=pos=' + str(pos))

    def create_map(self, texture):
        with open('map.txt', 'r')as file:
            x = 0
            for i in file:
                y = 0
                x += 1
                for n in i.replace('\n', ''):
                    for z in range(int(n) + 1):
                        self.add_block((x, y, z), texture)
                    y += 1







