
import random

MinNum=int(input('请输入要猜测数字范围的最小值：'))
MaxNum=int(input('请输入要猜测数字范围的最大值：'))
Num=random.randint(MinNum,MaxNum)
count=1   #记录猜测的次数
while count<1000:
    GuessNum = int(input('请输入猜测的数字：'))
    if GuessNum == Num:
        print('猜测正确')
        print('猜测了%d次'%count)
        break
    elif GuessNum < Num:
        print('猜测的数太小了')
        count=count+1
        continue
    else:
        print('猜测的数太大了')
        count=count+1
        continue