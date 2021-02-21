from os import listdir, walk
from os.path import isfile, join
import json


def convert_date(input_date, with_slash=True):
    y, m, d = input_date.split('/')
    if with_slash:
        return str(int(y)+1911) + '/' + m + '/' + d
    else:
        return str(int(y)+1911) + m + d


def all_history_data():
    file_list = []
    history_data = []
    target_folder = 'history'
    for path, subdirs, files in walk(target_folder):
        for name in files:
            if name.endswith('.json'):
                file_list.append(join(path, name))
    file_list.sort()
    for f in file_list:
        with open(f, 'r') as jf:
            history_data += json.loads(jf.read())['data']
    return history_data


def RSV(nine_day_data):
    ninth_day_close_value = float(nine_day_data[-1][4].replace(",", ""))
    nine_day_min_low_value = min(
        [float(m[3].replace(",", "")) for m in nine_day_data])
    nine_day_max_high_value = max(
        [float(m[2].replace(",", "")) for m in nine_day_data])
    return (ninth_day_close_value - nine_day_min_low_value) / (nine_day_max_high_value - nine_day_min_low_value)


if __name__ == '__main__':
    all_history_data = all_history_data()
    print("Total :" + str(len(all_history_data)))
    k_indicator_dict = {}
    for idx in range(len(all_history_data)):
        if idx < 9:
            k_indicator_dict[convert_date(all_history_data[idx][0])] = 0.5
            continue
        rsv = RSV(all_history_data[idx-8:idx+1])
        k_indicator_dict[convert_date(all_history_data[idx][0])] = rsv / 3 + \
            k_indicator_dict[convert_date(all_history_data[idx-1][0])] * 2 / 3
    # print(k_indicator_dict)
    filename = f"{convert_date(all_history_data[0][0], False)}-{convert_date(all_history_data[-1][0], False)}-k.json"
    with open('k-indicator/' + filename, 'w') as f:
        json.dump(k_indicator_dict, f)
