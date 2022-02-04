#---------------------------------------------------------------------#
# File: c:\Adam\Coding\SciPy\richestPeople.py
# Project: c:\Adam\Coding\SciPy
# Created Date: Friday, February 4th 2022, 11:48:34 am
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
# 2022-02-04	AO	Could make the scale better on y axis
# 2022-02-04	AO	Made the data displayed to user
#---------------------------------------------------------------------#
import matplotlib.pyplot as plt
import pandas as pd

rawData = pd.read_csv("billionaires.csv")
dataSet = pd.DataFrame(rawData)
name = dataSet["name"][:10][::-1]
net = dataSet["net_worth"][:10][::-1]
plt.bar(name,net)
plt.xlabel("Name")
plt.xticks(rotation=45)
plt.ylabel("Net worth in Billion")
plt.title("The top 10 richest people and their networth")
plt.show()