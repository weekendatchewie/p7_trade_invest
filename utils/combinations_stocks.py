from itertools import combinations

from utils.data_usefull import MAX_EXPENSE


def get_combinations_stocks(list_stocks: list) -> list:
    """
    Get all the combinations to get the best results of benefits

    :rtype: list
    :param list_stocks:
    :return: list_combinations_stocks
    """

    list_combinations_stocks = []

    for n in range(len(list_stocks)):
        # list_combinations_stocks.extend([list(item) for item in combinations(list_stocks, n) if item])
        for item in combinations(list_stocks, n):
            if item:
                list_combinations_stocks.append(list(item))

    return list_combinations_stocks


def get_total_cost_combinations_stocks(list_stocks: list) -> float:
    """
    Calculate the total price of stocks in combinations list

    :param list_stocks:
    :return: total_cost
    """

    total_cost = 0

    for stock in list_stocks:
        total_cost += stock.amount

    return total_cost


def get_total_profit_combinations_stocks(list_stocks) -> float:
    """
    Calculate the total profit in a combination of stocks

    :param list_stocks:
    :return: total_profit
    """

    total_profit = 0

    for stock in list_stocks:
        total_profit += stock.profit

    return round(total_profit, 2)


def get_best_combination_stocks(list_stocks: list) -> dict:
    """
    Compare the combinations stocks, keep those are lower than the max expense : 500€
    Sort by total profit
    Keep the combination with the best profit

    :param list_stocks:
    :return: best_combination
    """

    list_combinations_under_max_expense = []

    for combination in list_stocks:
        cost_to_compare = combination["Total coût d'achat des actions"]
        if cost_to_compare <= MAX_EXPENSE:
            list_combinations_under_max_expense.append(combination)

    sorted_combinations = sorted(list_combinations_under_max_expense, key=lambda item: item["Total bénéfice"],
                                 reverse=True)

    best_combination = sorted_combinations[0]

    return best_combination
