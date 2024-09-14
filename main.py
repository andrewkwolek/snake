from snake import Snake
from block import Body, Food
import pygame
import time
import settings
import random

def main():
    # Initialize pygame window
    pygame.init()
    clock = pygame.time.Clock
    window = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
    window.fill(settings.BLUE)
    pygame.display.update()
    pygame.display.flip()

    # Set user events
    EAT_FOOD = pygame.USEREVENT + 1
    DIE = pygame.USEREVENT + 2

    # Initialize snake object
    head = Body(400, 400)
    s = Snake(head)
    pygame.draw.rect(window, head.color, head.get_rect())

    # Initialize first food piece
    food = Food(random.randrange(0, settings.WIDTH, 10), random.randrange(0, settings.HEIGHT, 10))
    print(food.get_rect())
    pygame.draw.rect(window, food.color, food.get_rect())
    print(food.get_x(), food.get_y())
    pygame.display.update()

    running = True
    curr_dir = "a"

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    print("Up")
                    curr_dir = "w"
                elif event.key == pygame.K_s:
                    print("Down")
                    curr_dir = "s"
                elif event.key == pygame.K_a:
                    print("Left")
                    curr_dir = "a"
                elif event.key == pygame.K_d:
                    print("Right")
                    curr_dir = "d"
            if event.type == EAT_FOOD:
                print("Munch")
            if event.type == DIE:
                print("Game Over!")      

        window.fill(settings.BLUE)
        s.move(window, curr_dir)
        food.draw(window)
        pygame.display.update()

        time.sleep(0.1)


if __name__ == "__main__":
    main()