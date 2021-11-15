# 使用闭包来实现程序结构
# demo1：实现电子秤
# 实现思路一
def price(weight, unitPrice):
    return (weight - 0.1) * unitPrice
apple = price(10.1, 3)
print(apple)
banana = price(10.1, 5)
print(banana)

# 实现思路二
def price(unitPrice):
    def computer(weight):
        return (weight - 0.1) * unitPrice
    return computer # 一定要返回内置函数
apple = price(3)
print(apple(10.1))
banana = price(5)
print(banana(10.1))