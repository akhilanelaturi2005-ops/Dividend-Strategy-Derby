
from stock import Stock
from portfolio import Portfolio
from risk_analysis import calculate_risk
from game_engine import calculate_score

s1 = Stock("DividendCorp", 100, 5, 0.2)
s2 = Stock("IncomeLtd", 150, 6, 0.15)

portfolio = Portfolio()
portfolio.add_stock(s1, 10)
portfolio.add_stock(s2, 5)

income = portfolio.annual_income()
risk = calculate_risk(portfolio)
score = calculate_score(income, risk)

print("Annual Dividend Income:", income)
print("Risk Score:", risk)
print("Game Score:", score)
