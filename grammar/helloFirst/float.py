# 浮点数进行计算时，可能会出现小数位不确定的情况
print(1.1 + 2.2)
print(1.1 + 2.1)

# 解决方案：导入decimal模块
from decimal import Decimal
print(Decimal('1.1') + Decimal('2.2'))  # 3.3
