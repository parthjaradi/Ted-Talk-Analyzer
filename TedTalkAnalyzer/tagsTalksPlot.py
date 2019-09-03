# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 21:08:03 2019

@author: My Pc
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tkinter import messagebox


#Function to create graph for Number of Talks Vs Tags

def tagsTalksPlot(dataset):
    tags = []
    for i in range(len(dataset.loc[:,'tags'])):
        ls = list(dataset.loc[:,'tags'])[i][2:-2].split(',')
        for c in range(len(ls)):
            value= list(dataset.loc[:,'tags'])[i][2:-2].split(',')[c]
            tags.append(value.replace("'",""))
    tags = pd.DataFrame(tags,columns=["tags"])
    tags.iloc[:,0].value_counts().head(10)
    tags = pd.DataFrame(tags.iloc[:,0].value_counts()).reset_index()
    plt.figure(figsize=(15,5))
    sns.barplot(x=tags["index"].head(10),y=tags["tags"].head(10))
    plt.xlabel("tags")
    plt.ylabel("talks")
    plt.savefig("tagTalk.png")


#Function to count Number of Tags per year 
def tagsCountYearly(dataset,year,listTags):
    tags = []
    dataset = dataset[dataset["published_year"]==year]
    for i in range(len(dataset.loc[:,'tags'])):
        ls = list(dataset.loc[:,'tags'])[i][2:-2].split(',')
        for c in range(len(ls)):
            value= list(dataset.loc[:,'tags'])[i][2:-2].split(',')[c]
            tags.append(value.replace("'",""))
    tags=pd.DataFrame(tags,columns=["tags"])
    
    print("\n","\n",tags["tags"].value_counts().head(10))
    
  
#%%