import pygame
class GameSprite(pygame.sprite.Sprite):
    def __init__(self,image_name,speed=1):

        #由于父类不是object基类 ，调用父类的初始化方法,如果不调用,就用不了父类的初始化方法
        super().__init__()
        #定义对线属性
        self.image=pygame.image.load(image_name)
        self.rect=self.image.get_rect()
        self.speed=speed
        
    def update(self):
        #在屏幕的垂直方向上移动
        self.rect.y +=self.speed


