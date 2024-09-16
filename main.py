from snake import Snake
from block import Body, Food
import pygame
import time
import settings
import random

def game_over(window, score):
    time.sleep(1)
    window.fill(settings.BLUE)
    print("Game Over!")
    go_ft = pygame.font.SysFont(None, 48)
    go_text = pygame.font.Font.render(go_ft, f'GAME OVER! Score: {score}', 1, settings.RED)
    window.blit(go_text, (settings.WIDTH / 4, settings.HEIGHT / 4))
    pygame.display.update()
    time.sleep(2)
    pygame.quit()
    quit()

def main():
    # Initialize pygame window
    pygame.init()
    ft = pygame.font.SysFont(None, 32)
    clock = pygame.time.Clock
    window = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
    window.fill(settings.BLUE)
    pygame.display.update()
    pygame.display.flip()

    # Set user events
    EAT_FOOD = pygame.USEREVENT + 1
    DIE = pygame.USEREVENT + 2

    score = 0
    text = pygame.font.Font.render(ft, f'Score: {score}', 1, settings.WHITE)
    window.blit(text, (20, 20))

    # Initialize snake object
    head = Body(settings.WIDTH / 2, settings.HEIGHT / 2)
    s = Snake(head)
    pygame.draw.rect(window, head.color, head.get_rect())

    # Initialize first food piece
    food = Food(random.randrange(settings.BLOCK_LENGTH, settings.WIDTH - settings.BLOCK_LENGTH, settings.BLOCK_LENGTH), random.randrange(settings.BLOCK_LENGTH, settings.HEIGHT - settings.BLOCK_LENGTH, settings.BLOCK_LENGTH))
    food.draw(window)
    pygame.display.update()

    running = True
    curr_dir = "a"

    # Game loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                game_over(window, score)
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
                    game_over(window, score)
            if event.type == EAT_FOOD:
                score += 1
                s.grow()
                safe_x = False
                safe_y = False
                x_coords = s.get_xcoords()
                y_coords = s.get_ycoords()
                x = -1
                y = -1

                while not safe_x and not safe_y:
                    if not safe_x:
                        x = random.randrange(settings.BLOCK_LENGTH, settings.WIDTH - settings.BLOCK_LENGTH, settings.BLOCK_LENGTH)
                        if x not in x_coords:
                            safe_x = True
                    if not safe_y:
                        y = random.randrange(settings.BLOCK_LENGTH, settings.HEIGHT - settings.BLOCK_LENGTH, settings.BLOCK_LENGTH)
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
        text = pygame.font.Font.render(ft, f'Score: {score}', 1, settings.WHITE)
        window.blit(text, (20, 20))

        # Check if snake eats food
        head = s.get_head()
        if head.get_rect().colliderect(food.get_rect()):
            pygame.event.post(pygame.event.Event(EAT_FOOD))

        # Check if snake hits wall
        if head.get_x() < 0 or head.get_x() >= settings.WIDTH:
            game_over(window, score)
        if head.get_y() < 0 or head.get_y() >= settings.HEIGHT:
            game_over(window, score)
        
        # Check if snake hits itself
        for bod in s.get_body():
            if s.get_length() > 1 and head.get_rect().colliderect(bod.get_rect()):
                pygame.event.post(pygame.event.Event(DIE))
                game_over(window, score)
                break

        pygame.display.update()
        time.sleep(0.1)

    pygame.quit()


if __name__ == "__main__":
    main()