import csv
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

p_df = pd.read_csv('./patientdata.csv')

#clean up column formatting for easier retrieval
p_df.columns = p_df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace('-', '_').str.replace(',','_').str.replace('/','_')

#Function that finds patient based on patient ID
def Select_Patient(p):
    pt = p_df.loc[p_df['patient_id'] == p]

    with open('patient_search.csv', 'w', newline=''):
        pt.to_csv('patient_search.csv', index = False, header = True)


#Finds patients that provider is responsible for
def Select_Provider(p):
    pr = p_df.loc[p_df['provider_id'] == p]

    with open('provider_search.csv', 'w', newline=''):
        pr.to_csv('provider_search.csv', index = False, header = True)

#Find youngest and oldest patient(s)
def minmax_Age():
    minage = p_df[p_df.age_years == p_df.age_years.min()]
    maxage = p_df[p_df.age_years == p_df.age_years.max()]
    return minage, maxage

#Find shortest and tallest patient(s)
def minmax_Height():
    short = p_df[p_df.height_cm == p_df.height_cm.min()]
    tall = p_df[p_df.height_cm == p_df.height_cm.max()]
    return short, tall

#Find lightest and heaviest patient(s)
def minmax_Weight():
    light = p_df[p_df.weight_kg == p_df.weight_kg.min()]
    heavy = p_df[p_df.weight_kg == p_df.weight_kg.max()]
    return light, heavy

#Find patient(s) with lowest and highest BMI
def minmax_BMI():
    lBMI = p_df[p_df.bmi == p_df.bmi.min()]
    hBMI = p_df[p_df.bmi == p_df.bmi.max()]
    return lBMI, hBMI

#Find coldest and hottest patient(s)
def minmax_Temp():
    cold = p_df[p_df.temperature_degrees_celsius == p_df.temperature_degrees_celsius.min()]
    hot = p_df[p_df.temperature_degrees_celsius == p_df.temperature_degrees_celsius.max()]
    return cold, hot

#Find patient(s) with slowest and fastest pulse
def minmax_Pulse():
    slowpulse = p_df[p_df.pulse_bpm == p_df.pulse_bpm.min()]
    fastpulse = p_df[p_df.pulse_bpm == p_df.pulse_bpm.max()]
    return slowpulse, fastpulse

#Find patient(s) with slowest and fastest respiratory rate
def minmax_RR():
    slowrr = p_df[p_df.respiratory_rate_breaths_per_minute == p_df.respiratory_rate_breaths_per_minute.min()]
    fastrr = p_df[p_df.respiratory_rate_breaths_per_minute == p_df.respiratory_rate_breaths_per_minute.max()]
    return slowrr, fastrr

#Find patient(s) in the least and most pain
def minmax_Pain():
    minpain = p_df[p_df.pain_scale_1_10__10_is_worst == p_df.pain_scale_1_10__10_is_worst.min()]
    maxpain = p_df[p_df.pain_scale_1_10__10_is_worst == p_df.pain_scale_1_10__10_is_worst.max()]
    return minpain, maxpain

#Find patient(s) with lowest and highest total cholesterol
def minmax_Chol():
    minchol = p_df[p_df.total_cholesterol_mg_dl == p_df.total_cholesterol_mg_dl.min()]
    maxchol = p_df[p_df.total_cholesterol_mg_dl == p_df.total_cholesterol_mg_dl.max()]
    return minchol, maxchol

#Find patient(s) with lowest and highest total white blood cell count
def minmax_WBC():
    minWBC = p_df[p_df.white_blood_cell_count_cmm == p_df.white_blood_cell_count_cmm.min()]
    maxWBC = p_df[p_df.white_blood_cell_count_cmm == p_df.white_blood_cell_count_cmm.max()]
    return minWBC, maxWBC

#Find patient(s) with lowest and highest vitamin D
def minmax_D():
    minD = p_df[p_df.vitamin_d_ng_ml == p_df.vitamin_d_ng_ml.min()]
    maxD = p_df[p_df.vitamin_d_ng_ml == p_df.vitamin_d_ng_ml.max()]
    return minD, maxD

#Find patient(s) with lowest and highest sodium
def minmax_Sodium():
    minsodium = p_df[p_df.sodium_meq_l == p_df.sodium_meq_l.min()]
    maxsodium = p_df[p_df.sodium_meq_l == p_df.sodium_meq_l.max()]
    return minsodium, maxsodium

#Find patient(s) with lowest and highest albumin
def minmax_Albumin():
    minalbumin = p_df[p_df.albumin_g_dl == p_df.albumin_g_dl.min()]
    maxalbumin = p_df[p_df.albumin_g_dl == p_df.albumin_g_dl.max()]
    return minalbumin, maxalbumin

#Find frequency of patient sex
def what_Sex():
    wSex = p_df['sex'].value_counts()
    return wSex

#Find frequency of patient resident state
def what_State():
    wState = p_df['state'].value_counts()
    return wState

#Find frequency of visit types
def what_Visit():
    wVisit = p_df['visit_type'].value_counts()
    return wVisit

#Find frequency of disease at admission
def what_Disease():
    wDisease = p_df['disease_at_admission'].value_counts()
    return wDisease

#Find frequency of comorbidities
def what_Comorbid():
    wComorbid = p_df['comorbidities'].value_counts()
    return wComorbid



#List to string
def ListToString(s):
    str_new = ""
    for i in s:
        str_new += i
    return str_new



#Combine all searches

def all_search(x):
    catsim = [i for i in p_df.columns if x in i] #partial match string to columns
    catsim = ListToString(catsim)

    catalog_func = [
        minmax_Age,
        what_Sex,
        what_State,
        what_Visit,
        minmax_Height,
        minmax_Weight,
        minmax_BMI,
        minmax_Temp,
        minmax_Pulse,
        minmax_RR,
        minmax_Pain,
        minmax_Chol,
        minmax_WBC,
        minmax_D,
        minmax_Sodium,
        minmax_Albumin,
        what_Disease,
        what_Comorbid
    ]
        
    
    for i in range(len(catalog_func)): 
        if catsim == p_df.columns[i+2]:   #match user input from partial match to correct category, shift index read up 2 because patient and provider ID used separately
            if type(catalog_func[i]()) == type(what_Sex()):         #functions have two outputs, one is a panda series and other is tuples. This conditional accounts for both and exports to csv
                df = catalog_func[i]()
                with open('category_search.csv', 'w', newline=''):
                    df.to_csv('category_search.csv', header = True)
            else:
                tuples = catalog_func[i]()
                with open('category_search.csv', 'w', newline=''):
                    df1 = tuples[0]
                    df2 = tuples[1]
                    pd.concat([df1, df2]).to_csv('category_search.csv', index = False, header = True)


          
