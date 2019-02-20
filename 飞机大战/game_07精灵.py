import pygame


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

#定义rect记录飞机的初始位置
hero_rect=pygame.Rect(150,300,102,126)
# --------------------以上是初始化，下面是游戏循环----------------------------------------

while 1:
    #定义内部的代码执行频率
    clock.tick(60)
    #监听事件
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            print('游戏退出')
            #卸载模块
            pygame.quit()
            #终止程序
            exit()

   
    #修改飞机位置
    hero_rect.y-=1
    #判断飞机的位置
    if hero_rect.y<=-126:
        hero_rect.y=700
    #调用blit绘制图像
    screen.blit(bg,(0,0))
    screen.blit(hero,hero_rect)
    #update
    pygame.display.update()
pygame.quit()
