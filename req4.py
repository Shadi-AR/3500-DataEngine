# Jarl Ramos
# Requirement 4
#!/usr/bin/env python

read_info = { }

month_delays = []
day_delays = []
airline_delay_log = {}

def find_month_delays(read_info):
    for row in read_info:
        if row[0] == "1":
            num = int(row[2])
            month_delays[0] = num
        elif row[0] == "2":
            num = int(row[2])
            month_delays[1] = num
        elif row[0] == "3":
            num = int(row[2])
            month_delays[2] = num
        elif row[0] == "4":
            num = int(row[2])
            month_delays[3] = num
        elif row[0] == "5":
            num = int(row[2])
            month_delays[4] = num
        elif row[0] == "6":
            num = int(row[2])
            month_delays[5] = num
        elif row[0] == "7":
            num = int(row[2])
            month_delays[6] = num
        elif row[0] == "8":
            num = int(row[2])
            month_delays[7] = num
        elif row[0] == "9":
            num = int(row[2])
            month_delays[8] = num
        elif row[0] == "10":
            num = int(row[2])
            month_delays[9] = num
        elif row[0] == "11":
            num = int(row[2])
            month_delays[10] = num
        elif row[0] == "12":
            num = int(row[2])
            month_delays[11] = num
def find_day_delays(read_info):
    for row in read_info:
        if row[1] == "1":
            num = int(row[2])
            day_delays[0] = num
        elif row[1] == "2":
            num = int(row[2])
            day_delays[2] = num
        elif row[1] == "3":
            num = int(row[2])
            day_delays[3] = num
        elif row[1] == "4":
            num = int(row[2])
            month_delays[3] = num
        elif row[1] == "5":
            num = int(row[2])
            month_delays[4] = num
        elif row[1] == "6":
            num = int(row[2])
            month_delays[5] = num
        elif row[1] == "7":
            num = int(row[2])
            month_delays[6] = num
def find_most_delayed_airline(read_info, month_index, d_log):
    for row in read_info:
        if row[0] == month_index:
            if row[8] in d_log:
                d_log[row[8]] += 1
            else:
                dict_buf = {row[8] : 1}
                d_log.update(dict_buf)
    for i in d_log:
        hi_delays = i.key
        if (i.key > hi_delays):
            hi_delays = i.key
    return hi_delays

def find_avg_plane_age(carrier_name):
    avg_age = 0
    plane_count = 0

    for row in read_info:
        if row[8] == carrier_name and row[2] == 1:
            avg_age += int(row[16])
            plane_count += 1

    return avg_age / plane_count

def snow_delay(inches):
    count_of_planes = 0

    for row in read_info:
        if int(row[22]) >= 15 and row[2] == 1:
            count_of_planes += 1
    
    return count_of_planes

