import numpy as np

#Задание 1
hours = np.arange(0, 22, 3)
p_count = int(1/(1/5)) + 1
line = np.linspace(0, 1, p_count)
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2, 3), -1)
identity = np.eye(3, dtype=int)
print(hours.shape, hours.ndim, hours.size, hours.dtype)

#Задание 2
print("\n")

print(hours[2])
print(hours[-1])
print(hours[2: 5+1])
print(hours[1::2])
print(hours[::-1])

#Задание 3
print("\n")

temperatures = np.array([
	[12, 14, 13, 15],
	[11, 13, 16, 17],
	[10, 12, 15, 18]
])
print(temperatures.shape, temperatures.ndim, temperatures.size)
print(temperatures[1, 2])
print(temperatures[0])
print(temperatures[:, -1])
print(temperatures[:2, 1:])
print(temperatures[:2, 1:3])

#Задание 4
print("\n")

matrix = np.arange(1, 26).reshape(5, 5)
f_1 = matrix[:3]
print(f_1)
print(f_1.shape)

f_2 = matrix[-2:]
print(f_2)
print(f_2.shape)

f_3 = matrix[:, :2]
print(f_2)
print(f_2.shape)

f_4 = matrix[:3, 1:4]
print(f_3)
print(f_3.shape)

f_5 = matrix[-2:, -2:]
print(f_5)
print(f_5.shape)

#Задание 5
vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9

changed_hours = hours.copy()
changed_hours[1:3] = 99
changed_hours[1::2] = -1
print(changed_hours)
# .copy() создает новый массив идентичный данному, так мы изменяем копию, не трогая оригинальные данные

changed_matrix = matrix.copy()
changed_matrix[0, :] = 0
changed_matrix[:, -1] = -1
changed_matrix[1:-1, 1:-1] = 100
print(matrix)
print(changed_matrix)

#Задание 6
numbers = np.arange(12)
table = numbers.reshape(3, 4)
transposed = table.T

print(numbers.shape, table.shape, transposed.shape)
#reshape меняет форму массива, сохраняя количество элементов 12 элементов не хватит чтобы заполнить массив 5 на 3