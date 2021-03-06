import csv
import json
import difflib


def column(matrix, i):
    return [row[i] for row in matrix]


def date_extractor(str):
    num_list = []
    params = str.split(" ")
    for char in params:
        if(char.isdigit()):
            num_list.append(char)
    return [num_list, params[-1]]


def round_extractor(str):
    num_list = []
    params = str.split(" ")
    for char in params:
        if(char.isdigit()):
            num_list.append(char)
    return num_list[-1]


def format_entry(str, format):
    form_str = []
    for char in str:
        if(char.isdigit()):
            break
        else:
            form_str.append(char)
    return ''.join(form_str)+format


def map_ids(str, format):
    hold_list = [row['activity_name'] for row in json_db]
    best_matches = []
    not_found = []
    for entry in str:
        best_match = difflib.get_close_matches(format_entry(
            entry, format), hold_list, n=1, cutoff=0.9)
        for row in json_db:
            if(len(best_match) > 0):
                if (row['activity_name'] == best_match[0]):
                    best_matches.append(row)
            if(len(best_match) == 0):
                not_found.append(entry)         
    return [best_matches, list(set(not_found))]


file = open('plan.csv', 'r')
db = open('workouts.json', 'r', encoding="utf-8")
json_db = json.load(db)
reader = csv.reader(file)

workouts = []  # raw list of workout line by line
cell_holder = []  # separated by columns but not celled as individual workouts days
cell_length = 0  # define length for columns
separated_cells = []  # separated by a column [[A,A,A,A], [B,B,B,B]] etc
json_objs = []  # list of programs as jsons


for row in enumerate(reader):
    workouts.append(row[1])
    cell_length = len(row)

for index in range(0, len(row)+2):
    cell_holder.append(column(workouts, index))

for array_item in cell_holder:
    cell = []
    for item in array_item:
        if(item != ""):
            cell.append(item)
        if(item == ""):
            separated_cells.append(cell)
            cell = []


for item in separated_cells:
    mapped_ids = map_ids(item[2:], format="GYM");
    obj = {
        "date": {
            "month": date_extractor(item[0])[0][0],
            "week": date_extractor(item[0])[0][1],
            "day": date_extractor(item[0])[0][2],
            "workout": date_extractor(item[0])[1]
        },
        "rounds": round_extractor(item[1]),
        "workouts": mapped_ids[0],
        "missing": mapped_ids[1],
    }
    json_objs.append(obj)

f = open("file.txt", 'w')

for wk in separated_cells:
    print(wk)

for wk in json_objs:
    f.write(str(wk))
    f.write('\n')
    f.write('\n')


f.close()
file.close()
