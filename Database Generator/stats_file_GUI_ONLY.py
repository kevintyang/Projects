#%%%

#This file has no boxplot since I don't know how to plot in tkinter. This is only for GUI display over other outputs, refer to my other mod stat for how I used boxplot without UI

import csv
import pandas as pd
import warnings
import matplotlib.pyplot as plt
import numpy
warnings.filterwarnings('ignore')

p_df = pd.read_csv('./patientdata.csv')

#clean up column formatting for easier retrieval
p_df.columns = p_df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace('-', '_').str.replace(',','_').str.replace('/','_')

#Construct male/female and old/young dataframe
def fetch_df(whatsex, youngorsenior):
    whatdf = p_df
    if whatsex == 'male':
        sex_df = whatdf[whatdf['sex'] == whatsex]
    elif whatsex == 'female':
        sex_df = whatdf[whatdf['sex'] == whatsex]

    if youngorsenior == 'young':
        agesex_df = sex_df[sex_df['age_years'] < 65]
    elif youngorsenior == 'senior':
        agesex_df = sex_df[sex_df['age_years'] >= 65]

    return agesex_df

#List to string
def ListToString(s):
    str_new = ""
    for i in s:
        str_new += i
    return str_new


def num_stats(whatsex, youngorsenior, whatcat):
    whatdf = p_df
    db = fetch_df(whatsex, youngorsenior) #construct dataframe with constraints

    whatcat = [i for i in db.columns if whatcat in i] #partial match category input
    whatcat = ListToString(whatcat)
    
    test = p_df.iloc[0][whatcat] 

    if type(test) == str:      #if output is a string, then must be categorical data
        countcat = db[whatcat].value_counts()
        
        countcat.to_csv('stat_search.csv')
    
    else:                     #The rest are numerical
        mincat = db[whatcat].min()
        maxcat = db[whatcat].max()
        meancat = db[whatcat].mean()

        header = ['min','max','mean']        #write min,max,mean to csv for GUI
        values = [{'min':mincat, 'max':maxcat, 'mean':meancat}]
        with open('stat_search.csv', 'w', newline='') as f: 
            writer = csv.DictWriter(f, fieldnames = header)
        
            writer.writeheader()
            writer.writerows(values)  

    

# %%
