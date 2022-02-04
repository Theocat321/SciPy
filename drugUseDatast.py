#---------------------------------------------------------------------#
# File: c:\Adam\Coding\SciPy\drugUseDatast.py
# Project: c:\Adam\Coding\SciPy
# Created Date: Friday, January 28th 2022, 12:09:23 pm
# Description: 
# Author: Adam O'Neill
# Copyright (c) 2022 Adam O'Neill
# -----
# Last Modified: Fri Jan 28 2022
# Modified By: Adam O'Neill
# -----
# HISTORY:
# Date      	By	Comments
# ----------	---	---------------------------------------------------------
# 2022-01-28	AO	Testing getting data sets from url with pandas
#---------------------------------------------------------------------#
import pandas as pd
import numpy as np

csv = pd.read_csv("https://raw.githubusercontent.com/fivethirtyeight/data/master/drug-use-by-age/drug-use-by-age.csv")

columnHeadingArray = list(csv.columns)
ageArray = csv["age"].to_numpy()
alcohol_useArray = csv["alcohol-use"].to_numpy()
print(ageArray,alcohol_useArray)

f = open("Age-AlcholUse.csv","w")
f.write(columnHeadingArray[0]+","+columnHeadingArray[2]+"\n")
for x in range(len(ageArray)-1):
    
    f.write(str(ageArray[x])+","+str(alcohol_useArray[x])+"\n")
f.close()