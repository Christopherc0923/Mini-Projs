class BudgetTracker:
    def __init__(self):
        self.categories = {}

    def add_transaction(self, category, amount, description):
        # Update the balance for the specified category
        if category in self.categories:
            self.categories[category] += amount
        else:
            self.categories[category] = amount

    def get_all_categories(self):
        return self.categories