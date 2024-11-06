import pandas as pd

# class PET_Error(BaseException):
#   def __init__(self, message = 'Must be a number'):
#     self.message = message
#     super().__init__(self)

expense_list = {
    'Expense' : [],
    'Price' : [],
    'Amount' : [],
    'Total Price' : [],
    'Category' : [],
    'Description' : [],
    'total_expense' : []

}
class ExpenseTracker:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{self.name} expenses: '

    def add_expense(self, expense, price, amount, category, description):
        expense_list['Expense'].append(expense)
        expense_list['Price'].append(price)
        expense_list['Amount'].append(amount)
        expense_list['Category'].append(category)
        expense_list['Description'].append(description)

    def delete_expense(self, expense):
      if expense in expense_list['Expense']:
          expense_index = expense_list['Expense'].index(expense)
      del expense_list['Expense'][expense_index]
      del expense_list['Price'][expense_index]
      del expense_list['Amount'][expense_index]
      del expense_list['Category'][expense_index]
      del expense_list['Description'][expense_index]
      return expense_list

    # # def delete_expense(self, expense):
    # #   if expense in self.expense_data['Expense'].values:
    # #     # Drop rows where 'price' has a specific non-NaN value, for example, 0
    # #     self.expense_data.drop(self.expense_data[self.expense_data["Expense"] == expense].index, inplace=True)
    # #     # Reset the index if needed
    # #     self.expense_data.reset_index(drop=True, inplace=True)
    # #       # expense_index = expense_list['Expense'].index(expense)
    # #   # del expense_list['Expense'][expense_index]
    # #   # del expense_list['Amount'][expense_index]
    # #   # del expense_list['Category'][expense_index]
    # #   # del expense_list['Description'][expense_index]

    # def delete_expense(self, expense):
    #   if expense in self.expense_data['Expense'].values:
    #     self.expense_data.drop(self.expense_data[self.expense_data['Expense'] == expense].index, inplace=True)
    #     self.expense_data.reset_index(drop=True, inplace=True)
    #     self.total_expense_cost = self.expense_data['Amount'].sum()
    #   return self.expense_list

    def view_expense(self):
      # calculate the cost of the total expenses first
        total_expense_cost = 0.0
        for i in expense_list['Price']:
            total_expense_cost += i
            expense_list['total_expense'].append(total_expense_cost)
        expense_data = pd.DataFrame(expense_list)
        expense_data.index = expense_data.index + 1
        expense_data.to_csv(f'{self.name}_Expense_List.csv', index = True)
        # expense_data_total = pd.concat
        return expense_data



def main():
  print('Welcome to your Personal Expense Tracker')
  User_name = input('Please enter your name of choice: ').title()
  Username = ExpenseTracker(f'{User_name}\'s')
  print(Username)

  while True:
    print('\n1. Add Expense')
    print('2. Delete Expense')
    print('3. View Expenses')
    print('4. Exit')

    choice = input('Select an operation (1 / 2 / 3 / 4): ')

    if choice == '1':
      expense = input('Enter an expense to add: ')
      
      while True:
      
        try:
          price = int(input('Enter the price of the expense: '))
          break
        except ValueError:
          print('Price must be an integer')
          continue
      
      while True:
          
        try:
          amount = int(input('Enter the amount of the expense: '))
          break
        except ValueError:
          print('Amount must be an integer')
          continue
        
      
      # # # if amount > 1:
      # # #   expense_list['Total Price'] = (price * amount)
      for i, price_value in enumerate(expense_list['Price']):
        price_index = expense_list['Price'].index(price_value)
        amount_value = expense_list['Amount'][price_index] 
        expense_list['Total Price'][price_index] = (price_value * amount_value)
      
      # for price_value, amount_value in zip(expense_list['Price'], expense_list['Amount']):
      #   expense_list['Total Price'] = expense_list['Price'] * expense_list['Amount']
      
      # for price_value, amount_value in zip(expense_list['Price'], expense_list['Amount']):
      #   total_price = price_value * amount_value
      #   expense_list['Total Price'].append(total_price)  # Or update the list as needed
            
      category = input('Is your expense a need or want: ')
      if category != 'want' and category != 'need':
        print('Your expense can only be a need or a want')
        answer = input('Do you want to make a custom category (YES/NO)? ').title()
        if answer == 'Yes':
          category = input('Enter custom category name: ')
        else:
          continue
        
      description = input('Describe your expense: ')
      
      Username.add_expense(expense, price, amount, category, description)

    elif choice == '2':
      expense = input('Enter an expense to delete: ')
      Username.delete_expense(expense)

    elif choice == '3':
      print(f'{User_name} EXPENSES LIST')
      print(Username.view_expense())

    elif choice == '4':
      print('EXITING TRACKER...')
      break

    else:
      print('Invalid operation')
if __name__ == '__main__':
  main()
