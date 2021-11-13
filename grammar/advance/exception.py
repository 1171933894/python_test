# try-except-else-finally语法结构
try:
    num = 10 / 0
except BaseException as e:
    print("error->", e)
else:
    print("succ->", num)
finally:
    print("谢谢您的使用")

# traceback模块
import traceback
try:
    print("-------")
    print(10 / 0)
except:
    traceback.print_exc()