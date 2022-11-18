import pandas as pd
import numpy as np

def dataLoad():
    # Load data from file grades.csv
    while True:
        filename = input("Please enter the name of the file to load: ")
        
        try:
            dataCSV = pd.read_csv(filename, sep=',')
            break
        except FileNotFoundError:
            print('File not found. Try again.')
            pass

    # Extract the assignments and students
    assignments = len(dataCSV.columns) - 2
    #number of rows in the data
    students = len(dataCSV.index)

    return dataCSV, assignments, students