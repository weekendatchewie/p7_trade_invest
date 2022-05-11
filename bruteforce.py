"""
Trouver le meilleur résultat : 
    - Une action est acheté une seule fois, en entière
    - le total d'achat ne dépasse pas 500

Créer toutes les combinaisons possibles en les listant
Garder les combinaisons qui ne dépassent pas le montant max d'achat : 500
Calculer le bénéfice de ces combinaisons
Trier la liste et garder le meilleur résultat des bénéfices

"""

from utils.combinations_stocks import get_combinations_stocks, get_total_cost_combinations_stocks, \
    get_total_profit_combinations_stocks, get_best_combination_stocks
from utils.get_data_from_csv import get_data_from_csv


csv_file = open("./csv/action-test5.csv")


def brute_force(file=csv_file):

    stocks = get_data_from_csv(file)
    combinations_actions = get_combinations_stocks(stocks)

    list_combinations_with_cost = []

    for combination in combinations_actions:
        total_stocks_cost = get_total_cost_combinations_stocks(combination)
        total_profit = get_total_profit_combinations_stocks(combination)
        list_combinations_with_cost.append({
            "Combinaisons des actions": combination,
            "Total coût d'achat des actions": total_stocks_cost,
            "Total bénéfice": total_profit
        })

    result = get_best_combination_stocks(list_combinations_with_cost)

    return result
