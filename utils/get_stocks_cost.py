def get_stocks_cost(list_stocks: list) -> float:

    total_cost = 0

    for stock in list_stocks:
        total_cost += stock.amount

    print(total_cost)

    return total_cost
