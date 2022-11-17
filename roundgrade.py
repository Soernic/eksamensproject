import numpy as np
import pandas as pd


def roundGrade(grades: np.array):
    
    possible_grades = np.array([-3, 0, 2, 4, 7, 10, 12])
    gradesRounded = np.array([])
    
    for grade in grades:
        gradesRounded = np.append(gradesRounded, min(possible_grades, key=lambda x: abs(x - grade)))
    
    return gradesRounded

