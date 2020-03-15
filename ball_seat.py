
import random

seat_lenght,seat_wighat=eval(input('请输入座位席的长宽座位数量：'))
list=[]
for seat in range(seat_lenght):            #i为一个一维数组
    list.append([])
    for j in range(seat_wighat):
        list[seat].append(random.randint(0,1))
    print(list[seat])
# print(list[1])
# print(len(list))
'''
将生成的二维列表转变成一维列表
'''
i=0
list_1=[]
while i<len(list):
    list_1=list_1+list[i]
    i+=1
# print(list_1)
'''
将每个有人坐的位置用一维列表表示出来
'''
a=0
list_2=[]
while a<len(list_1):
    if list_1[a]==1:
        list_2.append(a)
        # print(a,end=' ')
    a+=1
print(list_2)

z=0
b=0
list_4=[]
while b<len(list_2):
    list_3= [list_2[b]]
    c = 1
    while c<len(list_2):
        if list_2[b]+1==list_2[c]:
            list_3.append(list_2[c])
        elif list_2[b]+seat_lenght==list_2[c]:
            list_3.append(list_2[c])
        elif list_2[b]+seat_lenght+1==list_2[c]:
            list_3.append(list_2[c])
        elif list_2[b]-1==list_2[c]and list_2[b]-1>=0:
            list_3.append(list_2[c])
        elif list_2[b]+seat_lenght-1==list_2[c]and list_2[b]+seat_lenght-1>=0and seat_lenght-1>=0:
            list_3.append(list_2[c])
        elif list_2[b]-seat_lenght==list_2[c]and list_2[b]-seat_lenght>=0:
            list_3.append(list_2[c])
        elif list_2[b]-seat_lenght-1==list_2[c]and list_2[b]-seat_lenght-1>=0and seat_lenght-1>=0:
            list_3.append(list_2[c])
        elif list_2[b]-seat_lenght+1==list_2[c]and list_2[b]+1-seat_lenght>=0:
            list_3.append(list_2[c])
        c=c+1
    b=b+1
    print(list_3)
    list_4.append(list_3)
print(list_4)

