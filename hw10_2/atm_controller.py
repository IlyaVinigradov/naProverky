"""
Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация
данных), которые вы уже решали. Превратите функции в методы класса, а
параметры в свойства. Задачи должны решаться через вызов методов
экземпляра. 
"""
import atm_model
import atm_view


class Main:
    atm = atm_model.Atm()

    while True:
        res = atm_view.View.view()

        if res[0] == 1:
            atm_model.Atm.add_money(atm, res[1])
        if res[0] == 2:
            atm_model.Atm.get_money(atm, res[1])
        if res[0] == 3:
            atm.print_bank()
            break
