class Expense:
    def __init__(self, amount):
        self.amount = amount

def handle_expense(expense):
    if expense.amount <= 100:
        print("small manager handles expenses up to 100")
    elif expense.amount <= 500:
        print("medium manager handles expenses up to 500")
    elif expense.amount <= 1000:
        print("large manager handles expenses up to 1000")
    else:
        print("director handles expenses over 1000")

expense1 = Expense(50)
expense2 = Expense(200)
expense3 = Expense(600)
expense4 = Expense(1500)

handle_expense(expense1)
handle_expense(expense2)
handle_expense(expense3)
handle_expense(expense4)
