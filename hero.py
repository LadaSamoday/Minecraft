class Hero():
    def __init__(self, land):
        self.model = loader.loadModel('smiley')
        self.model.reparentTo(render)
        self.model.setScale(0.5)
        self.model.setPos(3, 3, 2)
        self.camera_bind()
        self.land = land
        self.apply_events()
        self.texture = 'brick.png'
    def camera_bind(self):
        base.disableMouse()
        base.camera.setH(180)
        base.camera.reparentTo(self.model)
        base.camera.setPos(0, 0.8, 0)

    def turn_left(self):
        self.model.setH((self.model.getH() + 5) % 360)

    def turn_right(self):
        self.model.setH((self.model.getH() - 5) % 360)

    def turn_up(self):
        if self.model.getP() > 270 or self.model.getP() <= 90:
            self.model.setP((self.model.getP() - 5) % 360)
        print(self.model.getP())



    def turn_down(self):
        if self.model.getP() >= 270 or self.model.getP() < 90:
            self.model.setP((self.model.getP() + 5) % 360)

    def move(self, x, y):
        x = self.model.getX() + x
        y = self.model.getY() + y
        z = self.model.getZ() - 1
        if not self.land.find_blocks((x, y, z)):
            while not self.land.find_blocks((x, y, z - 1)):
                z -= 1
                if z < -10:
                    return
            self.model.setY(y)
            self.model.setZ(z + 1)
            self.model.setX(x)
        elif not self.land.find_blocks((x, y, z + 1)):
            self.model.setY(y)
            self.model.setX(x)
            self.model.setZ(self.model.getZ() + 1)

        print(self.model.getZ())





    def forward(self):
        self.move(*self.check_direction(0))

    def right(self):
        self.move(*self.check_direction(-90))

    def left(self):
        self.move(*self.check_direction(90))

    def back(self):
        self.move(*self.check_direction(180))

    def check_pitch(self):
        print(self.model.getP())
        if self.model.getP() >= 270 and self.model.getP() < 340:
            return 1
        elif self.model.getP() < 35 or self.model.getP() > 340:
            return 0
        elif self.model.getP() >= 35 and self.model.getP() < 75:
            return -1
        else:
            return -2

    def build_block(self):
        z = self.check_pitch()
        x, y = self.check_direction(0)
        self.land.add_block((self.model.getX() + x, self.model.getY() + y, self.model.getZ() + z),
                            self.texture)


    def break_block(self):
        z = self.check_pitch()
        x, y = self.check_direction(0)
        blocks = self.land.find_blocks((self.model.getX() + x,
                                        self.model.getY() + y, self.model.getZ() + z))
        for block in blocks:
            block.removeNode()


    def check_direction(self, angle):
        angle = (self.model.getH() + angle) % 360
        if angle >= 0 and angle <= 20:
            return (0, -1)
        elif angle <= 65:
            return (1, -1)
        elif angle <= 110:
            return (1, 0)
        elif angle <= 155:
            return (1, 1)
        elif angle <= 200:
            return (0, 1)
        elif angle <= 245:
            return (-1, 1)
        elif angle <= 290:
            return (-1, 0)
        elif angle <= 335:
            return (-1, -1)
        else:
            return (0, -1)

    def texture_wood (self):
        self.texture = 'wood.png'
    def texture_stone(self):
        self.texture = 'stone.png'
    def texture_brick(self):
        self.texture = 'brick.png'

    def apply_events(self):
        base.accept('arrow_left', self.turn_left)
        base.accept('arrow_right', self.turn_right)
        base.accept('arrow_left-repeat', self.turn_left)
        base.accept('arrow_right-repeat', self.turn_right)
        base.accept('arrow_up', self.turn_up)
        base.accept('arrow_down', self.turn_down)
        base.accept('arrow_up-repeat', self.turn_up)
        base.accept('arrow_down-repeat', self.turn_down)
        base.accept('w', self.forward)
        base.accept('w-repeat', self.forward)
        base.accept('d', self.right)
        base.accept('d-repeat', self.right)
        base.accept('a', self.left)
        base.accept('a-repeat', self.left)
        base.accept('s', self.back)
        base.accept('s-repeat', self.back)
        base.accept('space', self.build_block)
        base.accept('b', self.break_block)
        base.accept('1', self.texture_wood)
        base.accept('2', self.texture_brick)
        base.accept('3', self.texture_stone)
        base.accept('shift-=', self.land.save_map)
        base.accept('=', self.land.load_map)

