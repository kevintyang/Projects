from stats_file_GUI_ONLY import *
import tkinter as tk
import csv


def show_csv():

    num_stats(e1.get(), e2.get(), e3.get())



    # open file
    with open("stat_search.csv", newline = "") as f:
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
         text="Narrow by male or female:").grid(row=0)
tk.Label(master, 
         text="Narrow by young or senior:").grid(row=1)
tk.Label(master, 
         text="Search what category (lowercase):").grid(row=2)

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
          text='Show', command=show_csv).grid(row=3, 
                                                       column=1, 
                                                       sticky=tk.W, 
                                                       pady=4)

tk.mainloop()