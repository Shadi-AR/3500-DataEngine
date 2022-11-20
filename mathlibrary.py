# This is the library that will hold our statistical analysis functionalities

# TODO : Complete the classes/functions. 
#   If a method is comlpeted, make a comment saying it is complete


#Alonso ##########

# place holder sorting
def orderList(gen_array):
    # TODO : implement sorting algo
    new_list = []
    for item in gen_array:
        new_list.append(item)
    new_list = sorted(new_list)
    return new_list

#generator to prevent loading all of the object at once
def gen_objects(object):
    for item in object:
        yield item

def isOfNumber(numbers):
    if isinstance(numbers, (float, int)):
        array = [numbers]
        numbers = array

    for item in numbers:
        if not isinstance(item, (float, int)):
            raise Exception("A NaN was found. Please use numbers.")

def count(gen_list):
    # enumerate(x) returns an index starting at 1 and the item in the list
    for count, item in enumerate(gen_list, start=1):
        pass
    return count #all I need is the final count

# Return a list with only unique values. 
# Takes advantage of set's hashing functionality
def unique(gen_array):
    
    # Create an empty set
    unique_array = set()
    #get iterable array generator object
    for item in (gen_array):
        unique_array.add(item) # add item to set
    return list(unique_array) # return set as a list

def median(array):
    isOfNumber(array)
    length = len(array)
    isEven = not length %2
    middle_index = length //2 # floor division
    median = 0

    if (isEven):
        median = (array[middle_index] + array[middle_index-1]) /2
        return median
    else: #odd
        median = array[middle_index]
        return median

def mode(gen_array):

    # empty dictionary
    dictionary = {} # {value : occurence}
    for key_int in gen_array:
        isOfNumber(key_int) # check if dictionary keys are numbers
        if dictionary.get(key_int) is None: # if key does not exist yet
            # create dictionary key and set to one occurence
            dictionary[key_int] = 1 
        else:
            # increase the occurence if key exists
            dictionary[key_int] = dictionary.get(key_int)+1 
    dict_values = list(dictionary.values())
    dict_keys = list(dictionary.keys())
    max_keys = [key for key, value in dictionary.items() if value == max(dictionary.values())]
    most_occurence = maximum(dict_values)
    mode_array = []
    thing = dictionary.item(5)
    
    # code for one mode (the first one that appears)
    #occurences = maximum(dict_list)
    #modes = list(dictionary.keys())[dict_list.index(occurences)]
    return thing

def minimum(gen_array):
    number = next(gen_array)
    isOfNumber(number) # check if the first array item is a number
    min_val = number
    for number in gen_array:
        isOfNumber(number)
        if min_val > number:
            min_val = number
    return min_val

def maximum(gen_array):
    number = next(gen_array)
    isOfNumber(number) # check if the first array item is a number
    max_val = number
    for number in gen_array:
        isOfNumber(number)
        if max_val < number:
            max_val = number
    return max_val


#----------------- 

#Jarl ###########

# finds the arithmetic mean of a list of numerical values
def mean(data_list):
    mean_sum = 0
    mean_num = len(data_list)
    for i in data_list:
        mean_sum += i
    return mean_sum / mean_num
 
# finds the variance of a list of values
def variance(data_list, mean):
    var_sum = 0
    for i in data_list:
        var_sum += (i - mean) ** 2
    return var_sum / (len(data_list) - 1)

# finds the variance of a list of values by taking in the variance
# returned by the above function
def std_dev(var):
    return var ** (1 / 2)

# finds the 20th percentile of a list
def per_20(data_list):
    return data_list[len(data_list) // 5 - 1]

# finds the 40th percentile of a list
def per_40(data_list):
    return data_list[len(data_list) // 2.5 - 1]

# finds the 50th percentile of a list
def per_50(data_list):
    return data_list[len(data_list) // 2 - 1]

# finds the 60th percentile of a list
def per_60(data_list):
    return data_list[len(data_list) // 1.66667 - 1]

# finds the 80th percentile of a list
def per_80(data_list):
    return data_list[len(data_list) // 1.25 - 1]

#-------------------
