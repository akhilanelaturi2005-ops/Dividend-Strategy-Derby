
class Stock:
    def __init__(self, name, price, dividend, volatility):
        self.name = name
        self.price = price
        self.dividend = dividend
        self.volatility = volatility

    def dividend_yield(self):
        return self.dividend / self.price
