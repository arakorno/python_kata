import os
script_dir = os.path.dirname(__file__)


def read_data(data):
    abs_file_path = os.path.join(script_dir, 'data\\'+data.file_name)
    f = open(abs_file_path, 'r')
    return f.read().splitlines()


def clean_up(lines):
    lines.pop(0)
    lines = [l.replace('*', '') for l in lines]
    lines = [lines.pop() if l == '' or '--' in l else l for l in lines]
    return lines


def min_delta(lines, data):
    day = None
    delta = None
    for line in lines:
        min = line.split()[data.r_idx]
        max = line.split()[data.l_idx]
        new_delta = float(max) - float(min)
        if delta == None or delta > new_delta:
           day = line.split()[data.res_idx]
           delta = new_delta
    return day


class WheatherData:
    file_name = 'weather.dat'
    res_idx = 0
    l_idx = 1
    r_idx = 2


class FootballData:
    file_name = 'football.dat'
    res_idx = 1
    l_idx = 6
    r_idx = 8


w_data = WheatherData()
f_data = FootballData()

print(min_delta(clean_up(read_data(w_data)), w_data))
print(min_delta(clean_up(read_data(f_data)), f_data))
