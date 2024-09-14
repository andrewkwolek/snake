import pygame

class Block:
    def __init__(self, x_init, y_init):
        self.x = x_init
        self.y = y_init
        self.r = pygame.Rect(self.x, self.y, 10, 10)
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def get_rect(self):
        return self.r


class Body(Block):
    def __init__(self, x_init, y_init):
        self.color = (255, 255, 255)
        super().__init__(x_init, y_init)

    def move(self, window, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
        self.r.move_ip(dx, dy)
        pygame.draw.rect(window, self.color, self.r)

class Food(Block):
    def __init__(self, x_init, y_init):
        self.color = (0, 255, 0)
        super().__init__(x_init, y_init)

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.r)