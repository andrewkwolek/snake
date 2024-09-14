from collections import deque
from block import Block, Body, Food
import pygame
import settings

class Snake:
    def __init__(self, head : Body):
        self.q = deque()
        self.q.append(head)

    def move(self, window, dir):
        front = self.q[0]
        back = self.q.pop()
        dx = front.get_x() - back.get_x()
        dy = front.get_y() - back.get_y()
        if dir == "w":
            if back.get_y() - 10 < 0:
                back.move(window, dx, dy + settings.HEIGHT - 10)
            else:
                back.move(window, dx, dy - 10)
        if dir == "d":
            if back.get_x() + 10 > settings.WIDTH:
                back.move(window, dx - settings.WIDTH + 10, dy)
            else:
                back.move(window, dx + 10, dy)
        if dir == "a":
            if back.get_x() - 10 < 0:
                back.move(window, dx + settings.WIDTH - 10, dy)
            else:
                back.move(window, dx - 10, dy)
        if dir == "s":
            if back.get_y() + 10 > settings.HEIGHT:
                back.move(window, dx, dy - settings.HEIGHT + 10)
            else:
                back.move(window, dx, dy + 10)
        self.q.appendleft(back)
            
