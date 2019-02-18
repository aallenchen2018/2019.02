import pygame
import time

pygame.init()
#创建游戏的窗口
screen=pygame.display.set_mode((480,700))

#绘制背景图像
# 1.加载图像数据
bg=pygame.image.load('./images/background.png')
# 2.blit 绘制背景图像
screen.blit(bg,(0,0))

# # 3.update 更像屏幕显示可以省去用后面的update
# pygame.display.update()

#绘制英雄的飞机
hero=pygame.image.load('./images/me1.png')
screen.blit(hero,(200,500))

pygame.display.update()



time.sleep(10)

pygame.quit()
