from decimal import Decimal
from random import randint
num = 12.3456789
formatted_num = Decimal(f"{num:.5f}")
print(formatted_num)  # 12.34568
