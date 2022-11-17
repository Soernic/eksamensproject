import numpy as np

def computeFinalGrades(grades):
    gradesFinal = np.zeros(len(grades, axis=0))
    for i in range(0,len(grades)):
        if -3 in grades[i]:
            gradesFinal[i] = -3
        elif len(grades) == 1:
            gradesFinal[i] = grades[i]
        else:
            gradesFinal[i] = np.mean(grades[i]-min(grades[i]))
    return gradesFinal

print(computeFinalGrades(np.array([[10,12,7,4],[12,10],[7,4,-3],[2],[-3]])))