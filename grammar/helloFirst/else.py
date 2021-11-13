a = 0
while a < 51:
    a += 1
    if a % 5 != 0:
        continue
    print(a)
else:
    print('已打印完成', a)

for i in range(51):
    if i % 5 != 0:
        continue
    print(i)
else:
    print('已打印完成', i)
