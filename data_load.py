import pandas as pd
import numpy as np

'''
The dataLoad function should contain the following:
- A while loop that runs until the user enters a valid file name.
- A call to the read_csv function from the pandas library to load the data from the file.
- A print statement that displays the data.
- A print statement that displays the number of assignments and the number of students.
- A return statement that returns the data as a numpy array.

params: None
returns: data as a numpy array
'''

def dataLoad():
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