import pygame
import random
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))

pygame.display.set_caption("Shootin game")
icon = pygame.image.load("img/portrait-young-viking-children.jpg")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/istockphoto-521936579-612x612.jpg")
target_width = 80
target_height = 80
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HIGHT - target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

 running = True
while running:
    screen.fill(color )




pygame.quit()