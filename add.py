# 添加歌曲功能

import pygame, output, time, shutil
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

pygame.init()
display = pygame.display    # 显示
screen = display.set_mode((700, 600))
BackColor = (87, 105, 60)

def getLine():
	tot = 0
	content = open("txt/id.txt", "r", encoding="utf-8")
	for line in content: tot = tot + 1
	content.close()
	return tot

def add():
	screen.fill(BackColor)
	file_path = filedialog.askopenfilenames()
	flag = 0
	for f in file_path:
		shutil.copy(f, "music")
		f1 = f[::-1]
		f2 = ""
		for c in f1:
			if c == '/': break
			f2 = f2 + c
		f2 = f2[::-1]
		f2 = f2[:-4]
		id = f2
		content = open("txt/id.txt", "a", encoding="utf-8")
		tot = getLine() + 1
		if tot == 1: content.write("1: " + id)
		else: content.write('\n' + str(tot) + ": " + id)
		content.close()
		flag = 1
	if flag == 1:
		output.output("添加成功！", 350, 200)
		time.sleep(3)