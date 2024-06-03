import pygame
from cristall import Cristal
pygame.init()

W, H = 900, 500
window = pygame.display.set_mode((W, H))
pygame.display.set_caption("Game")


clock = pygame.time.Clock()

bg_image = pygame.event.get():
speed = 1
c_1 = Cristal(W//2, 1, 'imges/001.png')
c_2 = Cristal(W//2-250, 3, 'imges/002.png')


while True:
    for ivent in pygame.event.get():
        if ivent.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(c_1.image, c_1.rect)
    window.blit(c_2.image, c_2.rect)

    clock.tick(60)
    pygame.display.update()

    if c_1.rect.y < H - 20:
        c_1.rect.y += speed
    else:
        c_1.rect.y = 0

    c_1.move(H)
    c_1.move(H)




