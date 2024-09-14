from snake import Snake
import pygame


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