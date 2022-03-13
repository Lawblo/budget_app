class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def __str__(self):
        return 'test'

    def deposit(self, amount: int, desc: str = ''):
        self.ledger.append({'amount': amount, 'description': desc})

    def withdraw(self, amount: int, desc: str = ''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -(amount), 'description': desc})
            return True
        return False

    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item['amount']
        return total

    def transfer(self, amount: int, budget_category):
        if self.withdraw(amount, f'Transfer to {budget_category.category}'):
            budget_category.deposit(amount, f'Transfer from {self.category}')
            return True
        return False

    def check_funds(self, amount: int):
        if self.get_balance() < amount:
            return False
        return True
