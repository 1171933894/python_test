# 转移字符
print('hello\nworld')
# \t表示4位个字符，所以打印出来是hello	world和helloooo	world
print('hello\tworld')
print('helloooo\tworld')
print('helloooo\rworld')  # world将hello进行了覆盖
print('hello\bworld')  # \b是退一个格，将o退没了

# 特殊注意情况
print("https:\\\\www.baidu.com")
print("老师说:\'xxxx\'")
print("老师说:'xxxx'")
# （不希望字符串中的转移字符起作用，就用原字符，如下加上r或R）
print(r'hello\nworld')
print(R'hello\nworld')

# 字符类型练习
str1 = '和我' \
       '客人'
str2 = "sfakldsjf"
str3 = '''kdsafj，
lda'''
print(str1, type(str1))
print(str2, type(str2))
print(str3, type(str3))
