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
# 3.update 更像屏幕显示
pygame.display.update()

#绘制英雄的飞机
hero=pygame.image.load('./images/me1.png')
screen.blit(hero,(200,500))
screen.blit(hero,(100,300))
pygame.display.update()



time.sleep(10)




# hero_rect=pygame.Rect(100,500,120,130)

# print('英雄的原点 %d %d'% (hero_rect.x,hero_rect.y))
# print('英雄的尺寸 %d %d'% (hero_rect.width,hero_rect.height))
# print('%d %d' % hero_rect.size)

pygame.quit()