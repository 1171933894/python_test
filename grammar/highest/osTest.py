# open函数r
file = open('rtest.txt', mode='r', encoding='UTF-8')
print(file.readline())
file.close()

# open函数w
file = open('wtest.txt', mode='w', encoding='UTF-8')
file.write('helloworld')
file.close()

# open函数a
file = open('atest.txt', mode='a', encoding='UTF-8')
file.write('helloworld')
file.close()

# open函数rb
src_file = open('test.png', mode='rb')
target_file = open('testCopy.png', mode='wb')
target_file.write(src_file.read())
src_file.close()
target_file.close()

# open函数a+
file = open('a+test.txt', mode='a+', encoding='UTF-8')
file.write("宇宙")
print('------------')
print(file.readline())
file.close()

# read方法
file = open('a+test.txt', mode='r',encoding='UTF-8')
# print(file.read())
# print(file.read(4))
# print(file.readline())
# print(file.readlines())
file.close()

# write方法
# file = open('wtest.txt', mode='w', encoding='UTF-8')
# lst = ['Java', 'Go', 'Python']
# file.writelines(lst) # 不添加换行符
# file.close()

# seek方法
file = open('rtest.txt', mode='r', encoding='UTF-8')
print("-----seek-----")
file.seek(3)
print(file.read())
print(file.tell())# 指针位置
print("-----seek-----")
file.close()

# 上下文管理器对象
class MyContentMgr(object):
    def __enter__(self):
        print("enter方法被调用执行了")
        return self # 注意：这里需要返回self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit方法被调用执行了")
    def show(self):
        print("show方法被调用执行了")
with MyContentMgr() as file:
    file.show()

# with操作文件
# demo1
with open('rtest.txt', mode='r', encoding='UTF-8') as file:
    print(file.read())
# demo2
with open('rtest.txt', mode='r', encoding='UTF-8') as rfile:
    with open('wtest.txt', mode='w', encoding='UTF-8') as wfile:
        wfile.write(rfile.read())

import os
# os调用系统命令
# os.system('calc.exe')
# os.system('notepad.exe')
# os.startfile('E:\\as\\sublime\\SublimeText3\\sublime_text.exe')

# 返回当前文件目录
print(os.getcwd())
# 返回文件目录/文件
lst = os.listdir('..')
print(lst)
lst = os.listdir('.')
print(lst)
# 创建目录
os.mkdir('newdir2')
# os.makedirs('newdir2/newdir3') # 创建多级目录
# 删除目录
# os.rmdir('newdir2')
os.removedirs('newdir2') # 移除多级目录
# 改变目录
print(os.getcwd())
os.chdir('..')
print(os.getcwd())

import os.path
# 获取绝对路径
print(os.path.abspath('import.py'))
# 判断文件目录是否存在
print(os.path.exists('F:\\python_test\\grammar'))
# 拼接路径
print(os.path.join("E:\\abc", 'abc.txt'))
# 分割路径
print(os.path.split('import.py'))
print(os.path.split('F:\\python_test\\grammar'))
print(os.path.splitext('demo123.py'))
print(os.path.basename('F:\\python_test\\grammar\\demo123.py'))
print(os.path.dirname('F:\\python_test\\grammar\\demo123.py'))
print(os.path.isdir('F:\\python_test\\grammar\\demo123.py'))
print(os.path.isdir('F:\\python_test\\grammar'))

# 示例demo：获取目录下所有py文件
os.chdir('highest')
for item in os.listdir(os.getcwd()):
    print(item)
    if item.endswith('py'):
        print(item)
print('-------------------')
# walk方法
lst_file=os.walk(os.getcwd())
for dirpath,dirname,filename in lst_file:
    print(dirpath)
    print(dirname)
    print(filename)
    print()