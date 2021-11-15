# re包的使用
import re
x = 'heyuanxin学习Python课程，在CSDN的课程'
print(re.search('，', x))# 全字符串查找
print(re.match('heyuanxin', x))# 以heyuanxin开头
print(re.split('，', x))
print(re.findall('[nN]', x))

print('模式具体使用')
# 模式具体使用
r = re.compile('[0-9]')
x = '今天是2021:06:23'
print(r.search(x))
print(r.match(x))
print(r.findall(x))
r = re.compile(':')
print(r.split(x))