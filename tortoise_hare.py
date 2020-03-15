import random
import time

road=('_'*70)
tortoise_place=1
hare_place=1
# print(road)
print("BANG !!!!! AND THEY' RE OFF !!!!!")
while True:
    Num = random.randint(1, 10)  # 随机生成1~10中的数
    # print(Num)
    time.sleep(1)                #循环时间为1秒
    '''
    乌龟的运动轨迹
    '''
    # print(tortoise_place)
    if Num<=5:
        tortoise_place=tortoise_place+3
    elif Num>=8:
        tortoise_place=tortoise_place+1
    else:
        tortoise_place=tortoise_place-6
    if tortoise_place<1:
        tortoise_place=1
    print(tortoise_place)
    # road = road[:tortoise_place-1] + 'T' + road[tortoise_place:]
    '''
    兔子的运动轨迹
    '''
    # print(hare_place)
    if Num<=2:
        hare_place=hare_place
    elif Num<=4 and Num>2:
        hare_place=hare_place+9
    elif Num<=5 and Num>4:
        hare_place=hare_place-12
    elif Num<=8 and Num>5:
        hare_place=hare_place+1
    else:
        hare_place=hare_place-2
    if hare_place<1:
        hare_place=1
    print(hare_place)
    # road = road[:hare_place - 1] + 'H' + road[hare_place:]
    # print(road)
    road=('_'*70)
    if tortoise_place>=70:
        print('TORTOISE WINS!!!YAY!!!')
        break
    elif hare_place>=70:
        print('Hare wins!!!Yush!!!')
        break
    elif hare_place==tortoise_place:
        road = road[:hare_place - 1] + 'O' + road[hare_place:]
        print(road)
    else:
        road = road[:tortoise_place - 1] + 'T' + road[tortoise_place:]
        road = road[:hare_place - 1] + 'H' + road[hare_place:]
        print(road)