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

        #4.设置定时器事件-创建敌机  ls  (毫秒)
        pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)
 
    def __create_sprites(self):
        #创建背景精灵和精灵组
        bg1=Background()
        bg2=Background(True)
        
        self.back_group=pygame.sprite.Group(bg1,bg2)
        #创建敌机的精灵组
        self.enemy_group=pygame.sprite.Group()

    def start_game(self):
        print('游戏快开始...')

        #游戏循环
        while 1:
            #1.设置刷新频率
            self.clock.tick(FRAME_PER_SEC)
            #2.事件监听
            self.__event_handler()
            #3.碰撞检测
            self.__check__collide()
            #4.更新/绘制精灵组
            self.__update_sprites()
            #5.更新显示
            pygame.display.update()
        

    def __event_handler(self):
        #用这个方法来返回当前的操作信息
        for event in pygame.event.get():
            #判断是否退出游戏(类名+函数调用静态方法)
            if event.type==pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type==CREATE_ENEMY_EVENT:
                print('敌机出场...')
                #创建敌机精灵
                enemy= Enemy()

                #将敌机精灵添加到敌机精灵组
                self.enemy_group.add(enemy)
    def __check__collide(self):
        pass
    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

    #静态方法
    @staticmethod
    def __game_over():
        print('游戏结束...')

        pygame.quit()
        exit()

if __name__ == "__main__":
    #创建游戏对象
    game=PlaneGame()
    #启动游戏
    game.start_game()
    