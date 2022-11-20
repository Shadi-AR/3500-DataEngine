# generator function to open the large file
def gen_open_file(fname):
    for line in open(fname, 'r'):
        line = line.strip() #remove newlines
        # this will yield a line when the caller requests the file object
        yield line

# this defeats the purpose of generators so dont use it too often
def gen_to_list(gen_obj):
    new_list = []
    for item in gen_obj:
        new_list.append(item)
    return new_list
# # # # # #

def get_columns(line):
    columns = []
    columns = line.split(',')
    return columns

# wrapper for len()
def get_num_columns(columns_in):
    numcol = len(columns_in)
    return numcol

#converts list into a dictionary for fast searching
def create_dict(fileformat):
    # dictionary format:
    # {columnName:columnIndex}
    dict_fileformat = {fileformat[i]:i for i in range(0, len(fileformat))}
    return dict_fileformat

def drop_col(file_format, columns, column_name):
    for name in column_name:
        col_number = file_format.get(name)
        del columns[col_number]
    return columns

