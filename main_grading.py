import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''
This project is made by:
August Borg Ljørring    (s224178)
Søren Skov Jensen       (s224169)
Malte Lau               (s224183)
'''

def inputNumber(promt):
    '''
    
    Params: promt
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

def menuHandler(menuItems):
    '''
    
    Params: menuItems
    Returns: None
    
    Author: August Borg Ljørring (s224178)
    '''
    for i, menuitem in enumerate(menuItems, start=1):
        print(f'{i}. {menuitem}')

    choice = 0
    while True:
        choice = inputNumber("Please choose a menu item: ")

        # Break if choice is valid
        if choice > 0 and choice <= len(menuItems):
            break
        
        print(f"Not a valid menu choice. Please choose a number between 1 and {len(menuItems)}")

        # if choice not in range(1, len(menuItems)+1):
        #     print(f"Not a valid menu choice. Please choose a number between 1 and {len(menuItems)}")
        # else:
        #     break
            
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
            dataCSV = pd.read_csv(filename, sep=',')
            break
        except FileNotFoundError:
            print('File not found. Try again.')

    print(f'\n{dataCSV}\n')
    print(f'Number of assignments: {len(dataCSV.columns) - 2}')
    print(f'Number of students: {len(dataCSV.index)}\n')

    return np.array(dataCSV)


def checkError(data):
    '''
    
    Params: dataCSV
    Returns: None
    
    Author: Malte Lau (s224183)
    '''
    # DER SKAL LIGE LÆSES NOGET DATA HER :D
    datafail = []
    if data is not np.unique(data[:,0]):
        for i in range(0,len(data[:,0])):
            if data[i,0] not in datafail:
                datafail.append(data[i,0])
            else:
                print(f"Error: Student id duplicate: {data[i,0]} in line {i}")
                fail = True
    
    for i in range(2,len(data[0,:])):
        for j in range(0,len(data[:,0])):
            if data[j,i] not in np.array([-3, 0, 2, 4, 7, 10, 12]):
                print(f"Error: Student: {data[j,0]}: {data[j,1]} has recieved invalid grade in assignment {i}")
                fail = True
    if fail == True:
        true_or_false_data = print("Data is not valid and error messages have been printed")
    else:
        true_or_false_data = print("Data is valid")
    return true_or_false_data

def displayListOfGrades(data):
    '''
    
    Params: data
    Returns: None
    
    Author: Søren Skov Jensen (s224169)
    '''
    
    return None

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
    
    for grade in grades:
        gradesRounded = np.append(gradesRounded, min(possible_grades, key=lambda x: abs(x - grade)))

    # måske bedre at bruge list comprehension
    gradesRounded = np.array([min(possible_grades, key=lambda x: abs(x - grade)) for grade in grades])

    return gradesRounded

def gradesPlot(data):
    '''
    

    Params: data - a numpy array containing the grades for each student and assignment
    Returns: nothing
    
    Author: August Borg Ljørring (s224178)
    '''
    finalGrade = computeFinalGrades(data)
    
    fig, axs = plt.subplots(1, 2)
    fig.set_size_inches(13, 5)

    # Plot the grades
    gradeList = np.array([-3, 0, 2, 4, 7, 10, 12])

    for grade in gradeList:
        gradeAmount = np.count_nonzero([finalGrade == grade])
        axs[0].bar(str(grade), gradeAmount, width=0.6)

    axs[0].set_xlabel('Grades')
    axs[0].set_ylabel('Amount of students')
    axs[0].set_title('Bar plot of grades')
    axs[0].grid(axis='y')
    axs[0].yaxis.set_major_locator(plt.MaxNLocator(integer=True))

    grades = data[:, 2:]
    students_num = data.shape[0]
    assignments_num = data.shape[1] - 2

    # plotting the points for each assignment so each assignment is a different color
    for i in range(assignments_num):
        y = grades[:, i]
        y += np.random.normal(0, 0.1, students_num)

        x = np.ones(students_num) * (i+1)
        x += np.random.normal(0, 0.1, students_num)

        axs[1].scatter(x, y, s=30, marker='o', edgecolors='black')
        #add a line for the average grade for each assignment
        axs[1].plot([i+0.8, i+1.2], [np.mean(y), np.mean(y)], color='red', linewidth=2)

    axs[1].set_yticks([-3, 0, 2, 4, 7, 10, 12])
    axs[1].set_xticks(np.arange(assignments_num)+1)
    axs[1].set_xlabel('Assignments')
    axs[1].set_ylabel('Grades')
    axs[1].set_title('Grades for each assignment')
    axs[1].grid()
    axs[1].set_axisbelow(True)
    
    plt.show()

# The main function:
if __name__ == '__main__':
    data = dataLoad()
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