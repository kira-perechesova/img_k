import pygame
import sys

pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
img = pygame.image.load('data/creature.png')
rect = img.get_rect()
rect.topleft = (0, 0)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    k = pygame.key.get_pressed()
    if k[pygame.K_LEFT]:
        rect.x -= 10
    if k[pygame.K_RIGHT]:
        rect.x += 10
    if k[pygame.K_UP]:
        rect.y -= 10
    if k[pygame.K_DOWN]:
        rect.y += 10



    screen.fill((255, 255, 255))
    screen.blit(img, rect.topleft)
    pygame.display.flip()

pygame.quit()
sys.exit()