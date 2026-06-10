#1.if条件
age = 18
if age >=18:
    print("你已经成年了!")
else:
    print("你还未成年!")
#2.多条件判断
score = 85
if score >= 90:
    print("成绩优秀!")
elif score >= 60: 
    print("成绩及格!")
else:
    print("成绩不及格!")
#3.循环
#3.1 for循环
#遍历列表
fruits = ["苹果","香蕉","橘子"]
for fruit in fruits:
    print("我喜欢吃"+fruit)
#使用range函数
for i in range(5):
    print("这是第",i,"次循环")
for i in range(1,6):
    print("这是第"+str(i)+"次循环")
#3.2 while循环
count = 0
while count < 5:
    print("这是第"+str(count)+"次循环")
    count += 1

#练习：
#1.输入一个数字，判断它是奇数还是偶数。
number = input("请输入一个数字：")
number = int(number)
if number % 2 == 0:
    print("这个数字是偶数。")
else:
    print("这个数字是奇数。")

#2.用for循环得到1到100的和。
sum = 0
for i in range(1,101):
    sum += i
print("1到100的和是：",sum)