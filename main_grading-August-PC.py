from grades_plot import gradesPlot
from menu_handler import menuHandler
from data_load import dataLoad
from check_error import checkError
from display_list_of_grades import displayListOfGrades

import numpy as np

'''
The main function is the entry point of the program. It is called when the program is executed.

The main function should contain the following:
- A while loop that runs until the user chooses to exit the program.
- A call to the menuHandler function to display the main menu and get the user's choice.
- A call to the dataLoad function if the user chooses to load data from file.
- A call to the checkError function if the user chooses to check for errors.
- A call to the gradesPlot function if the user chooses to plot grades.
- A call to the displayListOfGrades function if the user chooses to display a list of grades.
- A break statement if the user chooses to exit the program.
'''

def main():
    while True:
        menuItems = np.array(['Load data from file', 'Check for errors', 'Plot grades', 'Display list of grades', 'Exit'])
        mainMenuOption = menuHandler(menuItems)
        if mainMenuOption == 1:
            data = dataLoad()
        elif mainMenuOption == 2:
            checkError(data)
        elif mainMenuOption == 3:
            gradesPlot(data)
        elif mainMenuOption == 4:
            displayListOfGrades(data)
        elif mainMenuOption == 5:
            break

if __name__ == '__main__':
    main()