print('--iter函数--')
# 迭代器操作iter函数（没有for-in方便）
x = ['CSDN', 'Python', 'heyuanxin']
i = iter(x)
print(next(i))
print(next(i))
print(next(i))
# 多一个就报错
# print(next(i))
print()

print('--for-in--')
# for-in操作
for item in x:
    print(item)
print()