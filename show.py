# 展示歌曲列表功能

import pygame, output, add, time

pygame.init()
display = pygame.display    # 显示
music = pygame.mixer.music  # 音乐
screen = display.set_mode((700, 600))
BackColor = (87, 105, 60)

def show(l, r):
	screen.fill(BackColor)
	obj = open("txt/id.txt", "r", encoding="utf-8")
	line = obj.readline()
	if line == False or line == "":
		output.output("曲库里空空如也...", 350, 50)
		time.sleep(1)
		return -1
	if l > add.getLine(): return -1
	if l < 1: return -1
	if r > add.getLine(): r = add.getLine()
	obj.close()

	tim = 0
	cnt = 0
	obj = open("txt/id.txt", "r", encoding="utf-8")
	for line in obj:
		tim = tim + 1
		if tim >= l and tim <= r:
			line = line.strip('\n')
			g = 0
			for c in line:
				if c == ':': break
				g = g + 1
			num = int(line[0:g])
			num = num % 9
			if num == 0: num = 9
			line = str(num) + ": " + line[g + 2:]
			cnt = cnt + 1
			output.output(line, 350, 50 + (cnt - 1) * 50)
	page = str(l // 9 + 1)
	output.output("页码：" + page, 100, 50)
	output.output("输入1～9听歌，a回到正在播放，↑↓翻页", 350, 520)
	output.output("q为回到主页，ESC为退出程序", 350, 550)
	obj.close()