# 12.5. Дан двумерный массив. Вывести на экран:
# # б) все элементы s-го столбца массива.
# import random
# def output_matrix(matrix_in):
#     for index in range(len(matrix_in)):
#         print(matrix_in[index])
# lenx = int(input('string'))
# leny = int(input('colums'))
# matrix = [[]] * lenx
# for i in range(lenx):
#     matrix[i] = [0] * leny
# for i in range(lenx):
#     print(matrix[i])
# print()
# print()
# print()
#
# for i in range(lenx):
#     for j in range(leny):
#         matrix[i][j] = random.randint(1,9)
# for i in range(lenx):
#     print(matrix[i])
# result = matrix[3][2]
# print(result)
# import random
# def print(* mass):
#     for i in mass:
#         for q in range(len(i)):
#             if q == 1:
#                 print(i[q], end = ' ')
#                 print()
# mass = [[1,2,3,4,5],
#         [6,7,8,9,10],
#         [11,12,13,14,15]]
#
# print(*mass[0])
# for i in mass:
#     for q in range(len(i)):
#         if q == 1:
#             print(i[q], end = ' ')
# print()

#
# #12.6. Дан двумерный массив. Вывести на экран:
# # б) все элементы m-й строки массива.
import random
# a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         print(a[i][j], end=' ')
#     print()

# 12.32. Дан двумерный массив. Вывести на экран:
# а) все элементы третьей строки массива, начиная с последнего элемента этой
# строки;

# import random
# def output_matrix(matrix_in):
#     for index in range(len(matrix_in)):
#         print(matrix_in[index])
# lenx = int(input('string'))
# leny = int(input('colums'))
# matrix = [[]] * lenx
# for i in range(lenx):
#     matrix[i] = [0] * leny
# for i in range(lenx):
#     print(matrix[i])
# print()
# print()
# print()
#
# for i in range(lenx):
#     for j in range(leny):
#         matrix[i][j] = random.randint(1,10)
# for i in range(lenx):
#     print(matrix[i])

# 12.16. Составить программу:
# а) расчета разности двух любых элементов двумерного массива;

# # 12.33. Дан двумерный массив. Вывести на экран:
# # а) все элементы пятого столбца массива, начиная с последнего элемента этого столбца;

#
# # Задача 12.62 (a)

# 12.62. Дан двумерный массив. Найти:
# а) сумму элементов каждой строки;
import random
# a = [[1,2,3,4,5],
#      [6,7,8,9,10]]
# sum = 0
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         sum += a[i][j]
#         print(sum)