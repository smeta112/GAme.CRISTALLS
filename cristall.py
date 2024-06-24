import pygame
#scale image

class Cristall(pygame.sprite.Sprite):
    def __init__(self, x, speed, surf, score, group):
        pygame.sprite.Sprite.__init__(self)
        image_l = surf
        self.image = pygame.transform.scale(image_l,(image_l.get_width()//30, image_l.get_height()//30))
        self.rect = self.image.get_rect(center=(x,0))
        self.speed = speed
        self.score = score
        self.add(group)

    balls_img = ["001.png", "002.png", "003.png"]


    def update(self, *args):
        if self.rect.y < args[0] - 20:
            self.rect.y += self.speed
        else:
            self.kill() #чтоб удалялось а не лежало


"""    else:
            self.rect.y = 0
#НЕ совсем правильно одно и то же считать
"""













""" def summa(*args):
            result = 0
            for i in list_sum:
                result += i
            return result

        list_of_number = [1, 2, 3]
        print(summa(list_of_number))

        # *args, **kwards"""