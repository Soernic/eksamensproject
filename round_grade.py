
import numpy as np
import pandas as pd


def roundGrade(grades: np.array):
    """_summary_

    Args:
        grades (np.array): _description_

    Returns:
        _type_: _description_
    """
    
    # Function takes vector of grades and rounds them to the nearest appropriate grade to correct for potential data errors.
    possible_grades = np.array([-3, 0, 2, 4, 7, 10, 12])
    gradesRounded = np.array([])
    
    for grade in grades:
        gradesRounded = np.append(gradesRounded, min(possible_grades, key=lambda x: abs(x - grade)))
    
    return gradesRounded

