# 入门DEMO

# 输出字符串
print("hello world")
print('hello world')
print('1', '2', '3')# 不进行输出（输出内容在一行当中）

# 输出数字
print(3.25)

# 输出运算符表达式
print(3 + 1)

# 将数据输出文件中（注意点：1、所指定的盘符存在；2、使用file=fp）
fp = open('C:\\Users\\HeYX\\Desktop\\text.txt', 'a+')  # a+表示如果文件不存在就创建，存在就在文件内容的后面继续追加
print('helloworld123', file=fp)
fp.close()