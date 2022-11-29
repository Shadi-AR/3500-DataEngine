#Anh Vu
#This is the method to load files

import pandas as pd

fname = '/home/fac/walter/public_html/courses/cs3500/2022_fall/proj/data/2019_Airline_Delays_Dataset_train_Part1.csv' 

def readByPandas(fname):
    df = pd.read_csv(fname)
    count = 0
    #Printing Column Names
    for colName in range (26):
        colName = df.iloc[0:0, colName].name
        print (colName) 


    #print unique values of chosen columns
    colUnique = input("Unique values of columns :")
    uniqueVal = df[colUnique].unique()
    print ("Unique values of chosen values are:", end = " ")
    print (uniqueVal)
    
    #Counting unique values
    for i in uniqueVal:
        if i != (i+1):
            count += 1
    print("Unique values of this columns:", end = " ")
    print(count)

    #Drop a column
    dropInput = input("Name of columns to drop: ")
    drop = df.drop(columns=(dropInput))
    print(drop)


#call function
readByPandas(fname)








