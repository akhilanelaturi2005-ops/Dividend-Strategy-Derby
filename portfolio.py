
class Portfolio:
    def __init__(self):
        self.holdings = []

    def add_stock(self, stock, quantity):
        self.holdings.append((stock, quantity))

    def annual_income(self):
        return sum(stock.dividend * qty for stock, qty in self.holdings)
