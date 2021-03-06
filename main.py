from tkinter import *
import tkinter.messagebox
import time

import tool


def main():
    
    # 游戏配置信息
    level_info = tool.update_config()
    if level_info == None:
        print('游戏配置信息加载失败')
        exit()
    mine_size = 20 # 雷的大小
    box_size = [
        level_info['size'][0] * mine_size, 
        level_info['size'][1] * mine_size
    ]
    
    tk = tkinter.Tk()
    tk.title('扫雷')
    tk.geometry(tool.set_tk_size(tk, box_size[0], box_size[1]))

    tk.mainloop()
                
if __name__ == '__main__':
    main()