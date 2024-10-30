import pandas as pd

expense_list = {
    'Expense' : [],
    'Amount' : [],
    'Category' : [],
    'Description' : [],
    'total_expense' : []
}
class ExpenseTracker:
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return f'This is a list of {self.name} expenses: '

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
            expense_list['total_expense'].append(total_expense_cost)
        expense_data = pd.DataFrame(expense_list)
        expense_data.index = expense_data.index + 1
        expense_data.to_csv(f'{self.name}_Expense_List.csv', index = True)
        # expense_data_total = pd.concat
        return expense_data
    
    def delete_expense(self, expense):
        if expense in expense_list['Expense']:
            expense_index = expense_list['Expense'].index(expense)

        del expense_list['Expense'][expense_index]
        del expense_list['Amount'][expense_index]
        del expense_list['Category'][expense_index]
        del expense_list['Description'][expense_index] 
        return expense_list      
        
        

Ugo = ExpenseTracker('Ugo')
Ugo.add_expense('water', '10', 'need', 'food')
Ugo.add_expense('prada sandals', '300', 'want', 'clothing')
Ugo.add_expense('donut', '54', 'need', 'food')
Ugo.delete_expense('prada sandals')
print(Ugo)
print(Ugo.view_expense())