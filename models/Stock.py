class Stock:

    def __init__(self, name, amount, percentage_profit):
        self.name = name
        self.amount = amount
        self.percentage_profit = percentage_profit

    def __str__(self):
        return f"{self.name}, montant : {self.amount}€, pourcentage bénéfice : {self.percentage_profit}%"

    def __repr__(self):
        return f"{self.name}, montant : {self.amount}€, bénéfice : {self.profit}€"

    @property
    def profit(self):
        profit = round(self.amount * (self.percentage_profit / 100), 2)

        return profit
