import tkinter as tk
import csv
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
from bmi6018_mod_display import *

def show_results():

    Select_Patient(int(e1.get()))

    # open file
    with open("patient_search.csv", newline = "") as f:
        reader = csv.reader(f)

        # r and c tell us where to grid the labels
        r = 0
        for col in reader:
            c = 4 #shift column over two to display input and output
            for row in col:
               
                label = tk.Label(master, width = 15, height = 2, 
                                    text = row, relief = tk.RIDGE, wraplength = 100)
                label.grid(row = r, column = c)
                c += 1
            r += 1
    
    Select_Provider(int(e2.get()))

    # open file
    with open("provider_search.csv", newline = "") as g:
        reader = csv.reader(g)

        # r and c tell us where to grid the labels
        a = r
        for col in reader:
            c = 4 #shift column over two to display input and output
            for row in col:
               
                label = tk.Label(master, width = 15, height = 2, 
                                    text = row, relief = tk.RIDGE, wraplength = 100)
                label.grid(row = a, column = c)
                c += 1
            a += 1
    
    all_search(str(e3.get()))

    # open file
    with open("category_search.csv", newline = "") as h:
        reader = csv.reader(h)

        # r and c tell us where to grid the labels
        m = a
        for col in reader:
            c = 4 #shift column over two to display input and output
            for row in col:
                
                label = tk.Label(master, width = 15, height = 2, 
                                    text = row, relief = tk.RIDGE, wraplength = 100)
                label.grid(row = m, column = c)
                c += 1
            m += 1
    
master = tk.Tk()
tk.Label(master, 
         text="Patient lookup by ID (integer):").grid(row=0)
tk.Label(master, 
         text="Provider lookup by ID (1-10):").grid(row=1)
tk.Label(master, 
         text="Display characteristics of given category (numerical data will show min first then max):",wraplength = 100).grid(row=2)

e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

tk.Button(master, 
          text='Quit', 
          command=master.quit).grid(row=3, 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=4)
tk.Button(master, 
          text='Show', command=show_results).grid(row=3, 
                                                       column=1, 
                                                       sticky=tk.W, 
                                                       pady=4)

tk.mainloop()