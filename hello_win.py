#!/usr/bin/python
# -*- coding: utf-8 -*-
#from http://morc-blog.logdown.com/posts/195045-hello-world-in-python-and-pygame


# 載入 pygame 模組
import pygame
# 初始化 pygame
pygame.init()
# 設定 pygame 視窗標題 (caption)
pygame.display.set_caption("Hello Python")
# 設定 pygame 視窗大小 (640 x 480)
pygame.display.set_mode((640, 480))
# 將 pygame 視窗顯示在螢幕上
pygame.display.flip()
# 無窮迴圈
while True:
    # 取得 pygame 的事件 (event)
    event = pygame.event.wait()
    # 如果視窗的 x 被按下，就結束迴圈
    if event.type == pygame.QUIT:
        break
# 釋放 pygame 的資源
pygame.quit()

# end of Hello.py
