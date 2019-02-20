import time,pygame
count=0
a=int(input('请输入时间:'))
b=a*60
while(count<b):
    timy=b-count
    m,s=divmod(timy,60)
    h,m=divmod(m,60)
    print('%d:%d:%d'%(h,m,s))
    time.sleep(1)
    count+=1
print('计时结束!')


 
pygame.mixer.init()
#加载音乐
pygame.mixer.music.load("C:\\Users\\34678\\Music\\VipSongsDownload\\music\\华晨宇 - 齐天.mp3")
while True:
	#检查音乐流播放，有返回True，没有返回False
	#如果没有音乐流则选择播放
	if pygame.mixer.music.get_busy()==False:

            pygame.mixer.music.play()
