import numpy as np
from roundgrade import roundGrade
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
            roundGrade(gradesFinal[i])
    return gradesFinal

print(computeFinalGrades(np.array([[10,12,7,4],[12,10],[7,4,-3],[2],[-3]])))