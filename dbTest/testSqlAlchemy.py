from sqlalchemy import Column, create_engine, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 定义ORM模型
Base = declarative_base()

class math(Base):
    __tablename__ = 'lesson'# 填写表名
    id = Column(String(20), primary_key=True)
    name = Column(String(50))

engine = create_engine("mysql+mysqlconnector://root:root@localhost:3306/test")
dbSession = sessionmaker(bind=engine)

# 插入数据
session = dbSession()

lilizong = math(id='0001', name='lilizong')
zhaosi = math(id='0002', name='zhaosi')
xieguangkun = math(id='0003', name='xieguangkun')

# session.add(lilizong)
# session.add(zhaosi)
# session.add(xieguangkun)
# session.commit()
session.close() # 关闭session

# 查询数据
session = dbSession()
r = session.query(math.id,math.name).all()
print(r)
print(type(r))
for i in r:
    print(i)
session.close() # 关闭session