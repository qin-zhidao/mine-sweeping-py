import json
import tkinter


def update_config(level_info=None):
    '''更新默认难度及排行榜信息'''
    with open('data.json', 'r') as f:
        load_f = json.load(f)['data']
        __level = load_f['default_level'][0]['val']
        level_info = load_f['level_info'][__level]
    return level_info

def set_tk_size(tk: tkinter.Tk, width: int, height: int):
    # 获取屏幕 宽、高
    screen_width = tk.winfo_screenwidth()
    screen_height = tk.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    geometry = f'{width}x{height}+{x}+{y}'
    return geometry