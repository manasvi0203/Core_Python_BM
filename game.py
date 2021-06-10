import pygame
import random

pygame.init()

width = 1000
height = 500

red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255
black = 0, 0, 0
white = 255, 255, 255
flag = False
def score(count):
    font = pygame.font.SysFont(None, 30)
    text = font.render(f"Score: {count}", True, black)
    screen.blit(text, (10,10))
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Keppy Uppy")
ball_x = width//2
ball_y = height - 40
count = 0
speed = 0.2
while True:
    screen.fill(white)
    mos_x, mos_y = pygame.mouse.get_pos()
    mouse_rect = pygame.Rect(mos_x, mos_y, 10, 10)
    ball = pygame.draw.circle(screen, red, [ball_x, ball_y], 40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if ball.colliderect(mouse_rect):
                ball_y = ball_y - 100
                ball_x = random.randint(40, width-40)
                flag = True
                count = count + 1
    if count%5==0:
        speed = speed + 0.2
    if flag:
        ball_y = ball_y + speed
    if ball_y > height - 40:
        ball_y = height -40
        count = 0
        speed = 0.2
        
    score(count)
    pygame.display.update()
