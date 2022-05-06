from itertools import combinations


def get_combinations_stocks(list_stocks: list) -> list:
    """
    get all the combinations to get the best results of benefits

    :rtype: list
    :param list_stocks:
    :return: list_combinations_stocks
    """

    list_combinations_stocks = []

    for n in range(len(list_stocks)):
        list_combinations_stocks.extend([list(item) for item in combinations(list_stocks, n) if item])

    return list_combinations_stocks
