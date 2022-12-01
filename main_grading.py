import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""
This project is made by:
August Borg Ljørring    (s224178)
Søren Skov Jensen       (s224169)
Malte Lau               (s224183)

In the project it was unclear whether we should use the data if it contained errors, 
so we decided to use the data, but print out a warning if there were errors. 
And asking the user to use 'check for errors' to see the errors.

We have also chosen to use snake case as variable naming convention, instead of opting
for camel case like the functions. This decision is based on the official PEP8 documentation
where camel case is reserved for classes.
"""

POSSIBLE_GRADES = np.array([-3, 0, 2, 4, 7, 10, 12])


def inputNumber(prompt: str):
    """
    INPUTNUMBER Asks user to input a integer, if input is not an integer, it will ask again.

    Usage: choice = inputNumber(prompt)
    Params: prompt (str): Prompt to be displayed to the user
    Returns: a valid number (integer)
    
    Author: August Borg Ljørring (s224178)
    """

    # Ask user to input a number
    while True:
        try:
            num = int(input(prompt))
            break
        except ValueError:
            print("Not an integer. Try again.")
    return num


def menuHandler(menu_items: list):
    """
    MENUHANDLER Displays the menu of menu_items, ask the user to select an item 
    and returns the selected item. If the input is not valid, it will ask again.

    Usage: choice = menuHandler(menu_items)
    Params: menu_items (array of strings)
    Returns: choice (integer)
    
    Author: August Borg Ljørring (s224178)
    """

    # Display menu
    for i, menu_item in enumerate(menu_items, start=1):
        print(f"{i}. {menu_item}")

    # Ask user to select an item
    choice = 0
    while True:
        choice = inputNumber("Please choose a menu item: ")

        if choice > 0 and choice <= len(menu_items):
            break

        print(
            f"Not a valid menu choice. Please choose a number between 1 and {len(menu_items)}"
        )

    return choice


def dataLoad():
    """
    DATALOAD Asks the user to input a filename, loads the data from the file.
    If the file does not exist, it will ask again.

    Usage: data = dataLoad()
    Params: None
    Returns: Data (numpy array)
    
    Author: August Borg Ljørring (s224178)
    """

    # Load data from csv file
    while True:
        file_name = input("Please enter the name of the file (csv-file with extension) to load: ")
        try:
            df = pd.read_csv(file_name, sep=",")
            break
        except FileNotFoundError:
            print("File not found. Try again.")

    # Show info about the data
    print(f"\n{df}\n")
    print(f"Number of assignments: {len(df.columns) - 2}")
    print(f"Number of students: {len(df.index)}\n")

    return np.array(df)


def checkError(data: np.array, print_errors: bool):
    """
    CHECKERROR Checks for errors in the data along with an option to print the errors.

    Usage: checkError(data, True) for printing out errors or checkError(data, False) for printing out a warning indicating that there are errors in the data. 
    Params: data (np.array), print_errors (bool)
    Returns: true or false (bool) if print_errors is false, otherwise None
    
    Author: Malte Lau (s224183)
    """

    has_error = False
    students = data[:, 0]

    if print_errors:
        print("\nChecking for errors...\n")

    # Checks for student duplicates
    if students.size != np.unique(students).size:
        has_error = True
        if not print_errors:
            return True

        for i, student in enumerate(students, start=2):
            if np.count_nonzero(student == students) > 1:
                print(f"Error: There are multiple occurences of student {student}. This error occurs at line {i}")

    # Checks for grades on the 7-step scale
    for students_num in range(data.shape[0]):
        for assignment_num in range(data.shape[1] - 2):
            if data[students_num, assignment_num + 2] not in POSSIBLE_GRADES:
                has_error = True
                if not print_errors:
                    return True

                else:
                    print(f"Error: Student {data[students_num, 0]} ({data[students_num, 1]}) has recieved an invalid grade in assignment {assignment_num + 1}")

    if not print_errors:
        return

    # Prints whether there are errors or not
    if has_error:
        print("\nErrors found in data. Please attend to the warnings listed above before continuing\n")
    else:
        print("\nNo errors found in data \n")

    return


def displayListOfGrades(data: np.array):
    """
    Displays a list of grades as a dataframe 
    along with a rounded final grade for each student.
    
    Usage: displayListOfGrades(data)
    Params: data (np.array)
    Returns: None
    
    Author: Søren Skov Jensen (s224169)
    """

    # Dataframe creation
    df_columns = np.hstack(("Student ID",
                            "Student Name",
                            np.array([f"A{count}" for count, _ in enumerate(data[0, 2:], start=1)])))

    df = pd.DataFrame(data=data, columns=df_columns)
    final_grades = pd.DataFrame({"Final Grade": computeFinalGrades(data[:, 2:])})
    df = df.join(final_grades)

    # Display dataframe
    print("\nStudent grades for each assignment:")
    with pd.option_context("display.max_rows", None):
        print(df.sort_values(by=["Student Name"]))
    print("")

    # Shows warning if there are errors in the data
    if checkError(data, False):
        print("The list of grades might not be accurate because of errors in your data. You can select the 'check for errors'-option to get further information. \n")

    return


def computeFinalGrades(grades: np.array):
    """
    COMPUTEFINALGRADES Computes the final grade for each student.
    The final is then rounded to the nearest possible grade.

    Usage: final_grades = computeFinalGrades(grades)
    Params: grades (np.array)
    Returns: final_grades_rounded (np.array)
    
    Author: Malte Lau (s224183)
    """

    grades_final = np.zeros(len(grades))

    # Computes final grade for each student
    for i, grade in enumerate(grades):
        if -3 in grade:
            grades_final[i] = -3
        elif len(grade) == 1:
            grades_final[i] = grade[0]
        else:
            grades_final[i] = np.mean(np.delete(grade, np.argmin(grade)))

    final_grades_rounded = roundGrade(grades_final)

    return final_grades_rounded


def roundGrade(grades: np.array):
    """
    ROUNDGRADE Rounds the grades to the nearest possible grade.

    Usage: grades_rounded = roundGrade(grades)
    Params: grades (np.array):
    Returns: grades_rounded (np.array)
    
    Author: Søren Skov Jensen (s224169)
    """

    grades_rounded = np.array([min(POSSIBLE_GRADES, key=lambda x: abs(x - grade)) for grade in grades])

    return grades_rounded


def gradesPlot(grades):
    """
    GRADESPLOT Plots a histogram of the final grades and a scatterplot of the grades 
    for each assignment with the average grade for each assignment as a line.
    
    Usage: gradesPlot(grades)
    Params: grades (np.array)
    Returns: None
    
    Author: August Borg Ljørring (s224178)
    """

    # Shows warning if there are errors in the data
    if checkError(data, False):
        print("The plot might not be accurate! Because of errors in your data, you can run 'check for errors' to get more information\n")

    # Get final grades
    final_grade = computeFinalGrades(grades)

    fig, axs = plt.subplots(1, 2)
    fig.set_size_inches(13, 5)

    # Plots the final grades
    for grade in POSSIBLE_GRADES:
        grade_amount = np.count_nonzero([final_grade == grade])
        axs[0].bar(str(grade), grade_amount, width=0.6)

    axs[0].set_xlabel("Grades")
    axs[0].set_ylabel("Amount of students")
    axs[0].set_title("Final Grades")
    axs[0].grid(axis="y")
    axs[0].yaxis.set_major_locator(plt.MaxNLocator(integer=True))

    grades_for_plot = grades.copy()
    number_of_students = data.shape[0]
    number_of_assignments = data.shape[1] - 2

    XM = []
    YM = []

    # Plotting the points for each assignment
    for i in range(number_of_assignments):
        x = np.ones(number_of_students) * (i + 1)
        x += np.random.uniform(-0.1, 0.1, number_of_students)

        y = grades_for_plot[:, i]
        y += np.random.uniform(-0.1, 0.1, number_of_students)

        axs[1].scatter(x, y, s=30, marker="o", edgecolors="black")

        ym = np.mean(grades_for_plot[:, i])
        XM += [i + 1]
        YM += [ym]

        # Plotting the average grade for each assignment
        axs[1].plot([i + 0.8, i + 1.2], [ym, ym], color="red", linewidth=2)

    # Plotting the mean for each assignment as a line
    axs[1].plot(XM, YM, color="blue", label="Average grade (as line)")

    axs[1].set_yticks(POSSIBLE_GRADES)
    axs[1].set_xticks(np.arange(number_of_assignments) + 1)
    axs[1].set_xlabel("Assignments")
    axs[1].set_ylabel("Grades")
    axs[1].set_title("Grades per Assignment")
    axs[1].set_ylim(-4, 13)
    axs[1].grid()
    axs[1].set_axisbelow(True)
    axs[1].plot([], [], color="red", label="Average grade (per assignment)")
    axs[1].legend()

    print("Plot is shown in a new window, please close the window to continue\n")
    plt.show()

    return


# Main function:
if __name__ == "__main__":
    print("\nWelcome to the gradehelper program!\n")
    data = dataLoad()

    # Main menu
    while True:
        menu_items = np.array(["Load new data.",
                               "Check for errors.",
                               "Generate plots.",
                               "Display list of grades.",
                               "Quit."])

        main_menu_option = menuHandler(menu_items)

        # 1. Load new data
        if main_menu_option == 1:
            data = dataLoad()

        # 2. Check for errors
        elif main_menu_option == 2:
            checkError(data, True)

        # 3. Generate plots
        elif main_menu_option == 3:
            gradesPlot(data[:, 2:])

        # 4. Display list of grades
        elif main_menu_option == 4:
            displayListOfGrades(data)

        # 5. Quit
        elif main_menu_option == 5:
            break