def computeFinalGrades(gradesRounded):
    gradesFinal = []
    for i in range(0, len(gradesRounded)):
        if len(gradesRounded[i]) == 1:
            gradesFinal.append(gradesRounded[i][0])
        else:
            gradesFinal.append((sum(gradesRounded)-min(gradesRounded))/len(gradesRounded))
        gradesFinal.append(gradesRounded[i])
    
    return gradesFinal
