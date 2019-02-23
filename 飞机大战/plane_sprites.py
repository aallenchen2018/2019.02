import pygame
SCREEN_RECT=pygame.Rect(0,0,480,700)
FRAME_PER_SEC=60
class GameSprite(pygame.sprite.Sprite):
    def __init__(self,image_name,speed=1):

        #由于父类不是object基类 ，调用父类的初始化方法,如果不调用,就用不了父类的初始化方法
        super().__init__()
        #定义对线属性
        self.image=pygame.image.load(r'C:\GitHub\2019.02代码\飞机大战\images\background.png')
        self.rect=self.image.get_rect()
        self.speed=speed 
        
    def update(self):
        #在屏幕的垂直方向上移动
        self.rect.y +=self.speed
#子类针对特有的需求,重写父类的方法,并且进行扩展
class Background(GameSprite):
    ##游戏的背景精灵###
    def __init__(self,is_alt=False):
        #1调用父类方法实现精灵的创建
        super().__init__('./images/background.png')
        #2判断是否是交替图像,如果是设置位置
        if is_alt:
            self.rect.y=-self.rect.height
    def update(self):
        #1.调用父类的方法实现
        super().update()
        #2.判断是否移出屏幕,如果移出了屏幕调到上方
        if self.rect.y>=SCREEN_RECT.height:
            self.rect.y=-self.rect.height
        
