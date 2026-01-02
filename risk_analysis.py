
def calculate_risk(portfolio):
    if not portfolio.holdings:
        return 0
    return sum(stock.volatility for stock, _ in portfolio.holdings) / len(portfolio.holdings)
