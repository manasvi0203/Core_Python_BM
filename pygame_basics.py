import pygame

pygame.init()

width, height = 1000, 500

white = 255, 255, 255
red = 255, 0, 0
yellow = 255, 255, 0
green = 0, 255, 0
blue = 0, 0, 255
black = 0, 0, 0
color_1 = 220,20,60
x = 0
y = 0
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Pygame Basics")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    screen.fill(white)
    pygame.draw.rect(screen, color_1, [x, y, 200, 200])
    x = x + 0.2
    if x > width:
        x = 0
    pygame.draw.circle(screen, green, [23, 45], 50)
    pygame.display.update()
            
