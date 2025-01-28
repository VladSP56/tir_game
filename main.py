import pygame
import random
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Shooting game")
icon = pygame.image.load("img/portrait-young-viking-children.jpg")
pygame.display.set_icon(icon)

# Загрузка изображения яблока
apple_img = pygame.image.load("img/maça 2.jpeg")
original_width, original_height = apple_img.get_size()

scale_factor = 0.08
target_width = int(original_width * scale_factor)
target_height = int(original_height * scale_factor)
target_img = pygame.transform.scale(apple_img, (target_width, target_height))


target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)

    screen.blit(target_img, (target_x, target_y))
    pygame.display.update()

pygame.quit()