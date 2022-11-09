#------------------------------
# CMPS 3500 - Class Project: Basic Data Analysis Engine
#
# Jarl Ramos
# Alonso Cardenas Sillas
# Anh Vu
# Shadi Abdul Razzak
#---------------------------

# Main file
import openFile
import mathlibrary as ml
myArray = [ 1, 4, 2, 8, 3, 4, 3, 5, 6, 6, 7, 2, 7, 9, 1, 0] # 16 random items
c = 0
c = ml.mode(myArray)
print(c)