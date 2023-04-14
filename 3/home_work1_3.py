""" 
Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. 
Программа должна подсказывать «больше» или «меньше» после каждой попытки. 
Для генерации случайного числа используйте код: from random import randint num = randint(LOWER_LIMIT, UPPER_LIMIT)
"""

from random import randint
num = randint(0, 1001)
print(num)

def game(a, win_num):
    if a == win_num:
        print('you win')
    elif a < win_num:
        print('число больше')
    else:
        print('число меньше')

count = 0
while count != 10:
    a = int(input())
    game(a, num)
    if a == num:
        break
    count = count + 1
