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


    def add_expense(self, expense, amount, category, description):
        expense_list['Expense'].append(expense)
        expense_list['Amount'].append(amount)
        expense_list['Category'].append(category)
        expense_list['Description'].append(description)


print(expense_list) 
df = pd.DataFrame(expense_list)
print(df)