import pygame
import os
import sys

screen_width = 200
screen_height = 200

def main():
    pygame.init()

    screen = pygame.display.set_mode(
        [screen_width, screen_height]
    )
    pygame.display.set_caption('test')
    running = True # 程序状态
    while running:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                running = False
                
if __name__ == '__main__':
    main()