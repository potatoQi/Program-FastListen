# 输出功能

import pygame

pygame.init()
display = pygame.display    # 显示
font = pygame.font.Font("font/msyh.ttf", 16) # 文字
screen = display.set_mode((700, 600))
color = (255, 255, 255)

def output(word, x, y):
	obj = font.render(word, True, color) # 定义对象
	xy = obj.get_rect() # 获得要显示的对象的rect
	xy.center = (x, y) # 重新设置坐标
	screen.blit(obj, xy) # 绘制字体 47,79,79
	display.update()