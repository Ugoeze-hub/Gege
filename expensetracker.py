#expense tracker
#list to store expenses
expenses = []

#function to add expenses
def add_expenses():
    amount = float(input('Enter the amount: '))
    description = input('Enter a description: ')
    expenses.append({'amount': amount, 'description': description})

#function view all expenses
def view_expenses():
    if len(expenses) == 0:
        print('No expenses recorded')
        return
    total = 0
    for i, expense in enumerate(expenses, 1):
        print(f'{i}. {expense['description']}: ${expense['amount']}')
        total += expense['amount']

    print(f'Total Expenses: ${total}')

#main function
def main():
    print('Expense Tracker App')
    while True:
        print('\n1. Add Expenses')
        print('2. View Expenses')
        print('3. Exit')

        choice = input('Select an operation (1/2/3)')

        if choice == '1':
            add_expenses()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            print('Exiting the application')
            break
        else:
            print('Invalid operation')

if __name__ == '__main__':
    main()
    