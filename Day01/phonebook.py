def print_menu():
    print('1. Print Phone Numbers')
    print('2. Add a Phone Number')
    print('3. Remove a Phone Number')
    print('4. Lookup a Phone Number')
    print('5. Quit')
numbers = {}
menu_choices = 0
print_menu()

while menu_choices !=5 :
    menu_choices = int(input("Type in a number (1-5) -> "))
    if(menu_choices == 1):
        print("Telephone Numbers -> ")
        for key, value in numbers.items():
            print(f" {key} --> {value}")
            print()
    elif(menu_choices == 2):
        number = input("Enter Number -> ")
        name = input("Enter the Name -> ")
        numbers[name] = number
        print("saved Succesfully...")
    elif(menu_choices == 3):
        name = input("Enter the name that you want to delete --> ")
        if(name in numbers):
            del numbers[name]
            print("deleted Succesfully...")
    elif(menu_choices == 4 ):
        name = input("Search here -> ")
        if(name in numbers):
            print(f'{name} -> {numbers[name]}')
           
    elif(menu_choices != 5):
        print_menu()
            