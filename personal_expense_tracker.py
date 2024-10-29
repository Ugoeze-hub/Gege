expense_list = {
    'Expense' : [],
    'Amount' : [],
    'Category' : [],
    'Description' : []
}
class ExpenseTracker:
    def __init__(self, name):
        self.name = name


    def add_expense(self, expense):
        expense_list['Expense'] += expense 
        