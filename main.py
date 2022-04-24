import pygame,sys
from pygame.locals import *
from level import *

pygame.init()
size = (600,600)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (0,0,0)
images = {"w": "images/tiles/wall12.gif",
          "f":"images/tiles/roomFloor13.gif",
          }

levels = []
level_num = 0
current_level = None


def change_level(change):
    global level_num,levels
    if change == 1:
        if level_num == len(levels) - 1:
            levels.append((RandomLevel(images)))
        level_num += 1
        current_level = levels[level_num]
    elif change == -1:
        if level_num > 0:
            level_num -= 1
            current_level = levels[level_num]
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
def main():
    global images
    global screen,level_num,current_level
    levels.append(RandomLevel(images))
    current_level = levels[level_num]

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_f:
                    screen = pygame.display.set_mode(size,FULLSCREEN)
                if event.key == K_d:
                    screen = pygame.display.set_mode(size)


        change_level(current_level.update())

        screen.fill(color)
        current_level.draw(screen)
        pygame.display.flip()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

