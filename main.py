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
    food.draw(window)
    print(food.get_x(), food.get_y())
    pygame.display.update()

    running = True
    curr_dir = "a"

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and curr_dir != "s":
                    curr_dir = "w"
                elif event.key == pygame.K_s and curr_dir != "w":
                    curr_dir = "s"
                elif event.key == pygame.K_a and curr_dir != "d":
                    curr_dir = "a"
                elif event.key == pygame.K_d and curr_dir != "a":
                    curr_dir = "d"
                elif event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == EAT_FOOD:
                print("Munch")
                s.grow()
                safe_x = False
                safe_y = False
                x_coords = s.get_xcoords()
                y_coords = s.get_ycoords()
                x = -1
                y = -1

                while not safe_x and not safe_y:
                    if not safe_x:
                        x = random.randrange(0, settings.WIDTH, 10)
                        if x not in x_coords:
                            safe_x = True
                    if not safe_y:
                        y = random.randrange(0, settings.HEIGHT, 10)
                        if y not in y_coords:
                            safe_y = True
                
                food.move(x, y)
                
            if event.type == DIE:
                print("Game Over!") 
                running = False

        # Draw game objects
        window.fill(settings.BLUE)
        s.move(window, curr_dir)
        food.draw(window)
        pygame.display.update()

        # Check if snake eats food
        head = s.get_head()
        if head.get_rect().colliderect(food.get_rect()):
            pygame.event.post(pygame.event.Event(EAT_FOOD))
        
        # Check if snake hits itself
        for bod in s.get_body():
            if s.get_length() > 2 and head.get_rect().colliderect(bod.get_rect()):
                print(head.get_x(), head.get_y())
                print(bod.get_x(), bod.get_y())
                pygame.event.post(pygame.event.Event(DIE))
                break

        time.sleep(0.1)

    pygame.quit()


if __name__ == "__main__":
    main()