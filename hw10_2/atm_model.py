class Atm:

    def __init__(self) -> None:
        self._start = 0


    def print_bank(self):
        print(self._start)

    def add_money(self, sum):
        self._start += sum
        self.print_bank()

    def get_money(self, sum):
        self._start -= sum
        self.print_bank()

    # def percent(self, sum):
