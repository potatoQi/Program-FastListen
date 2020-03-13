# 删除歌曲功能

import pygame, output, add, time, os
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

pygame.init()
display = pygame.display    # 显示
screen = display.set_mode((700, 600))
BackColor = (87, 105, 60)

def getName(f):
	f1 = f[::-1]
	f2 = ""
	for c in f1:
		if c == '/': break
		f2 = f2 + c
	f2 = f2[::-1]
	f2 = f2[:-4]
	return f2

def getId(fl):
	name = getName(fl)
	ans = 0
	with open('txt/id.txt', encoding = "utf-8") as obj:
		for line in obj:
			ans = ans + 1
			line = line.strip('\n')
			pos = 2
			for c in line:
				if c == ":":
					break
				else:
					pos = pos + 1
			line = line[pos:]
			if line == name: break
	return ans

def erase():
	tag = 0
	file_path = filedialog.askopenfilenames(initialdir='music')
	for f in file_path:
		tag = 1
		id = getName(f)
		tot = 0
		with open('txt/id.txt', encoding = "utf-8") as fr, open('txt/.id.txt', 'a', encoding = "utf-8") as fm:
			for line in fr:
				line = line.strip('\n')
				pos = 2
				for c in line:
					if c == ":": break
					else: pos = pos + 1
				line = line[pos:]
				if line != id:
					tot = tot + 1
					if tot == 1: fm.write("1: " + line)
					else: fm.write('\n' + str(tot) + ": " + line)
		pygame.mixer.music.load(r"music/用户切忌这个文件不能删.mp3") # 为了确保删除指定歌曲时，指定歌曲不被占用！
		os.remove("music/" + id + ".mp3")
		os.remove('txt/id.txt')
		os.rename('txt/.id.txt', 'txt/id.txt')
	if tag == 1:
		screen.fill(BackColor)
		output.output("删除成功！", 350, 200)
		time.sleep(3)