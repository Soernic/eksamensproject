import numpy as np

def inputNumber(promt):
        while True:
            try:
                num = int(input(promt))
                break
            except ValueError:
                print("Not an integer. Try again.")
                pass
        return num

def menuHandler(menuItems):
    for i in range(len(menuItems)):
        print(f'{i+1}. {menuItems[i]}')

    choice = 0
    while True:
        choice = inputNumber("Please choose a menu item: ")

        if choice in range(1, len(menuItems)+1):
            break
        else:
            print(f"Not a valid menu choice. Please choose a number between 1 and {len(menuItems)}")
            
    return choice