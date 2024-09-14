class Block:
    def __init__(self, x_init, y_init, col):
        self.x = x_init
        self.y = y_init
        self.color = col



class Body(Block):
    def __init__(self, x_init, y_init):
        color = (255, 255, 255)
        super().__init__(x_init, y_init, color)

class Food(Block):
    def __init__(self, x_init, y_init):
        color = (0, 255, 0)
        super().__init__(x_init, y_init, color)