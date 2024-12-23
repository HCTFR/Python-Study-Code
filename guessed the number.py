import random #导入随机模块
numbers=random.randint(1,100) #随机数字
att=0 #设置初始化次数
print("guess number 1-100")
while True:
    guess=int(input("Enter you guess number:"))
    att+=1
    if guess > numbers:
        print("too,hight")
    elif guess < numbers:
        print("too,low")
    else:
        print(f",yes,the numbers is {numbers} and you spent {att}")
        break
