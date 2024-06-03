import pygame
from cristall import Cristall
pygame.init()

W, H = 900,500
window = pygame.display.set_mode((W,H))
pygame.display.set_caption("Game")

clock = pygame.time.Clock()

bg_load = pygame.image.load('imges/фон.png')
bg_image = pygame.transform.scale(bg_load,(bg_load.get_width()//2, bg_load.get_height()//2))

cristalls = pygame.sprite.Group()
cristalls.add(Cristall(W//2, 1, 'imges/001.png'),
              Cristall(W//2-250, 3, 'imges/002.png'),
              Cristall(W//2+250, 5, 'imges/003.png'))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.blit(bg_image, (0,0))
    cristalls.draw(window)

    pygame.display.update()
    clock.tick(60)

    cristalls.update(H)

