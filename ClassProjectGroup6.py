#------------------------------
# CMPS 3500 - Class Project: Basic Data Analysis Engine
#
# Jarl Ramos
# Alonso Cardenas Sillas
# Anh Vu
# Shadi Abdul Razzak
#---------------------------

# Main file
# import openFile
import mathlibrary as ml
import openFile2 as of2
# myList = [ 1, 4, 2, 8, -3, 4, 3, -5, 6, 6, 7, 2, 7, 9, 1, 0] # 16 random items
str_filename = "datasampleTwo.csv"
# list fileformat must be right after opening the file
#  because the first line is the format
myGen = of2.gen_open_file(str_filename)
list_fileformat = next(myGen)
list_fileformat = of2.get_columns(list_fileformat)
dict_fileformat = of2.create_dict(list_fileformat)
name = []

list_myColumns = of2.drop_col(dict_fileformat, list_fileformat, "Month") 
c = 0
print(list_myColumns)
#c = ml.minimum(myList)
#print(c)