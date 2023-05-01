""" 
Напишите функцию для транспонирования матрицы .
"""

line1 = [1, 2, 3, 4, 5]
line2 = [6, 7, 8, 9, 0]
line3 = [11, 22, 33, 44, 55]

def transp(*matrix):
    for line in zip(*matrix):
        print(line, sep='\n')

transp(line1, line2)
print()
transp(line1, line2, line3)