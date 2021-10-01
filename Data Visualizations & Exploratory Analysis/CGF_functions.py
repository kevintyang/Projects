def col_stats(list,column):
    #input list of dataframes for analysis
    #input column for needed stats, as string

    for i,table in enumerate(list):
        table[column].describe().T
