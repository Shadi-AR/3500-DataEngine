#Anh Vu
#Edit: Shadi Abdul Razzak
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
    ans = input("Sort in DESC or ASC order: ")
    rows = int(input("Amount of rows to show: "))
    drop = df.drop(columns=(dropInput))
    if ans == 'DESC' and rows > 0:
        drop.sort_values(colUnique, ascending = False, inplace = True)
        result = drop[:rows]
        print(result)
    elif ans == 'ASC' and rows > 0:
        drop.sort_values(colUnique, inplace = True)
        result = drop[:rows]
        print(result)
    else:
        print("Please enter ASC or DESC and a correct number of rows")
        return
    
    #Search input values
    searchColInput = input("Columns to search for: ")
    searchCol = df[searchColInput]
    print(searchCol)
    searchInput = input("Values to search for: " )
    counting = 0
    """
    for i in searchCol:
        if str(i) in searchInput:
            counting += 1
            print(df.loc[i])
    print(counting)
"""
    totalRow = 0
    for i in searchCol:
        totalRow+=1
        if str(i) in searchInput:
            counting += 1
            print("Elements found in row: ", end= " ")
            print(totalRow)
    print("Elements were found in ", end= "" )
    print(counting, end =" ")
    print("rows")

#call function
readByPandas(fname)
