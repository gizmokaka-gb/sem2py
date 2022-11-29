# 4. Задайте список из N элементов, заполненных числами
# из промежутка [-N, N]. Найдите произведение элементов
# на указанных позициях. Позиции хранятся в файле file.txt
# в одной строке одно число.

n = int(input('Введите размер последовательности N: '))
n_list = []
for i in range(-n, n + 1):
    n_list.append(i)
print(n_list)
with open('file.txt', 'r') as data:
    a = 1
    for i in data:
        a = a * n_list[int(i)]
    print(a)


