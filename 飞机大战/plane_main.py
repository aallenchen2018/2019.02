import pygame
from plane_sprites import*
 
class PlaneGame(object):
    def __init__(self):
        print('游戏初始化')
        #1.创建游戏的窗口
        self.screen=pygame.display.set_mode(SCREEN_RECT.size)
        #2.创建游戏的始终
        self.clock=pygame.time.Clock()
        #3.调用私有方法,精灵和精灵组的创建
        self.__create_sprites()
 
    def __create_sprites(self):
        pass

    def start_game(self):
        print('游戏快开始...')

        #游戏循环
        while 1:
            #1.设置刷新频率
            #2.事件监听
            #3.碰撞检测
            #4.更新/绘制精灵
            #5.更新显示
            pass

    def __event_handler(self):
        pass

if __name__ == "__main__":
    #创建游戏对象
    game=PlaneGame()
    #启动游戏
    game.start_game()
    