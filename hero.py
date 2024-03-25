class Hero():
    def __init__(self, land):
        self.model = loader.loadModel('smiley')
        self.model.reparentTo(render)
        self.model.setScale(0.5)
        self.model.setPos(3, 3, 2)
        self.camera_bind()
        self.apply_events()
        self.land = land
    def camera_bind(self):
        base.disableMouse()
        base.camera.setH(180)
        base.camera.reparentTo(self.model)

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
        if not self.land.find_blocks((x, y, self.model.getZ())):
            self.model.setY(y)
            self.model.setX(x)
        print(self.land.find_blocks((x, y, self.model.getZ())))


    def forward(self):
        self.check_direction(0)

    def right(self):
        self.check_direction(-90)

    def left(self):
        self.check_direction(90)

    def back(self):
        self.check_direction(180)


    def check_direction(self, angle):
        angle = (self.model.getH() + angle) % 360
        if angle >= 0 and angle <= 20:
            self.move(0, -1)
        elif angle <= 65:
            self.move(1, -1)
        elif angle <= 110:
            self.move(1, 0)
        elif angle <= 155:
            self.move(1, 1)
        elif angle <= 200:
            self.move(0, 1)
        elif angle <= 245:
            self.move(-1, 1)
        elif angle <= 290:
            self.move(-1, 0)
        elif angle <= 335:
            self.move(-1, -1)
        else:
            self.move(0, -1)


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
