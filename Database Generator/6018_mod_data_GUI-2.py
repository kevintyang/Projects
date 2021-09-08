import tkinter as tk
from bmi6018_mod_data import *

def show_csv():

    All_Gen(int(e1.get()))

    # open file
    with open("patientdata.csv", newline = "") as f:
        reader = csv.reader(f)

        # r and c tell us where to grid the labels
        r = 0
        for col in reader:
            c = 2 #shift column over two to display input and output
            for row in col:
                # i've added some styling
                label = tk.Label(master, width = 15, height = 3, 
                                    text = row, relief = tk.RIDGE, wraplength = 100)
                label.grid(row = r, column = c)
                c += 1
            r += 1
        
master = tk.Tk()
tk.Label(master, 
         text="How many patients would you like to generate?", wraplength = 120).grid(row=0)

e1 = tk.Entry(master, width = 10)

e1.grid(row=0, column=1)


tk.Button(master, 
          text='Quit', 
          command=master.quit).grid(row=3, 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=4)
tk.Button(master, 
          text='Show', command=show_csv).grid(row=3, 
                                                       column=1, 
                                                       sticky=tk.W, 
                                                       pady=4)

tk.mainloop()