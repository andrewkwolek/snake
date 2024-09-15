from collections import deque
from block import Block, Body, Food
import pygame
import settings
from itertools import islice

class Snake:
    def __init__(self, head : Body):
        self.q = deque()
        self.q.append(head)
        self.coords = [(head.get_x(), head.get_y())]

    def get_length(self):
        return len(self.q)

    def get_head(self):
        return self.q[0]
    
    def get_body(self):
        return islice(self.q, 1, len(self.q))
    
    def get_xcoords(self):
        coords = []
        for block in self.q:
            coords.append(block.coord[0])
        return coords
    
    def get_ycoords(self):
        coords = []
        for block in self.q:
            coords.append(block.coord[1])
        return coords
    
    def update_coords(self):
        coords = []
        for block in self.q:
            coords.append(block.get_coords())
        self.coords = coords

    def move(self, window, dir):
        front = self.q[0]
        back = self.q.pop()
        dx = front.get_x() - back.get_x()
        dy = front.get_y() - back.get_y()
        if dir == "w":
            if back.get_y() - 10 < 0:
                back.move(dx, dy + settings.HEIGHT - 10)
            else:
                back.move(dx, dy - 10)
        if dir == "d":
            if back.get_x() + 10 > settings.WIDTH:
                back.move(dx - settings.WIDTH + 10, dy)
            else:
                back.move(dx + 10, dy)
        if dir == "a":
            if back.get_x() - 10 < 0:
                back.move(dx + settings.WIDTH - 10, dy)
            else:
                back.move(dx - 10, dy)
        if dir == "s":
            if back.get_y() + 10 > settings.HEIGHT:
                back.move(dx, dy - settings.HEIGHT + 10)
            else:
                back.move(dx, dy + 10)
        self.q.appendleft(back)

        for link in self.q:
            link.draw(window)

        self.update_coords()
    
    def grow(self):
        new_bod = Body(self.get_head().get_x(), self.get_head().get_y())
        print(self.get_head(), new_bod)
        self.q.append(new_bod)
        self.coords.append((self.get_head().get_x(), self.get_head().get_y()))
        print("coords: %s", self.coords)


            
