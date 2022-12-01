import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''
This project is made by:
August Borg Ljørring    (s224178)
Søren Skov Jensen       (s224169)
Malte Lau               (s224183)
'''

def inputNumber(promt: str):
    '''
    Params: promt (str): Promt to be displayed to the user
    Returns: number
    
    Author: August Borg Ljørring (s224178)
    '''
    
    while True:
        try:
            num = int(input(promt))
            break
        except ValueError:
            print("Not an integer. Try again.")
    return num


def menuHandler(menu_items: list):
    '''
    Params: menuItems
    Returns: None
    
    Author: August Borg Ljørring (s224178)
    '''

    for i, menuitem in enumerate(menu_items, start=1):
        print(f'{i}. {menuitem}')

    choice = 0
    while True:
        choice = inputNumber("Please choose a menu item: ")

        # Break if choice is valid
        if choice > 0 and choice <= len(menu_items):
            break
        
        print(f"Not a valid menu choice. Please choose a number between 1 and {len(menu_items)}")
            
    return choice


def dataLoad():
    '''
    Params: None
    Returns: Data as a numpy array
    
    Author: August Borg Ljørring (s224178)
    '''
    
    # Load data from file grades.csv
    while True:
        filename = input("Please enter the name of the file to load: ")
        try:
            df = pd.read_csv(filename, sep=',')
            break
        except FileNotFoundError:
            print('File not found. Try again.')

    print(f'\n{df}\n')
    print(f'Number of assignments: {len(df.columns) - 2}')
    print(f'Number of students: {len(df.index)}\n')

    return np.array(df)


def checkError(data: np.array, printErrors: bool):
    '''
    Params: data
    Returns: None
    
    Author: Malte Lau (s224183)
    '''
    
    has_error = False
    students = data[:, 0]
    
    if students.size != np.unique(students).size:
        has_error = True
        if not printErrors:
            return True
        for i, student in enumerate(students, start=2):
            if np.count_nonzero(student == students) > 1:
                print(f'Error: There are multiple occurences of student {student}. This error occurs at line {i}')
    
    for students_num in range(data.shape[0]):
        for assignment_num in range(data.shape[1] - 2):
            if data[students_num,assignment_num+2] not in np.array([-3, 0, 2, 4, 7, 10, 12]):
                has_error = True
                if not printErrors:
                    return True
                else:
                    print(f"Error: Student {data[students_num,0]} ({data[students_num,1]}) has recieved an invalid grade in assignment {assignment_num + 1}")   
    
    if not printErrors:
        return False
    
    if has_error:
        print("\nErrors found in data, please se above for more information\n")
        return
    
    else:
        print("\nNo errors found in data \n")
        return


def displayListOfGrades(data: np.array):
    '''
    Displays a list of grades as a dataframe along with a rounded final grade for each student.
    
    Params: data
    Returns: None
    
    Author: Søren Skov Jensen (s224169)
    '''
    
    df_columns = np.hstack((
        'Student ID', 'Student Name', 
        np.array([f"A{count}" for count, _ in enumerate(data[0, 2:], start=1)])))
    
    df = pd.DataFrame(data=data, columns=df_columns)
    final_grades = pd.DataFrame({'Final Grade': computeFinalGrades(data[:, 2:])})
    df = df.join(final_grades)
    
    print("\nList of grades (alphabetical order):")
    with pd.option_context('display.max_rows', None):  # more options can be specified also
        print(df.sort_values(by=['Student Name']))
    print("")

    if checkError(data, False):
        print("The list of grades might not be accurate! Because of errors in your data, you can run 'check for errors' to get more information\n")
        
    return


def computeFinalGrades(data):
    '''
    Params: data
    Returns: data as a numpy array
    
    Author: Malte Lau (s224183)
    '''
    
    grades = data[:, 2:]
    gradesFinal = np.zeros(len(data))
    
    # checks each students grades and assigns a final grade
    for i, grade in enumerate(grades):
        if -3 in grade:
            gradesFinal[i] = -3
        elif len(grade) == 1:
            gradesFinal[i] = grade[0]
        else:
            gradesFinal[i] = np.mean(np.delete(grade, np.argmin(grade)))

    return roundGrade(gradesFinal)


def roundGrade(grades: np.array):
    """
    Params: Grades (np.array): Array of grades to be rounded
    Returns: Grades rounded to the nearest grade
    
    Author: Søren Skov Jensen (s224169)
    """
    
    # Function takes vector of grades and rounds them to the nearest appropriate grade to correct for potential data errors.
    possible_grades = np.array([-3, 0, 2, 4, 7, 10, 12])
    gradesRounded = np.array([])
    
    gradesRounded = np.array([min(possible_grades, key=lambda x: abs(x - grade)) for grade in grades])

    return gradesRounded


def gradesPlot(grades):
    '''
    Params: data - a numpy array containing the grades for each student and assignment
    Returns: nothing
    
    Author: August Borg Ljørring (s224178)
    '''
    
    if checkError(data, False):
        print("The plot might not be accurate! Because of errors in your data, you can run 'check for errors' to get more information\n")
    
    finalGrade = computeFinalGrades(grades)
    
    fig, axs = plt.subplots(1, 2)
    fig.set_size_inches(13, 5)

    # Plot the grades
    gradeList = np.array([-3, 0, 2, 4, 7, 10, 12])

    for grade in gradeList:
        gradeAmount = np.count_nonzero([finalGrade == grade])
        axs[0].bar(str(grade), gradeAmount, width=0.6)

    axs[0].set_xlabel('Grades')
    axs[0].set_ylabel('Amount of students')
    axs[0].set_title('Final Grades')
    axs[0].grid(axis='y')
    axs[0].yaxis.set_major_locator(plt.MaxNLocator(integer=True))

    grades_for_plot = grades.copy()
    number_of_students = data.shape[0]
    number_of_assignments = data.shape[1] - 2

    # plotting the points for each assignment so each assignment is a different color
    XM = []
    YM = []
    
    for i in range(number_of_assignments):
        x = np.ones(number_of_students) * (i+1)
        x += np.random.uniform(-0.1,0.1, number_of_students)
        
        y = grades_for_plot[:, i]
        y += np.random.uniform(-0.1,0.1, number_of_students)

        axs[1].scatter(x, y, s=30, marker='o', edgecolors='black')
        
        ym = np.mean(grades_for_plot[:, i])
        XM += [i+1]
        YM += [ym]
        
        axs[1].plot([i+0.8, i+1.2], [ym, ym], color='red', linewidth=2)
    
    # plotting the mean for each assignment
    axs[1].plot(XM, YM, color='blue', label='Average grade (as line)')
    
    axs[1].set_yticks([-3, 0, 2, 4, 7, 10, 12])
    axs[1].set_xticks(np.arange(number_of_assignments)+1)
    axs[1].set_xlabel('Assignments')
    axs[1].set_ylabel('Grades')
    axs[1].set_title('Grades per Assignment')
    axs[1].set_ylim(-4, 13)
    axs[1].grid()
    axs[1].set_axisbelow(True)
    axs[1].plot([], [], color='red', label='Average grade (per assignment)')
    axs[1].legend()
    #git
    print("Plot is shown in a new window, please close the window to continue\n")
    plt.show()
    
    return


# The main function:
if __name__ == '__main__':
    print("\nWelcome to the gradehelper program!\n")
    data = dataLoad()
    while True:
        menuItems = np.array(['Load new data.', 'Check for errors.', 'Generate plots.', 'Display list of grades.', 'Quit.'])
        mainMenuOption = menuHandler(menuItems)
        
        # 1. Load new data
        if mainMenuOption == 1:
            data = dataLoad()
            
        # 2. Check for errors
        elif mainMenuOption == 2:
            checkError(data, True)
            
        # 3. Generate plots
        elif mainMenuOption == 3:
            gradesPlot(data[:, 2:])
            
        # 4. Display list of grades
        elif mainMenuOption == 4:
            displayListOfGrades(data)
            
        # 5. Quit
        elif mainMenuOption == 5:
            break
