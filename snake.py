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
            back.move(dx, dy - settings.BLOCK_LENGTH)
        if dir == "d":
            back.move(dx + settings.BLOCK_LENGTH, dy)
        if dir == "a":
            back.move(dx - settings.BLOCK_LENGTH, dy)
        if dir == "s":
            back.move(dx, dy + settings.BLOCK_LENGTH)
        self.q.appendleft(back)

        for link in self.q:
            link.draw(window)

        self.update_coords()
    
    def grow(self):
        for i in range(3):
            new_bod = Body(self.get_head().get_x(), self.get_head().get_y())
            self.q.append(new_bod)
            self.coords.append((self.get_head().get_x(), self.get_head().get_y()))


            
