for item in 'Python':
    print(item)

for item in range(10):
    print(item)

# 如果用不到自定义变量，那么可以写为”_“
for _ in range(10) :
    print("人生苦短，我用Python")

# 求和1到100的偶数和
sum=0
for i in range(1,101) :
    if i % 2 == 0 :
        sum += i
print(sum)