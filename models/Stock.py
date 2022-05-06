class Stock:

    def __init__(self, name, amount, percentage_profit):
        self.name = name
        self.amount = amount
        self.percent_profit = percentage_profit

    def __str__(self):
        return f"{self.name}, montant : {self.amount}€, pourcentage bénéfice : {self.percent_profit}%"
