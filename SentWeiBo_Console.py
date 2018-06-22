# coding:utf-8
import optparse
import random
from weibo import APIClient
import datetime
import time
import os
#################################################################################
u''' 
  一个可以定时发送微博的小脚本
  -h, --help          show this help message and exit
  -t T, --time=T      -t 设定每天几点发。如 -t 8；默认4点发，24小时制。
  -p, --picture       -p 随机发送图片
  -y, --yingyingying  -y 报时+卖萌
  -r, --random        -r 每天从以上内容中随机选择一种发送
  例如 python SentWeiBo_Console.py -h 19 -p 就是每天19点发送一次图片

'''
################################################################################
#新浪微博API的验证信息
APP_KEY = '782542634' # app key
APP_SECRET = 'b5e3473a613bd8c740dc6b3b2d2a9550' # app secret
CALLBACK_URL = 'https://api.weibo.com/oauth2/default.html' # callback url

access_token = "2.00VfLpvC05FTxq9a86b1e3f5rjTuVC"
expires_in = 1660225135

client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
client.set_access_token(access_token, expires_in)
#################################################################################
#命令行
parser = optparse.OptionParser()

parser.add_option('-t','--time',dest='t',default="4",type='string',help = u'-t 设定每天几点发。如 -t 8；默认4点发，24小时制。')
# parser.add_option('-f','--frequency',dest='f',default="days=1",type='string',help = u'-t 设定发送频率,默认一天一次')
parser.add_option('-p','--picture',action="store_true",dest='p',help = u'-p 随机发送图片')
parser.add_option('-y','--yingyingying',action="store_true",dest='y',help = u'-y 报时+卖萌')
parser.add_option('-r','--random',action="store_true",dest='r',help = u'-r 每天从以上内容中随机选择一种发送')

(option, args) = parser.parse_args()
c = int(option.t)
pic = option.p
ying = option.y
ran = option.r
# f = option.f
aaa = ['pic','ying']
##########################################################################################
#功能函数
def yingyingying():#报时+颜表情卖萌
    TimeSecound = time.time()
    date = time.localtime(TimeSecound)  # 现在的具体时间
    DateMday = date[2]
    DateHour = date[3]

    str = u'''咚~咚~咚~%s,现在是%d年%d月%d日%d时%d分%d秒,
         现在我有其他功能了哦~  http://www.google.com 404喽%s''' % (random.choice(
            [u'(๑•̀ㅂ•́)و✧', u'ヾ(≧▽≦*)o ', u'o(*≧▽≦)ツ ', u'(o゜▽゜)o☆', u'<(￣︶￣)>', u'o(*￣▽￣*)o ', u'(｡･∀･)ﾉﾞ',
             u'ヾ(≧∇≦*)ゝ',
             u'Hi~ o(*￣▽￣*)ブ ', u'(≧∀≦)ゞ', u'ε(*´･∀･｀)зﾞ', u'(～￣▽￣)～ ', u'︿(￣︶￣)︿', u'(/≧▽≦)/', u'(ﾉ*･ω･)ﾉ',
             u'o(〃\'▽\'〃)o ', u'o(￣▽￣)ｄ ', u'o(^▽^)o']), date[0], date[1], DateMday, DateHour, date[4], date[5],
                                                         random.choice(
                                                             [u'w(ﾟДﾟ)w', u'Ｏ(≧口≦)Ｏ', u'Σ(｀д′*ノ)ノ', u'ヽ(*。>Д<)o゜',
                                                              u'┻━┻︵╰(‵□′)╯︵┻━┻', u'φ(-ω-*)', u'(σ｀д′)σ',
                                                              u'(#`O′)', u'( >ρ < ”)', u'o(一︿一+)o', u'(#`O′) ',
                                                              u'(＞﹏＜)', u'(；′⌒`) ', u'（；´д｀）ゞ', u'Σ( ° △ °|||)︴',
                                                              u'(lll￢ω￢)', u'…（⊙＿⊙；）…', u'_〆(´Д｀ ) ',
                                                              u'Σ(っ °Д °;)っ', u'(・-・*)', u'(°ー°〃) ',
                                                              u'(((φ(◎ロ◎;)φ)))', u'o((⊙﹏⊙))o.', u'ヽ(*。>Д<)o゜ ', ]))
    client.statuses.share.post(status=str)  # 这是有返回值的

def picture():#随机发送图片
    with open('./haha.txt', 'r') as f:
        a = f.read()
    a = a.split('\r\n\r\n')
    haha = random.choice(a)
    a.remove(haha)
    with open('./haha.txt', 'w') as f:
        for i in a:
            if i == '' or i == '\n':
                a.remove(i)
                continue
            f.write(i)
            f.write('\r\n')
            f.write('\r\n')

    picture = random.choice(piclist)
    piclist.remove(picture)
    str = '%s\nhttp://www.google.com图文无关' % haha
    pic = open('./pic/%s' % picture, 'rb')
    client.statuses.share.post(status=str, pic=pic)
    pic.close()
    os.remove('./pic/' + picture)

def jiangzemin(f):#判断时间到没到，到了就执行f()
    while True:
        t = datetime.datetime.now()
        schedtime = datetime.datetime(t.year, t.month, t.day, c, c, c)  # 要执行的时间
        time.sleep(1)  # 循环执行的速度太快，虽然只有一秒但也会执行很多次,所以要等1s

        now = datetime.datetime.now()  # 返回值里面有微秒可把我坑惨了
        if now.date() == schedtime.date():  # 先判断日期相不相同
            if (now.hour == schedtime.hour) and (now.minute == schedtime.minute) and (now.second == schedtime.second):  # 在判断时间相不相同，主要是为了避开微秒的比较
                f()
                # schedtime = schedtime + Frequency
                print now, u"sent successfully"
            else:
                pass
        else:
            pass

def randomm():#随机选一个函数执行
    r = random.choice(aaa)
    if r == 'pic':
        picture()
    if r == 'ying':
        yingyingying()
################################################################################

if __name__ == '__main__':
    piclist = os.listdir('./pic/')#放图片的目录
    Frequency = datetime.timedelta(days=1)# 频率

    if ran == None:
        if (pic == None and ying == None) or (not pic == None and not ying == None):
            print  u'参数有误'
            exit(0)
        if not pic == None:
            jiangzemin(picture)
        if not ying == None:
            jiangzemin(yingyingying)
    if ran == True:
        jiangzemin(randomm)
