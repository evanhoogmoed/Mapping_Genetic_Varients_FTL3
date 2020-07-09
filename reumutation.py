# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 20:59:34 2020

@author: emmav
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np  
#create dataframe from excel file using desired columns
dfControl = pd.read_excel(r'C:\Users\emmav\reumutation\flt3Controlpop.xlsx',index_col=None,na_values=['NaN'])

dfCancer = pd.read_excel(r'C:\Users\emmav\reumutation\amlmutation.xlsx',index_col=None,na_values=['NaN'],usecols = "D,G,O,P,AA,AB")


def lollipop(df):
    missenserows = df[df['Mutation Type'] == 'Missense_Mutation']
    countm = missenserows.groupby(['Protein Change','Start Pos']).size().reset_index(name="Number")
    mvalues = countm["Number"].to_numpy()
    mlocation = countm["Start Pos"].to_numpy()
    plt.stem(mlocation,mvalues,markerfmt='o', label='Missense')
    
    ifrows = df[df['Mutation Type'] == 'In_Frame_Ins']
    countif = ifrows.groupby(['Protein Change','Start Pos']).size().reset_index(name="Number")
    ifvalues = countif["Number"].to_numpy()
    iflocation = countif["Start Pos"].to_numpy()
    plt.stem(iflocation,ifvalues,markerfmt='o', label='In Frame')
    
    nrows = df[df['Mutation Type'] == 'Nonsense_Mutation']
    countn = nrows.groupby(['Protein Change','Start Pos']).size().reset_index(name="Number")
    nvalues = countn["Number"].to_numpy()
    nlocation = countn["Start Pos"].to_numpy()
    plt.stem(nlocation,nvalues,markerfmt='o', label='Nonsense')
    
    
    plt.legend()
    plt.show()

def main():
    lollipop(dfCancer)
    
if __name__ == "__main__":
    main()
