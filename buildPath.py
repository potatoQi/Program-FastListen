# 生成歌曲路径

import pygame

pygame.init()
display = pygame.display    # 显示
screen = display.set_mode((700, 600))

def buildPath(id):
	obj = open("txt/id.txt", "r", encoding="utf-8")
	tim = 0
	for line in obj:
		tim = tim + 1
		line = line.strip('\n')
		if tim == id:
			tim = 0
			pos = -1
			for c in line:
				if c == ':':
					pos = tim + 2
					break
				tim = tim + 1
			line = line[pos:]
			obj.close()
			return "music/" + line + ".mp3"
	obj.close()
	return "error"