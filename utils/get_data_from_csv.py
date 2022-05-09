import csv

from models.Stock import Stock


def get_data_from_csv(file) -> list:
    """
    Function read csv file and get data to create object

    :param file:
    :return: list_stocks
    """

    # with open(file, newline='\n'):

    list_stocks = []

    reader = csv.reader(file, delimiter=',')

    for row in reader:
        list_stocks.append(Stock(row[0], int(row[1]), int(row[2])))

    return list_stocks
