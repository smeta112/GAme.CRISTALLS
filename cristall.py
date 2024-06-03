import pygame
#scale image

class Cristall(pygame.sprite.Sprite):
    def __init__(self, x, speed,filename):
        pygame.sprite.Sprite.__init__(self)
        image_l = pygame.image.load(filename)
        self.image = pygame.transform.scale(image_l,(image_l.get_width()//30, image_l.get_height()//30))
        self.rect = self.image.get_rect(center=(x,0))
        self.speed = speed

    def move(self, *args):
        if self.rect.y < args[0] - 20:
            self.rect.y += self.speed
        else:
            self.rect.y = 0















""" def summa(*args):
            result = 0
            for i in list_sum:
                result += i
            return result

        list_of_number = [1, 2, 3]
        print(summa(list_of_number))

        # *args, **kwards"""