from ast import keyword
import json
import difflib

db = open('workouts.json', 'r', encoding="utf-8")
json_db = json.load(db)

def extractKeys(entry, format):
    entry = entry.lower()
    format = format.lower()
    split_entry = [char for char in entry if char != " "]
    joined = []
    for char in split_entry:
        if(char.isdigit()):
            break
        joined.append(char)
    
    return "".join(joined) + format.lower()

    # return row.name && row.id 

def map_ids(str, format):
    obj_lsit = []
    row_list = []

    for row in json_db:
        row_entry = [char for char in row['activity_name'] if char != ' ']
        clost_list = []
        for char in row_entry:
            if(char == '(' or char == ")"):
                continue
            clost_list.append(char)
        row_list.append(''.join(clost_list))

    for entry in str:
        key = extractKeys(entry, format)
        print(difflib.get_close_matches(key, row_list, 1))

        

    # return obj_list || obj_list.append[{"entry": [entry.name entry['id'], reps]}]


map_ids(['Glute bridge with a band 20 reps', 'Goblet squat 20 reps', 'Fire hydrant 12 reps per side', 'Split squat 12 reps per leg', 'Sumo squat 20 reps'], format='GYM')

db.close()


# ['Glute bridge with a band 20 reps', 'Goblet squat 20 reps', 'Fire hydrant 12 reps per side', 'Split squat 12 reps per leg', 'Sumo squat 20 reps']
# ('Glute bridge to chest press GYM', '211', 'Glute bridge with a band 20 reps')
# ('Goblet squat with a band GYM', '289', 'Goblet squat 20 reps')
# ('Fire hydrant GYM', '262', 'Fire hydrant 12 reps per side')
# ('Split Squat GYM', '263', 'Split squat 12 reps per leg')

