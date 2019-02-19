import pygame
import time

pygame.init()
#创建游戏的窗口
screen=pygame.display.set_mode((480,700))

#绘制背景图像
# 1.加载图像数据
bg=pygame.image.load(r'C:\GitHub\2019.02代码\飞机大战\images\background.png')
# 2.blit 绘制背景图像
screen.blit(bg,(0,0))

# # 3.update 更像屏幕显示可以省去用后面的update
pygame.display.update()

#绘制英雄的飞机
hero=pygame.image.load(r'C:\GitHub\2019.02代码\飞机大战\images\me1.png')
screen.blit(hero,(200,500))

pygame.display.update()
#始终对象
clock=pygame.time.Clock()

# --------------------以上是初始化，下面是游戏循环----------------------------------------
i=0
while 1:
    clock.tick(60)
    print(i)

pygame.quit()
