import math

import sys

print("hello world")
# 开启Python之路
# 缩进:同一个代码块必须拥有相同的缩进空格数
if True:
    print("if True")
    print("It is True")
else:
    print("else")
    print("It is False")
# print("iii")

# 多行语句使用(\)来拼接
total = "ha lo" + \
        "lsjdsda"
total1 = ["a", "b" +
          "c" + 'd']
print(total)
print(total1)

print(int(34.67))

a = 43.3
print(math.ceil(a))
print(math.pi)

# 生成器函数 yield


def fibonacci(n):
    x, y, count2 = 0, 1, 0
    while True:
        if count2 > n:
            return
        yield x  # 保存运行信息
        x, y = y, x+y
        count2 += 1
f = fibonacci(10)
while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()



