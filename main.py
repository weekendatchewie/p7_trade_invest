from utils.get_combinations_stocks import get_combinations_stocks
from utils.get_data_from_csv import get_data_from_csv
from utils.get_stocks_cost import get_stocks_cost

fichier = open("./csv/action-test5.csv")


def run():
    stocks = get_data_from_csv(fichier)
    combinations_actions = get_combinations_stocks(stocks)

    for combination in combinations_actions:
        get_stocks_cost(combination)


if __name__ == "__main__":
    run()
