from roundgrade import roundGrade
from computefinalgrade import computeFinalGrades
from gradesplot import gradesPlot

import pandas as pd
import numpy as np

def main():
    grades = None
    roundGrade(grades)
    computeFinalGrades(grades)
    gradesPlot(grades)

if __name__ == '__main__':
    main()