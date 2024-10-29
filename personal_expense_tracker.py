import pandas as pd

expense_list = {
    'Expense' : [],
    'Amount' : [],
    'Category' : [],
    'Description' : []
}
class ExpenseTracker:
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return f'This is a list of {self.name} expenses'

    def add_expense(self, expense, amount, category, description):
        expense_list['Expense'].append(expense)
        expense_list['Amount'].append(amount)
        expense_list['Category'].append(category)
        expense_list['Description'].append(description)
        
    def view_expense(self):
        # calculate the cost of the total expenses first
        total_expense_cost = 0
        for i in expense_list['Amount']:
            i = int(i)
            total_expense_cost += i
            expense_list['total_expense'] = total_expense_cost
        expense_data = pd.DataFrame(expense_list)
        # expense_data_total = pd.concat
        return expense_data

Ugo = ExpenseTracker('Ugo')
Ugo.add_expense('water', '10', 'need', 'food')
Ugo.add_expense('prada sandals', '300', 'want', 'clothing')
print(Ugo.view_expense())