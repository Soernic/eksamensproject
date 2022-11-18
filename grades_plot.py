import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def gradesPlot(data):

    finalGrade = np.array([12, 12, 10, 7, 4, 2, -3,0,0,0])

    fig, axs = plt.subplots(1, 2)
    fig.set_size_inches(13, 5)

    # Plot the grades
    gradeList = [-3, 0, 2, 4, 7, 10, 12]

    for i in gradeList:
        b = np.count_nonzero([finalGrade == i])
        axs[0].bar(str(i), b, width=0.6)

    axs[0].set_xlabel('Grades')
    axs[0].set_ylabel('Amount of students')
    axs[0].set_title('Bar plot of grades')
    axs[0].grid(axis='y')
    axs[0].yaxis.set_major_locator(plt.MaxNLocator(integer=True))

    #import data from file
    dataCSV = pd.read_csv('grades.csv', sep=',')
    data = np.array(dataCSV)

    grades = data[:, 2:]

    assignments = len(grades[0])

    for i in range(len(gradeList)):
        grades[grades == gradeList[i]] = str(i)

    grades = grades.astype(float)

    # plot each assignment on the x-axis and the grades on the y-axis as a scatter plot, add random noise to the y-axis to avoid overlapping points
    for i in range(assignments):
        y = grades[:, i]
        y += np.random.normal(0, 0.1, len(y))

        x = np.ones(len(y)) * i
        x += np.random.normal(0, 0.1, len(y))

        axs[1].scatter(x, y, s=30, marker='o', edgecolors='black')

    axs[1].set_yticklabels(['', '-3', '0', '2', '4', '7', '10', '12'])
    axs[1].set_xticks(np.arange(assignments))
    axs[1].set_xlabel('Assignments')
    axs[1].set_ylabel('Grades')
    axs[1].set_title('Grades for each assignment')
    axs[1].legend()

    # shows the plot
    plt.show()

gradesPlot("")

