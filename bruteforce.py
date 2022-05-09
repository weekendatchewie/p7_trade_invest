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


def brute_force(file):

    stocks = get_data_from_csv(file)
    combinations_actions = get_combinations_stocks(stocks)

    list_combinations_with_cost = []

    for combination in combinations_actions:
        total_stocks_cost = get_total_cost_combinations_stocks(combination)
        total_profit = get_total_profit_combinations_stocks(combination)
        list_combinations_with_cost.append({
            "combinaisons des actions": combination,
            "total coût d'achat des actions": total_stocks_cost,
            "total bénéfice": total_profit
        })

    result = get_best_combination_stocks(list_combinations_with_cost)

    return result
