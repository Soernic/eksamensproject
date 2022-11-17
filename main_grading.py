from round_grade import roundGrade
from compute_final_grade import computeFinalGrades
from grades_plot import gradesPlot
from menu_handler import menuHandler
from data_load import dataLoad
from check_error import checkError
from display_list_of_grades import displayListOfGrades

import pandas as pd
import numpy as np

def main():
    while True:
        menuItems = ['Load data from file', 'Display list of grades', 'Compute final grades', 'Round grades', 'Plot grades', 'Exit']
        mainMenuOption = menuHandler(menuItems)
        if mainMenuOption is 1:
            dataLoad()
        elif mainMenuOption is 2:
            checkError()
        elif mainMenuOption is 3:
            gradesPlot()
        elif mainMenuOption is 4:
            displayListOfGrades()
        elif mainMenuOption is 5:
            break

if __name__ == '__main__':
    main()