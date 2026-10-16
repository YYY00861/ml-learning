import random

secret = random.randint(1, 1000)
guess_count = 0

print("我想了一个1到1000的数字，你猜猜看。")

while True:
    guess = int(input("请输入你猜的数字："))
    guess_count = guess_count + 1
    if guess_count == 6:
        print("咋这样")

    if guess < secret:
        print("小了，往大猜。")
    elif guess > secret:
        print("大了，往小猜。")
    else:
        print(f"猜对了，你一共猜了{guess_count}次。")
        if guess_count == 1:
            print("真棒")
        elif guess_count <= 4:
            print("还行")
        else:
            print("一般般")
        break
