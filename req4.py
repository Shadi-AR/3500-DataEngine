# Jarl Ramos
# Requirement 4
#!/usr/bin/env python

read_info = { }

month_delay_list = []
day_delays = []
airline_delay_log = {}

airport_lists = {}

def find_month_delays(read_info, month_delays):
    if read_info[0] == "1":
        num = int(read_info[2])
        month_delays[0] += num
    elif read_info[0] == "2":
        num = int(read_info[2])
        month_delays[1] += num
    elif read_info[0] == "3":
        num = int(read_info[2])
        month_delays[2] += num
    elif read_info[0] == "4":
        num = int(read_info[2])
        month_delays[3] += num
    elif read_info[0] == "5":
        num = int(read_info[2])
        month_delays[4] += num
    elif read_info[0] == "6":
        num = int(read_info[2])
        month_delays[5] += num
    elif read_info[0] == "7":
        num = int(read_info[2])
        month_delays[6] += num
    elif read_info[0] == "8":
        num = int(read_info[2])
        month_delays[7] += num
    elif read_info[0] == "9":
        num = int(read_info[2])
        month_delays[8] += num
    elif read_info[0] == "10":
        num = int(read_info[2])
        month_delays[9] += num
    elif read_info[0] == "11":
        num = int(read_info[2])
        month_delays[10] += num
    elif read_info[0] == "12":
        num = int(read_info[2])
        month_delays[11] += num
def find_day_delays(read_info, day_delays):
    if read_info[1] == "1":
        num = int(read_info[2])
        day_delays[0] += num
    elif read_info[1] == "2":
        num = int(read_info[2])
        day_delays[1] += num
    elif read_info[1] == "3":
        num = int(read_info[2])
        day_delays[2] += num
    elif read_info[1] == "4":
        num = int(read_info[2])
        day_delays[3] += num
    elif read_info[1] == "5":
        num = int(read_info[2])
        day_delays[4] += num
    elif read_info[1] == "6":
        num = int(read_info[2])
        day_delays[5] += num
    elif read_info[1] == "7":
        num = int(read_info[2])
        day_delays[6] += num
def find_most_delayed_airline(read_info, month_index, d_log):
    if read_info[0] == month_index:
        if read_info[8] in d_log:
            d_log[read_info[8]] += 1
        else:
            dict_buf = {read_info[8] : 1}
            d_log.update(dict_buf)
    for i in d_log:
        hi_delays = i.key
        if (i.key > hi_delays):
            hi_delays = i.key
    return hi_delays

def find_avg_plane_age(carrier_name):
    avg_age = 0
    plane_count = 0
    if read_info[8] == carrier_name and read_info[2] == 1:
        avg_age += int(read_info[16])
        plane_count += 1

    return avg_age / plane_count

def snow_delay(read_info):
    count_of_planes = 0

    if int(read_info[22]) >= 15 and read_info[2] == 1:
        count_of_planes += 1
    
    return count_of_planes

def collect_airports(read_info, alist):
    if read_info[17] in alist:
        alist[read_info[17]] += 1
    else:
        dict_buf = {read_info[17] : 1}
        alist.update(dict_buf)

def top_5_airports(alist):
    new_dict = { }
    most_delays = 0
    most_delayed_airport = '0'
    for h in range(5):
        for i in alist:
            if alist[i] > most_delays:
                most_delays = alist[i]
                most_delayed_airport = alist
        dict_buf = {most_delayed_airport : most_delays}
        new_dict.update(dict_buf)
        del alist[most_delayed_airport]
    return new_dict
        
