
from numpy import random
import csv


#Patient ID Generator, sequential counter 
def Patient_ID_Gen(n):
    PID = []
    for i in range(1,n+1):
        PID.append(i)
    return PID

#Provider ID Generator
def Provider_ID_Gen(n):
    PrID = []
    for i in range(n):
        PrID.append(random.randint(1,10))
    return PrID

#Age Generator
def Age_Gen(n):
    Age_List = []
    for i in range(n):
        Age_List.append(random.randint(1,100))
    return Age_List

#Sex Generator
def Sex_Gen(n):
    Sex_List = []
    for i in range(n):
        Sex_x_chrom = random.randint(1,3)
        if Sex_x_chrom == 1:
            Sex_List.append('male')
        else:
            Sex_List.append('female')
    return Sex_List

#State Generator
def State_Gen(n):
    States = ['Washington','Oregon','California','Arizona','New Mexico','Texas','Idaho','Nevada','Utah','Colorado']
    State_List = []
    for i in range(n):
        State_List.append(random.choice(States))
    return State_List

#Visit Type Generator
def Visit_Type_Gen(n):
    Visit_Types = ['Office Visit','Physical','Urgent Visit','Surgery', 'Observation']
    Visit_Types_List = []
    for i in range(n):
        Visit_Types_List.append(random.choice(Visit_Types))
    return Visit_Types_List

#Height Generator in cm
def Height_Gen(n):
    Height_List = []
    for i in range(n):  
        Height_List.append(random.randint(147,194))
    return Height_List

#Weight Generator in kg
def Weight_Gen(n):
    Weight_List = []
    for i in range(n):
        Weight_List.append(random.randint(41,146))
    return Weight_List

#BMI Generator
def BMI_Gen(n):
    BMI_List = []
    hBMI = Height_Gen(n) #Call Height and Weight Generator
    wBMI = Weight_Gen(n)
    for i in range(n):
        x = (round(wBMI[i]/((hBMI[i]/100)**2),2)) #Convert height and weight to BMI
        BMI_List.append(x)
    return BMI_List

#Temperature Generator
def Temperature_Gen(n):
    Temperature_List = []
    for i in range(n):  
        new_temp = round(random.uniform(13.7,46.5),2)
        Temperature_List.append(new_temp)
    return Temperature_List

#Pulse Generator
def Pulse_Gen(n):
    Pulse_List = []
    for i in range(n):
        Pulse_List.append(random.randint(0,480))
    return Pulse_List

#Respiratory Rate Generator
def Respiratory_Rate_Gen(n):
    RR_List = []
    for i in range(n):
        RR_List.append(random.randint(0,50))
    return RR_List

#Pain Generator
def Pain_Gen(n):
    Pain_List = []
    for i in range(n):
        Pain_List.append(random.randint(0,10))
    return Pain_List

#Total Cholesterol Generator
def Cholesterol_Gen(n):
    Chol_List = []
    for i in range(n):
        Chol_List.append(random.randint(0,3165))
    return Chol_List

#White Blood Cell Count Generator
def WBC_Gen(n):
    WBC_List = []
    for i in range(n):
        WBC_List.append(random.randint(0,20000))
    return WBC_List

#Vitamin D Generator
def D_Gen(n):
    D_List = []
    for i in range(n):
        D_List.append(random.randint(0,86))
    return D_List

#Sodium Generator
def Sodium_Gen(n):
    Sodium_List = []
    for i in range(n):
        Sodium_List.append(random.randint(0,300))
    return Sodium_List

#Albumin Generator
def Albumin_Gen(n):
    Albumin_List = []
    for i in range(n):
        alb_new = round(random.uniform(0,10),2)
        Albumin_List.append(alb_new)
    return Albumin_List

#Disease at Admission Generator
def Disease_Gen(n):
    Diseases = ['Cancer', 'Alzheimers', 'Diabetes', 'Pneumonia', 'Chronic Kidney Disease']
    Disease_List = []
    for i in range(n):
        Disease_List.append(random.choice(Diseases))
    return Disease_List

#Comorbidities
def Comorbidities_Gen(n):
    Comorbidities = ['Heart Disease', 'Arthritis', 'Obesity', 'Bronchitis', 'Vascular Dementia']
    Comorbidities_List = []
    for i in range(n):
        Comorbidities_List.append(random.choice(Comorbidities))
    return(Comorbidities_List)

#Function that creates list of dictionary of patient values

def All_Gen(n):
    all_pid = Patient_ID_Gen(n)  
    all_prid = Provider_ID_Gen(n)
    all_age = Age_Gen(n)
    all_sex = Sex_Gen(n)
    all_state = State_Gen(n)
    all_visit = Visit_Type_Gen(n)
    all_height = Height_Gen(n)
    all_weight = Weight_Gen(n)
    all_bmi = BMI_Gen(n)
    all_temp = Temperature_Gen(n)
    all_pulse = Pulse_Gen(n)
    all_rr = Respiratory_Rate_Gen(n)
    all_pain = Pain_Gen(n)
    all_chol = Cholesterol_Gen(n)
    all_wbc = WBC_Gen(n)
    all_d = D_Gen(n)
    all_sodium = Sodium_Gen(n)
    all_albumin = Albumin_Gen(n)
    all_disease = Disease_Gen(n)
    all_comorbid = Comorbidities_Gen(n)

    all_dictionary = []

    for i in range(n):  #Creating a dictionary per patient and then adding them to a list
        patient_dict = {
            'Patient ID':all_pid[i],
            'Provider ID':all_prid[i],
            'Age (years)':all_age[i],
            'Sex':all_sex[i],
            'State':all_state[i],
            'Visit_Type':all_visit[i],
            'Height (cm)':all_height[i],
            'Weight (kg)':all_weight[i],
            'BMI':all_bmi[i],
            'Temperature (degrees Celsius)':all_temp[i], 
            'Pulse (bpm)':all_pulse[i], 
            'Respiratory Rate (breaths per minute)':all_rr[i],
            'Pain (Scale 1-10, 10 is worst)':all_pain[i], 
            'Total Cholesterol (mg/dL)':all_chol[i], 
            'White Blood Cell Count (cmm)':all_wbc[i], 
            'Vitamin D (ng/mL)':all_d[i], 
            'Sodium (mEq/L)':all_sodium[i], 
            'Albumin (g/dL)':all_albumin[i], 
            'Disease at Admission':all_disease[i], 
            'Comorbidities':all_comorbid[i]
            }
        all_dictionary.append(patient_dict)
    
    with open('patientdata.csv', 'w', newline='') as f:

        #Patient data categories that will be fieldnames for the csv
        patient_categories = [
            'Patient ID', 
            'Provider ID', 
            'Age (years)', 
            'Sex', 
            'State', 
            'Visit_Type', 
            'Height (cm)', 
            'Weight (kg)', 
            'BMI', 
            'Temperature (degrees Celsius)', 
            'Pulse (bpm)', 
            'Respiratory Rate (breaths per minute)',
            'Pain (Scale 1-10, 10 is worst)', 
            'Total Cholesterol (mg/dL)', 
            'White Blood Cell Count (cmm)', 
            'Vitamin D (ng/mL)', 
            'Sodium (mEq/L)', 
            'Albumin (g/dL)', 
            'Disease at Admission', 
            'Comorbidities'
            ]
        writer = csv.DictWriter(f, fieldnames = patient_categories)
        
        writer.writeheader()
        writer.writerows(all_dictionary)

All_Gen(300)
