from re import search
import csv
import json

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

def util_map(act, format):
    act.lower()
    format.lower()
    for row in json_db:
        if(act.split(" ")[0] in row["activity_name"].split(" ") and format in row["activity_name"].split(" ")):
            return (row["activity_name"], row["id"], act)
        

def map_id_to_wk(str):
    obj_list = []
    for entry in str:
       print(util_map(entry, format="GYM"))

                
    pass # return [{'glute gridge': 309}]

file = open('plan.csv', 'r')
db = open('workouts.json', 'r', encoding="utf-8")
json_db = json.load(db)
reader = csv.reader(file)

workouts = [] # raw list of workout line by line
cell_holder = [] # separated by columns but not celled as individual workouts days 
cell_length = 0 # define length for columns
separated_cells = [] # separated by a column [[A,A,A,A], [B,B,B,B]] etc
json_objs = [] # list of programs as jsons


for row in enumerate(reader):
    workouts.append(row[1])
    cell_length = len(row)

for index in range(0,len(row)+2):
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
    obj = {
        "date": {
            "month": date_extractor(item[0])[0][0],
            "week": date_extractor(item[0])[0][1],
            "day": date_extractor(item[0])[0][2],
            "workout": date_extractor(item[0])[1]
        },
        "rounds": round_extractor(item[1]),
        "workouts": item[2:]
    }
    json_objs.append(obj)

for wk in json_objs:
    print(wk)


file.close()