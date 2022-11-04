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

c = Count.count(myArray)
print(c)