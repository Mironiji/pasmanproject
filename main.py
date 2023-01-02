import os
import sys
import pygame

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image

class Pic(pygame.sprite.Sprite):
    image = load_image("start_pic.png")
    image1 = load_image("end_pic.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Pic.image1
        self.rect = self.image.get_rect()
        self.rect.x = -600
        self.rect.y = 0

    def update(self):
        if self.rect.x < 0:
            self.rect.x += 3

    def titr(self):
        self.rect.x = -600
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    running = False
            pic.update()
            screen.fill('black')
            all_sprites.draw(screen)
            clock.tick(150)
            pygame.display.flip()

class field_object():
    def __init__(self, callable=False, other_obj=[], sym='?'):
        self._callable = callable
        self._other_obj = other_obj
        self.sym = sym

    def can_move(self, object_name):
        return self._callable ^ (not object_name in self._other_obj)

    def __str__(self):
        return self.sym

    def move(self, x, y):
        pass


class Wall(field_object):
    def __init__(self):
        super().__init__(True, [], '#')


class Space(field_object):
    def __init__(self):
        super().__init__(False, [], ' ')


class Player(field_object):
    def __init__(self):
        super().__init__(False, ['#', '@'], '@')


class Field:
    def __init__(self, name):
        with open(name, 'r') as f:
            mp = list(map(list, (f.read().split('\n'))))
        self._field = [[None for x in range(len(mp[0]))] for y in range(len(mp))]
        for y in range(len(self._field)):
            for x in range(len(self._field)):
                self._field[y][x] = ret_class(mp[y][x])

    def print(self):
        for y in self._field:
            print(''.join(map(str, y)))

    def __getitem__(self, key):
        return self._field[key[1]][key[0]]


def ret_class(sym):
    for x in (Wall(), Space()):
        if x.sym == sym:
            return x
    return field_object()

def terminate():
    pygame.quit()
    sys.exit()
def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.button:
                    pass
        running = False

pygame.init()
size = width, height = 600, 300
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
pic = Pic(all_sprites)

screen.fill('black')
all_sprites.draw(screen)
pic.image = Pic.image
pic.titr()
screen.fill('black')

pic.image = Pic.image1
pic.titr()

terminate()