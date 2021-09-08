#%%%
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
    else:
        sex_df = whatdf[whatdf['sex'] == whatsex]

    if youngorsenior == 'young':
        agesex_df = sex_df[sex_df['age_years'] < 65]
    else:
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

    if type(test) == numpy.int64: #match integer output
        mincat = db[whatcat].min()
        maxcat = db[whatcat].max()
        meancat = db[whatcat].mean()
        boxplot = plt.boxplot(db[whatcat])

        return mincat, maxcat, meancat, boxplot         #boxplot plots with jupyter (deprecated) extension
    
    elif type(test) == numpy.float64:   #match float output
        mincat = db[whatcat].min()
        maxcat = db[whatcat].max()
        meancat = db[whatcat].mean()
        boxplot = plt.boxplot(db[whatcat])

        return mincat, maxcat, meancat, boxplot

    elif type(test) == str: #if output is a string, then must be categorical data
        countcat = db[whatcat].value_counts()

        return countcat

        

print(num_stats('male', 'young', 'bmi'))


    

# %%
