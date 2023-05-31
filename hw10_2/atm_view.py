import atm_model


class View:

    def view() -> tuple:
        user_in = input(
            'введите команду:\n1 - пополнить\n2 - снять\n3 - выйти\n')
        match user_in:
            case '1':
                sum = (1, int(input('введите сумму пополнения: ')))
                return sum
            case '2':
                sum = (2, int(input('введите сумму выдачи: ')))
                return sum
            case '3':
                return 3
