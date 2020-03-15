#写一个循环，不断的问用户想买什么，用户选择一个商品编号，就把对应的商品添加到购物车里，
# 最终用户输入q退出时，打印购物车里的商品列表

shop_list=[['iphone',7299],['samsung',5000],['huawei',7000]]
shop_car=[]
while True:
    print('商品有如下：')
    for shop in enumerate(shop_list):
        print(shop)
    user=input('输入想要购买的产品编号或退出（退出请输入q）：')
    if user.isdigit():    #isdigit()判断变量是什么类型
        users=int(user)
        if users>=0 and users<(len(shop_list)):
            shop_car.append(shop_list[users])
            # print('购物车里的商品是%s'%shop_car)

        else:
            print('没有此商品')
    elif user=='q':
        print('购物车里的商品是%s' % shop_car)
        break