from utils.data_usefull import MAX_EXPENSE
from utils.get_data_from_csv import get_data_from_csv


csv_file = open("./csv/action-test5.csv")


def algo_dynamic(file=csv_file) -> dict:
    """
    On créé une matrice, une sorte de tableau comportant autant de ligne que d'élément et de colonne que de capacité.
    Chaque élément sera comparé afin de trouver le résultat le plus optimal

    :param file:
    """

    stocks = get_data_from_csv(file)

    matrix = [[0 for x in range(MAX_EXPENSE + 1)] for x in range(len(stocks) + 1)]

    for i in range(1, len(stocks) + 1):
        # Pour chaque élément on parcourt la capacité: ligne de la matrice
        for w in range(1, MAX_EXPENSE + 1):

            # On vérifie si le montant de l'élément de la ligne précédente est inférieur ou égal que la capacité
            # dans la matrice, on vérifie si le bénéfice est supérieur à celui de la ligne précédente
            if stocks[i-1].amount <= w:
                matrix[i][w] = max(stocks[i-1].profit + matrix[i-1][w-stocks[i-1].amount], matrix[i-1][w])
            else:
                # On garde l'élément optimiser de la ligne d'avant
                matrix[i][w] = matrix[i-1][w]

    # Retrouver les éléments en fonction de la somme
    max_expense = MAX_EXPENSE
    n = len(stocks)
    elements_selection = []

    while max_expense >= 0 and n >= 0:
        e = stocks[n-1]

        if matrix[n][max_expense] == matrix[n-1][max_expense-e.amount] + e.profit:
            elements_selection.append(e)
            max_expense -= e.amount

        n -= 1

    return {"Total bénéfice": matrix[-1][-1], "Combinaisons d'actions": elements_selection}
