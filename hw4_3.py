"""
Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег
"""

bank = 0
count = 0


def add_money(a):
    global bank
    if a % 50 == 0 and a >= 0:
        bank += a
    else:
        print("error")
    return round(bank, 2)


def count_it():
    global count
    count += 1
    global bank
    if count % 3 == 0:
        bank *= 0.97
        print('+ налог за работу')


def wealth_tax():
    global bank
    if bank >= 5_000_000:
        print('+ налог на богатство')
        return round(bank * 0.9, 2)
    else:
        return round(bank, 2)


def out_money(a):
    global bank
    if a % 50 == 0 and bank >= a and a >= 0:

        percent = a * 0.015
        if 30 >= percent:
            bank -= 30
        elif percent >= 600:
            bank -= 600
        else:
            bank -= percent

        bank -= a
    else:
        print('error')


while True:
    a = ''
    a = input(
        'введите действие:\n1 -- пополнить\n2 -- снять\n3 -- выйти\n')
    match a:
        case '1':
            cash = int(input('введите сумму кратную 50: '))
            print(bank)
            add_money(cash)
            count_it()
            wealth_tax()
            print(bank)
        case '2':
            cash = int(input('введите сумму кратную 50: '))
            out_money(cash)
            count_it()
            wealth_tax()
            print(bank)
        case '3':
            break
