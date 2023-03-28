print("Hello world!");
print(999);
print(3.14)
print(True)
print("欢迎来到Python的世界")

# 这个是注释
age = 19
money = pi = 3.14
print(money)
zhangsan,lisi,wangwu= "张三","李四","王五"
print(zhangsan)
print(lisi)
string_type = type(zhangsan)
print(string_type)
print(type(11))
a = int(3.14)
b = int("1")
print(type(a))
print(type(b))

a = float(3)
b = float("3.14")
print(type(a))
print(type(b))


str1 = str("1")
str2 = str("3.14")
str3 = str("字符串")
str4 = str("[1,2,3,4]")
print(type(str1))
print(type(str2))
print(type(str3))
print(type(str4))


res1 = bool(1)
print(str(type(res1))+" "+str(res1))
res2 = bool(0)
print(str(type(res2))+" "+str(res2))
res3 = bool([1,2,3,4])
print(str(type(res3))+" "+str(res3))
res4 = bool([])
print(str(type(res4))+" "+str(res4))
res5 = bool(None)
print(str(type(res5))+" "+str(res5))

print((2+3)*5)
print(9/3)
print(9//3)
"""
这个是注释
"""
'''
这个也是注释
'''
print('a'+'b')
# print('a'+10)
# start = input("Do you want to start(y/n)?")
# print(start)

a3 = 'a'
b3 = 'a'
print(a3.__eq__(b3))

a3_1 = 'A'
b3_1 = 'a'
print(a3_1 > b3_1)

a3_2 = '我'
b3_2 = '我'
print(a3_2 >= b3_2)
score = 90
print(60 <score <=100)
print("hello world")

num = 5
print("d结果为：%d" % (num))
print("2d结果为：%2d" % (num))
print("02d结果为：%02d" % (num))
print("-2d结果为：%-2d" % (num))
print("2d结果为：%.2d" % (num))
print("2d结果为：%.2d" % (200))

a = 8
b = 10
c = -100
print("%2d" % a)
print("%03d" % b)
print("%-3d" % b)
print("%d" % c)
print("%.4d" % c)
d = 1.345
print("%.2d" % d)
print("%.2f" % d)

print("------if判断开始------")
if(age >= 18):
    print("我已经成年了")
print("------if判断结束------")

chePiao = 1 # 用1代表有车票，0代表没有车票
if chePiao == 1:
    print("有车票，可以上火车")
    print("终于可以见到Ta了，美滋滋~~~")
else:
    print("没有车票，不能上车")
    print("亲爱的，那就下次见了，一票难求啊~~~~(>_<)~~~~")

score = 77
if score>=90 and score<=100:
    print('本次考试，等级为A')
elif score>=80 and score<90:
    print('本次考试，等级为B')
elif score>=70 and score<80:
    print('本次考试，等级为C')
elif score>=60 and score<70:
    print('本次考试，等级为D')
elif score>=0 and score<60:
   print('本次考试，等级为E')


import random
player = input('请输入：剪刀(0)  石头(1)  布(2):')
player = int(player)
computer = random.randint(0,2)
# 用来进行测试
#print('player=%d,computer=%d',(player,computer))
if ((player == 0) and (computer == 2)) or ((player ==1) and (computer == 0)) or ((player == 2) and (computer == 1)):
    print('获胜，哈哈，你太厉害了')
elif player == computer:
    print('平局，要不再来一局')
else:
    print('输了，不要走，洗洗手接着来，决战到天亮')