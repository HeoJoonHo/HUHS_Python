from random import *

fulllist = range(1,21)
fulllist = list(fulllist)
shuffle(fulllist)
win = sample(fulllist, 4)
print(" -- 당첨자 발표 -- ")
print("치킨 당첨자: {} \n커피 당첨자: {}, {}, {}".format(win[0], win[1], win[2], win[3]))
print(" -- 축하합니다 -- ")