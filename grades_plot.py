import matplotlib.pyplot as plt
import numpy as np

'''
The function gradesPlot takes a numpy array as input and plots the grades in a bar plot and a scatter plot.
The bar plot shows the amount of students that got each grade.
The scatter plot shows the grades for each assignment. The x-axis shows the assignment number and the y-axis shows the grade.

params: data - a numpy array containing the grades for each student and assignment
returns: nothing
'''

def gradesPlot(data):

    finalGrade = np.array([12, 12, 10, 7, 4, 2, -3,0,0,0])

    fig, axs = plt.subplots(1, 2)
    fig.set_size_inches(13, 5)

    # Plot the grades
    gradeList = [-3, 0, 2, 4, 7, 10, 12]

    for grade in gradeList:
        gradeAmount = np.count_nonzero([finalGrade == grade])
        axs[0].bar(str(grade), gradeAmount, width=0.6)

    axs[0].set_xlabel('Grades')
    axs[0].set_ylabel('Amount of students')
    axs[0].set_title('Bar plot of grades')
    axs[0].grid(axis='y')
    axs[0].yaxis.set_major_locator(plt.MaxNLocator(integer=True))

    grades = data[:, 2:]

    assignments = len(grades[0])

    for i in range(assignments):
        y = grades[:, i]
        y += np.random.normal(0, 0.1, len(y))

        x = np.ones(len(y)) * (i+1)
        x += np.random.normal(0, 0.1, len(y))

        axs[1].scatter(x, y, s=30, marker='o', edgecolors='black')

    axs[1].set_yticks([-3, 0, 2, 4, 7, 10, 12])
    axs[1].set_xticks(np.arange(assignments)+1)
    axs[1].set_xlabel('Assignments')
    axs[1].set_ylabel('Grades')
    axs[1].set_title('Grades for each assignment')
    axs[1].grid()
    axs[1].set_axisbelow(True)
    # axs[1].legend()

    # shows the plot
    plt.show()

