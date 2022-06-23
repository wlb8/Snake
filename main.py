from turtle import width
import pygame
import operator

pygame.init()



def ConstantMove(direction, x, y):
    if direction == "left":
        x += 10
    elif direction == "right":
        x -= 10
    elif direction == "up":
        y -= 10
    elif direction == "down":
        y += 10

size = width, height = 500, 500
screen = pygame.display.set_mode(size)
x = 250
y = 250
direction = "down"
def Snake(screen, x, y):
    pygame.draw.rect(screen, (255, 0, 0), (x, y, 10, 10))


if __name__ == '__main__':
    snakeMove = 0
    while True:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(1)


        if x > 500 or x < 0:
            print("Game over")
            break
        if y > 500 or y < 0:
            print("Game over")
            break
            

        snakeMove
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x -= 10
            direction = "left"
        elif keys[pygame.K_RIGHT]:
            x += 10
            direction = "right"
        elif keys[pygame.K_DOWN]:
            y += 10
            direction = "down"
        elif keys[pygame.K_UP]:
            y -= 10
            direction = "up"
        ConstantMove(direction, x, y)
        
        screen.fill("black")
        Snake(screen, x, y)
        pygame.display.update()
    
