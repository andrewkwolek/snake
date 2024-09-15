import pygame
import settings

class Block:
    def __init__(self, x_init, y_init):
        self.coord = (x_init, y_init)
        self.r = pygame.Rect(self.coord[0], self.coord[1], settings.BLOCK_LENGTH, settings.BLOCK_LENGTH)

    def get_coords(self):
        return self.coord
    
    def get_x(self):
        return self.coord[0]
    
    def get_y(self):
        return self.coord[1]
    
    def get_rect(self):
        return self.r


class Body(Block):
    def __init__(self, x_init, y_init):
        self.color = settings.WHITE
        super().__init__(x_init, y_init)
    
    def draw(self, window):
        pygame.draw.rect(window, self.color, self.r)

    def move(self, dx, dy):
        self.coord = (self.coord[0] + dx, self.coord[1] + dy)
        self.r.move_ip(dx, dy)

class Food(Block):
    def __init__(self, x_init, y_init):
        self.color = settings.GREEN
        super().__init__(x_init, y_init)

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.r)

    def move(self, new_x, new_y):
        dx = new_x - self.get_x()
        dy = new_y - self.get_y()
        self.coord = (self.coord[0] + dx, self.coord[1] + dy)
        self.r.move_ip(dx, dy)
