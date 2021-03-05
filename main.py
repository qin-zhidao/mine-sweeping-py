import pygame
import os, sys
import json
import time


def update_config(level_info=None):
    '''更新默认难度及排行榜信息'''
    with open('data.json', 'r') as f:
        load_f = json.load(f)['data']
        __level = load_f['default_level'][0]['val']
        level_info = load_f['level_info'][__level]
    return level_info

def main():

    # 游戏配置信息
    level_info = update_config()

    mine_size = 20 # 雷的大小
    if level_info == None:
        print('游戏配置信息加载失败')
        exit()
    screen_size = [
        level_info['size'][0] * mine_size, 
        level_info['size'][1] * mine_size
    ] 

    pygame.init()
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption('扫雷')
    running = True # 程序状态

    while running:
        for event in pygame.event.get():
            print(event)
            # 点击窗口关闭按钮
            if event.type == pygame.QUIT:
                running = False
                
if __name__ == '__main__':
    main()