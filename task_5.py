# 5. Реализуйте алгоритм нахождения (генерации) рандомного (случайного)
# числа. (Не используя библиотеки связанные с рандомом)

import time

a = 1
b = 1000
random = int((time.time() % 1) * (a + b)*a)
print(random)