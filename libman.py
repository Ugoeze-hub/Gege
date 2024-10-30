#Basic Library Management system
#Dictionary to store books and their availability status

library = {}

#function to add a new book to the library
def add_book(title):
    library[title] = 'Available'

#function to issue a book
def issue_book(title):
    if title in library:
        if library[title] == 'Available':
            library[title] = 'Issued'
            print(f'{title} has been issued.')
        else:
            print(f'{title} is already issued.')
    else:
        print(f'{title} does not exist in the library')

#function to return a book
def return_book(title):
    if title in library:
        if library[title] == 'Issued':
            library[title] = 'Available'
            print(f'{title} has been returned')
        else:
            print(f'{title} is already available')
    else:
        print(f'{title} does not exist in the library')

#function to list all book and their availability status
def list_books():
    for title, status in library.items():
        print(f'{title} - {status}')


#main function for user input
def main():
    print('Library Management System')

    while True:
        print('\n1. Add Book')
        print('2. Issue Book')
        print('3. Return Book')
        print('4. List Books')
        print('5. Exit')

        choice = input('Select an operation (1/2/3/4/5): ')

        if choice == '1':
            title = input('Enter the title of the book to add: ')
            add_book(title)
        elif choice == '2':
            title = input('Enter the title of the book to issue: ')
            issue_book(title)
        elif choice == '3':
            title = input('Enter the title of the book to return: ')
            return_book(title)  
        elif choice == '4':
            list_books()
        elif choice == '5':
            print('Exiting the application')
            break
        else:
            print('Invalid choice')

#execute the main function
if __name__ == '__main__':
    main()
    