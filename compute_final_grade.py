import numpy as np

def computeFinalGrades(grades):
    gradesFinal = np.zeros(len(grades))
    
    for i in range(len(grades)):
        if -3 in grades[i]:
            gradesFinal[i] = -3
        elif len(grades[i]) == 1:
            gradesFinal[i] = grades[i][0]
        else:
            grades[i].remove(np.min(grades[i]))
            gradesFinal[i] = np.mean(grades[i])
    return gradesFinal