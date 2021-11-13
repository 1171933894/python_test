# 全局变量
c = 1
def fun(a, b):
    print(c + a + b)
    global age # 局部变量添加global修饰，变成全局变量
    age = 20
fun(1, 2)
print(c)
print(age)