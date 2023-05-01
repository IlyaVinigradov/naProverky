import model


def user_input():
    a = input(
        'введите действие:\n1 -- пополнить\n2 -- снять\n3 -- показать баланс\nпустая строка -- выйти\n')
    while len(a) > 0:
        print('введите действие:\n1 -- пополнить\n2 -- снять\n3 -- показать баланс\nпустая строка -- выйти\n')
        match a:
            case '1':
                cash = input('введите сумму кратную 50: ')
                model.add_money(cash)
                print(bank)
                return bank
            case '2':
                cash = input('введите сумму кратную 50: ')
                model.out_money(cash)
                print(bank)
                return bank
