# 数据类型为class int
print(type(10))

# 类的创建
class Student:  # 类名首字母大写
    native_place = '成都'  # 类属性

    def __init__(self, name, age):
        self.name = name  # 实例属性
        self.age = age  # 实例属性

    # 实例方法
    def eat(self):
        print('学生在吃饭...')

    # 静态方法
    @staticmethod
    def method():
        print("staticmethod")

    # 类方法
    @classmethod
    def cm(cls):
        print('classmethod')


class Student1:  # 类名首字母大写
    pass

# 查看类对象
print(id(Student))
print(type(Student))
print(Student)
print(Student1)

# 创建实例对象
stu1 = Student('hyx', 29)
print(stu1)
print(id(stu1))
print(type(stu1))
stu1.eat()
print(stu1.name, ' ', stu1.age)
Student.eat(stu1)  # 同stu1.eat()

# 类属性的使用
print(Student.native_place)
stu1 = Student('hyx1', 29)
stu2 = Student('hyx2', 30)
print(stu1.native_place)
print(stu2.native_place)
Student.native_place = "北京"
print(stu1.native_place)
print(stu2.native_place)

# 类方法的使用
Student.cm()

# 静态方法的使用
Student.method()

# 动态绑定属性和方法
# 绑定属性
stu2.gender = '女'
print(stu2.gender)
# 绑定方法
stu2.eat()
def show():
    print("show()")
stu2.show = show
stu2.show()

# 类的封装
class Student2:
    def __init__(self,name,age):
        self.name=name
        self.__age=age # 不希望被外部使用，前面加__
    def show(self):
        print(self.name,self.__age)
stu2=Student2('hhh',29)
print(stu2)
print(id(stu2))
stu2.show()
# print(stu2.__age) 抛错AttributeError，但是可以通过以下方式进行访问
print(dir(stu2))
print(stu2._Student2__age)

# 类的继承
class Person(object):# Person继承object类
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(self.name,self.age)
class Student(Person):
    def __init__(self,name,age,no):
        super().__init__(name,age)
        self.no=no
    def info(self):
        print('-----')
        super().info()
        print(self.no)
        print('-----')
class Teacher(Person):
    def __init__(self,name,age,toy):
        super().__init__(name,age)
        self.toy=toy
    def info(self):
        print('-----')
        super().info()
        print(self.toy)
        print('-----')
stu5=Student('hhh',29,'1101')
tea5=Teacher('hhh',29,10)
stu5.info()
tea5.info()

# 方法重写
class Person(object):# Person继承object类
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(self.name,self.age)
class Student(Person):
    def __init__(self,name,age,no):
        super().__init__(name,age)
        self.no=no
    def info(self):
        print('-----')
        super().info()
        print(self.no)
        print('-----')
class Teacher(Person):
    def __init__(self,name,age,toy):
        super().__init__(name,age)
        self.toy=toy
    def info(self):
        print('-----')
        super().info()
        print(self.toy)
        print('-----')
    def __str__(self):
        return '重写了'
stu5=Student('hhh',29,'1101')
tea5=Teacher('hhh',29,10)
stu5.info()
tea5.info()
# 重写__str__
tea5=Teacher('hhh',29,10)
print(tea5) # 默认调用__str__

# 类的多态
class Animal(object):
    def eat(self):
        print('动物会吃')
class Dog(Animal):
    def eat(self):
        print('狗啃骨头')
class Cat(Animal):
    def eat(self):
        print('猫吃鱼')
class Person:
    def eat(self):
        print('人吃饭')
def fun7(obj):
    obj.eat()
fun7(Animal())
fun7(Dog())
fun7(Cat())

# 对象特殊属性
# __dict__属性，查看对象属性字典
print(tea5.__dict__)
# __class__对象所属类
print(tea5.__class__)
# __bases__类的父类型的元素
print(Teacher.__bases__)
print(Teacher.__base__)
# __mro__类的层次结构
print(Teacher.__mro__)
# __subclasses__方法表示子类个数
print(Animal.__subclasses__())

# 对象特殊方法
# __add__
a = 10
b = 20
c = a + b
d = a.__add__(b)
print(c, d)
class Num:
    def __init__(self, num):
        self.num = num
    def __add__(self, other):
        return self.num+other.num
    def __len__(self):
        return 1
n1 = Num(1)
n2 = Num(2)
print(n1+n2)
# __len__
lst = [1, 2, 3]
print(len(lst))
print(lst.__len__())
print(n1.__len__())
print(len(n1))
# __new__方法
class Test:
    def __new__(cls, *args, **kwargs):
        print('__new__被调用了cls的id值为{0}'.format(id(cls)))
        obj = super().__new__(cls)
        print('创建的对象id为:{0}'.format(id(obj)))
        return obj
    def __init__(self,name,age):
        print('__init__方法被调用了，self的id值为:{0}'.format(id(self)))
        self.name=name
        self.age=age
print('object这个类对象的id为{0}'.format(id(object)))
print('Test这个类对象的id为{0}'.format(id(Test)))
t1 = Test('hyx', 29)
print('Test实例对象id为{0}'.format(id(t1)))
print(t1.name, t1.age)

# 深浅拷贝
class CPU:
    pass
class Disk:
    pass
class Computer:
    def __init__(self, cpu, disk):
        self.cpu = cpu
        self.disk = disk
# 变量赋值
cpu1 = CPU()
cpu2 = cpu1
print(id(cpu1), id(cpu2))
# 浅拷贝demo
import copy
disk = Disk()
cpu = CPU()
computer1 = Computer(cpu, disk)
computer2 = copy.copy(computer1)
print(computer1, computer1.cpu, computer1.disk)
print(computer2, computer2.cpu, computer2.disk)
# 深拷贝demo
computer3 = copy.deepcopy(computer1)
print(computer3, computer3.cpu, computer3.disk)
