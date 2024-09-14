from collections import deque
from block import Block, Body, Food
import random

class Snake:
    def __init__(self):
        self.q = deque()
        b = Body(400, 400)
        print(b.x)
        self.q.append(b)

    def move(self, dir):
        temp = self.q.pop()
        if dir == "w":
            temp.y -= 10
        if dir == "d":
            temp.x += 10
        if dir == "a":
            temp.x -= 10
        if dir == "s":
            temp.y += 10
        self.q.appendleft(temp)
