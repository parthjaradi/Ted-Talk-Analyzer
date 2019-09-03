# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 17:52:31 2019

@author: My Pc
"""

#Function to create graph for Number of Talks Vs Published_Year
import matplotlib.pyplot as plt
import seaborn as sns

def pubYearPlot(dataset):
    plt.figure(figsize=(15,5))
    sns.countplot(dataset["published_year"])
    plt.savefig("pyp.png")
#%%