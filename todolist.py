#list to store the to-do items

to_do_list = []

#function to display list
def display_list():
    for i, item in enumerate(to_do_list, 1):
        print(f'{i}. {item}')

#main function to handle user operations
def main():
    print('To-Do List App')
    while True:
        print('\n1. Add task')
        print('2. Complete Task')
        print('3. View Task')
        print('4. Exit')

        choice = input('Select an operation (1/2/3/4)')

        if choice == '1':
            task = input('Enter the task: ')
            to_do_list.append(task)
        elif choice == '2':
            display_list()
            index = int(input('Enter the task number to complete: '))
            if index < len(to_do_list):
                to_do_list.pop(index - 1)
            else:
                print('Invalid task number')
        elif choice == '3':
            display_list()
        elif choice == '4':
            break
        else:
            print('Invalid choice')

#execute the main function
if __name__ == '__main__':
    main()