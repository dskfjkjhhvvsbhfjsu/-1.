import random
from operator import  itemgetter

# Створюємо масив з випадковими числами від 0 до 9 розмірністю N
print("Введіть розмірність")
N = int(input())
print(N)

matrix = []
for i in range(N):
    list_ = []
    for j in range(N):
        list_.append(random.randint(0,10))
    matrix.append(list_[:])

# Виводимо масив, що створили
print("Початковий масив")
for i in range(N):
    for j in range(N):
        print(matrix[i][j], end = ' ')
    print('')

# Шукаємо суму для кожного стовпця та записуємо в словник пари номеру стовпця і суми
dict_of_rows = {}
for i in range(N):
    rows = [row[i] for row in matrix]
    dict_of_rows[i] = sum(rows)
    print('Сума ' + str(i+1) + ' рядка: ' + str(sum(rows)))

# Сортуємо по сумі кожного стовпця
sorted_dict = dict(sorted(dict_of_rows.items(), key=itemgetter(1)))

# Створюємо матрицю заповнену нулями (потім заповнимо її посортованими стовпцями)
sorted_matrix = []
for i in range(N):
    list_ = []
    for j in range(N):
        list_.append(0)
    sorted_matrix.append(list_[:])

# Заповнюємо матрицю посортованими стовпцями
counter = 0
for i in sorted_dict.keys():
    rows = [row[i] for row in matrix]

    for j in range(N):
        sorted_matrix[j][counter] = rows[j]
    counter += 1

# Виводимо посортовану матрицю
print('Посортована матриця:')
for i in range(N):
    for j in range(N):
        print(sorted_matrix[i][j], end = ' ')
    print('')