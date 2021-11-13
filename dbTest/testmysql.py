# 导入pymysql模块
import pymysql

print(pymysql.apilevel)  # api版本
print(pymysql.paramstyle)

# 打开数据库连接
conn = pymysql.connect(host='localhost', user='root', password='root', db='test', port=3306)
# 使用cursor()方法获取操作游标
cursor = conn.cursor()
# 1、建表结构
# cTableSql = 'create table lesson(' \
#             'id varchar(20) PRIMARY KEY,' \
#             'name varchar(20))'
# print(cursor.execute(cTableSql))
# 2、插入数据
# cursor.execute('insert into lesson(id, name) values (%s, %s)', ['001', '张三'])
# cursor.execute('insert into lesson(id, name) values (%s, %s)', ['002', '李四'])
# cursor.execute('insert into lesson(id, name) values (%s, %s)', ['003', '王五'])
# conn.commit()
# 3、查询数据
try:
    cursor.execute('select * from lesson')
    result = cursor.fetchall()
    print(result)  # 元组
    for item in result:
        print(item)  # 元素
except Exception as e:
    raise e # 重新抛出异常
finally:
    pass
cursor.close()
conn.close()
