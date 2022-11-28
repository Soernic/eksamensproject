from round_grade import roundGrade
from compute_final_grade import computeFinalGrades
from grades_plot import gradesPlot
from menu_handler import menuHandler
from data_load import dataLoad
from check_error import checkError
from display_list_of_grades import displayListOfGrades

import numpy as np

def main():
    '''
    The main loop runs the main menu and calls the appropriate function
    The main script calls the menuHandler function to display the main menu
    This main menu runs in a loop until the user quits
    '''
    while True:
        menuItems = np.array(['Load data from file', 'Check for errors', 'Plot grades', 'Display list of grades', 'Exit'])
        mainMenuOption = menuHandler(menuItems)
        if mainMenuOption == 1:
            dataCSV, assignments, students = dataLoad()

            print(f'\n{dataCSV}\n')
            print(f'Number of assignments: {assignments}')
            print(f'Number of students: {students}\n')

            data = np.array(dataCSV)

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