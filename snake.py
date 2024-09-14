from collections import deque
import pygame
import random

class Snake:
    q = deque()

    def __init__(self):
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


class Block:
    x = 0
    y = 0
    color = (0, 0, 0)
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


    

def main():
    pygame.init()
    s = Snake()
    window = pygame.display.set_mode((800, 800))
    blue = (0, 0, 255)
    window.fill(blue)
    pygame.display.flip()
    pygame.display.update()
    EAT_FOOD = pygame.USEREVENT + 1
    DIE = pygame.USEREVENT + 2

    pygame.draw.rect(window, (255, 255, 255), (s.q[0].x, s.q[0].y, 10, 10))
    pygame.display.update()
    running = True

    while running:
        for event in pygame.event.get():
            print(event.type)
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    print("Up")
                    s.move("w")
                elif event.key == pygame.K_s:
                    print("Down")
                    s.move("s")
                elif event.key == pygame.K_a:
                    print("Left")
                    s.move("a")
                elif event.key == pygame.K_d:
                    print("Right")
                    s.move("d")
                for block in s.q:
                        pygame.draw.rect(window, block.color, (block.x, block.y, 10, 10))
                pygame.display.update()
            if event.type == EAT_FOOD:
                print("Munch")
            if event.type == DIE:
                print("Game Over!")      


if __name__ == "__main__":
    main()