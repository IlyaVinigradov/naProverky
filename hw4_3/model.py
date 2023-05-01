import hw4_3


def add_money(cash):
    global bank
    bank += cash
    return bank


def out_money(cash):
    global bank
