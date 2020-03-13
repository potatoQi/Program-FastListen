import pygame
from pygame.locals import *
import output, play, add, show, buildPath, erase

# 实例化对象
pygame.init()
display = pygame.display    # 显示
music = pygame.mixer.music  # 音乐
image = pygame.image        # 图片
font = pygame.font.Font("font/msyh.ttf", 16) # 文字
# 初始化窗口
display.set_caption("Fast Listen!")
screen = display.set_mode((700, 600))
display.set_icon(image.load("image/title.jpg"))
# 初始化字体
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BackColor = (87, 105, 60)

def tran(id, num):
    id = id // 9
    id = id * 9 + num
    return id

def musicList():
    num = 1
    tag = 0
    fl = ""
    sta = show.show(num, num + 8)
    if sta == -1: return -1
    while 1:
        if tag != 0:
            fl = play.play(buildPath.buildPath(tag), 0)
            if fl.find(".mp3") == -1:
                if fl == "exit^": return -2
                tmp = int(fl)
                if tmp == tag: tag = 0
                else:
                    tag = tmp
                    continue
            else: tag = 0
            show.show(num, num + 8)
        if music.get_busy() == 0 and fl != "":
            id = erase.getId(fl)
            if add.getLine() == id: id = 1
            else: id = id + 1
            fl = play.play(buildPath.buildPath(id), 0)
            show.show(num, num + 8)
        i = pygame.event.wait()
        if i.type == KEYDOWN:
            if i.key == K_1 or i.key == K_2 or i.key == K_3 or i.key == K_4 or i.key == K_5 or i.key == K_6 or i.key == K_7 or i.key == K_8 or i.key == K_9:
                if i.key == K_1: fl = play.play(buildPath.buildPath(tran(num, 1)), 0)
                elif i.key == K_2: fl = play.play(buildPath.buildPath(tran(num, 2)), 0)
                elif i.key == K_3: fl = play.play(buildPath.buildPath(tran(num, 3)), 0)
                elif i.key == K_4: fl = play.play(buildPath.buildPath(tran(num, 4)), 0)
                elif i.key == K_5: fl = play.play(buildPath.buildPath(tran(num, 5)), 0)
                elif i.key == K_6: fl = play.play(buildPath.buildPath(tran(num, 6)), 0)
                elif i.key == K_7: fl = play.play(buildPath.buildPath(tran(num, 7)), 0)
                elif i.key == K_8: fl = play.play(buildPath.buildPath(tran(num, 8)), 0)
                elif i.key == K_9: fl = play.play(buildPath.buildPath(tran(num, 9)), 0)
                if fl == "exit^": return -2
                if fl.find(".mp3") == -1:
                    tag = int(fl)
                    continue
                else: tag = 0
                show.show(num, num + 8)
            if i.key == K_a and fl != "":
                fl = play.play(fl, -1)
                if fl == "exit^": return -2
                if fl.find(".mp3") == -1:
                    tag = int(fl)
                    continue
                else: tag = 0
                show.show(num, num + 8)
            elif i.key == K_ESCAPE: return -2
            elif i.key == K_q:
                music.stop()
                return -1
            elif i.key == K_DOWN:
                sta = show.show(num + 9, num + 17)
                if sta != -1: num = num + 9
            elif i.key == K_UP:
                sta = show.show(num - 9, num - 1)
                if sta !=-1: num = num - 9
def musicUpd():
    screen.fill(BackColor)
    output.output("1：添加歌曲", 350, 100)
    output.output("2：删除歌曲", 350, 200)
    output.output("请按下相应键", 350, 300)
    output.output("q回到主页，ESC退出程序", 350, 350)
    while 1:
        i = pygame.event.wait()
        if i.type == KEYDOWN:
            if i.key == K_ESCAPE: return -2
            elif i.key == K_q: return -1
            elif i.key == K_1: add.add()
            elif i.key == K_2: erase.erase()
            screen.fill(BackColor)
            output.output("1：添加歌曲", 350, 100)
            output.output("2：删除歌曲", 350, 200)
            output.output("请按下相应键", 350, 300)
            output.output("q回到主页，ESC退出程序", 350, 350)

def main():
    screen.fill(BackColor)
    output.output("开发：周其星(Error_666)", 350, 20)
    output.output("w为进入曲库，e为管理曲库，ESC为退出程序", 350, 200)
    output.output("请按下相应键", 350, 300)
    running = 1
    while running:
        i = pygame.event.wait()
        if i.type == KEYDOWN:
            sta = 0
            if i.key == K_w: sta = musicList()
            elif i.key == K_e: sta = musicUpd()
            elif i.key == K_ESCAPE: running = 0
            if sta == -1:
                screen.fill(BackColor)
                output.output("w为进入曲库，e为管理曲库，ESC为退出程序", 350, 200)
                output.output("请按下相应键", 350, 300)
            elif sta == -2: running = 0

if __name__ == '__main__': main()