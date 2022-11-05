# This is the library that will hold our statistical analysis functionalities

# TODO : Complete the classes/functions. 
#   If a method is comlpeted, make a comment saying it is complete


#Alonso ##########
class Count:

    # get a count by calling myArray.count
    @staticmethod
    def count(x):
        # enumerate(x) returns an index starting at 1 and the item in the list
        for count, item in enumerate(x, start=1):
            pass
        return count #all I need is the final count


#----------------- 

#Jarl ###########
def mean(x):
    # TODO: Find mean of all the values of set

def variance(x):
    # TODO: Find the variance

def std_dev(x):
    # TODO: Find the std. deviation

def per_20(x):
    # TODO: Find the 20th percentile

def per_40(x):
    # TODO: Find the 40th percentile

def per_50(x):
    # TODO: Find the 50th percentile

def per_60(x):
    # TODO: Find the 60th percentile

def per_80(x):
    # TODO: Find the 80th percentile

#-------------------
c = Count.count(myArray)
print(c)