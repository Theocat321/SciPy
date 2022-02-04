#---------------------------------------------------------------------#
# File: c:\Adam\Coding\SciPy\studentsPerYearGraph.py
# Project: c:\Adam\Coding\SciPy
# Created Date: Friday, February 4th 2022, 11:36:25 am
# Description: 
# Author: Adam O'Neill
# Copyright (c) 2022 Adam O'Neill
# -----
# Last Modified: Fri Feb 04 2022
# Modified By: Adam O'Neill
# -----
# HISTORY:
# Date      	By	Comments
# ----------	---	---------------------------------------------------------
#---------------------------------------------------------------------#
import matplotlib.pyplot as plt


# Bar chart
years = ["Year 7","Year 8","Year 9","Year 10","Year 11","Sixth form"]
numStudents = [198,211,189,190,176,124]
plt.bar(years,numStudents)
plt.title("A graph to show the number of students to people in year")
plt.xlabel("Year group")
plt.ylabel("Number of students")
plt.show()

# Box plot

data = [3,7,5,4,8]
plt.boxplot(data,vert=False)
plt.show()