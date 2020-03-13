# 播放功能

import pygame, output, erase, add
from pygame.locals import *

pygame.init()
display = pygame.display    # 显示
music = pygame.mixer.music  # 音乐
screen = display.set_mode((700, 600))
font = pygame.font.Font("font/msyh.ttf", 16) # 文字
BackColor = (87, 105, 60)

tim = 1 # 实现只用空格控制暂停与播放
val = 0.5 # 记录音量
pygame.key.set_repeat(500, 80) # 实现一直按一个键重复触发事件

def volUpd(key, name):
    global val
    if key == K_UP:
        val = round(val + 0.05, 2)
        if val > 1: val = 1
        music.set_volume(val)
        screen.fill(BackColor)
        output.output(name, 350, 100)
        output.output("音量：%d" % int(val * 100) + '%', 350, 200)
        output.output("空格为暂停/播放，↑↓键调节音量", 350, 350)
        output.output("s为上一首，d为下一首", 350, 380)
        output.output("w回到曲库，ESC退出程序", 350, 410)

    elif key == K_DOWN:
        val = round(val - 0.05, 2)
        if val < 0: val = 0
        music.set_volume(val)
        screen.fill(BackColor)
        output.output(name, 350, 100)
        output.output("音量：%d" % int(val * 100) + '%', 350, 200)
        output.output("空格为暂停/播放，↑↓键调节音量", 350, 350)
        output.output("s为上一首，d为下一首", 350, 380)
        output.output("w回到曲库，ESC退出程序", 350, 410)

def staUpd(key):
    if key == K_SPACE:
        global tim
        tim = -tim
        if tim == -1: music.pause()
        else: music.unpause()
    elif key == K_w: return -1
    elif key == K_ESCAPE: return -2

def play(fl, tag):
    if fl == "error": return -1
    screen.fill(BackColor)
    global val, tim
    if tag == -1:
        val = music.get_volume()
        tim = 1
    else:
        val = 0.5
        tim = 1
        music.load(fl)
        music.play()
        music.set_volume(val)
    name = erase.getName(fl)
    output.output(name, 350, 100)
    output.output("音量：%d" % int(val * 100) + '%', 350, 200)
    output.output("空格为暂停/播放，↑↓键调节音量", 350, 350)
    output.output("s为上一首，d为下一首", 350, 380)
    output.output("w回到曲库，ESC退出程序", 350, 410)
    while True:
        if music.get_busy() == 0: return fl
        i = pygame.event.wait()
        if i.type == KEYDOWN:
            volUpd(i.key, name)
            sta = staUpd(i.key)
            if sta == -1: return fl
            if sta == -2: return "exit^"
            if i.key == K_s:
                id = erase.getId(fl)
                if add.getLine() == id: id = 1
                else: id = id + 1
                return str(id)
            elif i.key == K_d:
                id = erase.getId(fl)
                if id == 1: id = add.getLine()
                else: id = id - 1
                return str(id)