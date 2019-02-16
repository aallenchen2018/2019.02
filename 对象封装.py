# class skill:
#     def __init__(self,name,damage,damana):
#         self.sname=name
#         self.伤害生命=damage
#         self.伤害魔法=damana

#     def __str__(self):
#         return ('%s have %d 点伤害 和%d 点蓝量损失'%(self.sname ,self.伤害生命 , self.伤害魔法))

# class 英雄:
#     def __init__(self,hname,health,mana):
#         self.hname=hname
#         self.health=health
#         self.mana=mana
#         self.realheal=health
#         self.realmana=mana
#         self.skill_list=[]

#     def __str__(self):
#         return ('英雄名字%s, 英雄生命值: %d,魔法值: %d, 英雄剩余生命: %d, 英雄剩余魔法值: %d'%(self.hname, self.health, self.mana ,self.realheal, self.realmana))
    
#     def add_skill(self,技能):
#         print(' %s 被 %s 技能击中,受到 %d点的伤害和 %d 魔法损失'%(self.hname,技能.sname,技能.伤害生命,技能.伤害魔法))
#         self.skill_list.append(技能.sname)
#         if 技能.伤害生命>self.realheal:
            

#             print('%s over damage,target death'% 技能.sname)
#             self.realheal=0
#             return
        

#         self.realheal-=技能.伤害生命
#         self.realmana-=技能.伤害魔法
#         if self.realmana<0:
#             self.realmana=0
        
# 秘书银蛇=skill('秘书银蛇',650,800)
# 抽蓝=skill('抽蓝',450,200)

# 大帝=英雄('大帝',1600,550)
# 剑圣=英雄('剑圣',1350,600)

# 大帝.add_skill(秘书银蛇)
# 剑圣.add_skill(抽蓝)

# print(大帝)
# print(剑圣)
from random import randint
class skill:
    def __init__(self,name,damage,damana):
        self.sname=name
        self.伤害生命=damage
        self.伤害魔法=damana
    def __str__(self):
        return ('%s have %d 点伤害 和 %d 点蓝量损失'%(self.sname,self.伤害生命,self.伤害魔法))

class 英雄:
    def __init__(self,hname,health,mana):
        self.hname=hname
        self.health=health
        self.mana=mana
        self.realheal=health
        self.skill_list=[]
        self.realmana=mana
    def __str__(self):
        return ('英雄名字%s, 英雄生命值: %d,魔法值: %d, 英雄剩余生命: %d, 英雄剩余魔法值: %d'%(self.hname, self.health, self.mana ,self.realheal, self.realmana))
    def add_skill(self,技能):
        print(' %s 被 %s 技能击中,受到 %d点的伤害和 %d 魔法损失'%(self.hname,技能.sname,技能.伤害生命,技能.伤害魔法))
        
        self.skill_list.append(技能.sname)
        
       

        if 技能.伤害生命> self.realheal:
            print('%s over damage,target death'% 技能.sname)
            self.realtheal=0
            return
        self.realheal-=技能.伤害生命
        self.realmana-=技能.伤害魔法

        if self.realmana<0:
            self.realmana=0
#设置变量
火焰爆轰=skill('火焰爆轰',500,200)
抽蓝=skill('抽蓝',500,600)

恐怖利刃=英雄('恐怖利刃',1350,600)
虚空假面=英雄('虚空假面',1250,500)

恐怖利刃.add_skill(火焰爆轰)
虚空假面.add_skill(抽蓝)


print(恐怖利刃)
print(虚空假面)



