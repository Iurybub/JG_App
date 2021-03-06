from ast import keyword
import json
import difflib

db = open('workouts.json', 'r', encoding="utf-8")
json_db = json.load(db)


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
    for entry in str:
        best_match = difflib.get_close_matches(format_entry(
            entry, format="GYM"), hold_list, n=1, cutoff=0.6)
        for row in json_db:
            if (row['activity_name'] == best_match[0]):
                best_matches.append(row)

    for n in best_matches:
        print(n)
        print('\n')


map_ids(['Glute bridge with a band 20 reps', 'Goblet squat 20 reps', 'Fire hydrant 12 reps per side',
        'Split squat 12 reps per leg', 'Sumo squat 20 reps'], format='GYM')

db.close()


# ['Glute bridge with a band 20 reps', 'Goblet squat 20 reps', 'Fire hydrant 12 reps per side', 'Split squat 12 reps per leg', 'Sumo squat 20 reps']
# ('Glute bridge to chest press GYM', '211', 'Glute bridge with a band 20 reps')
# ('Goblet squat with a band GYM', '289', 'Goblet squat 20 reps')
# ('Fire hydrant GYM', '262', 'Fire hydrant 12 reps per side')
# ('Split Squat GYM', '263', 'Split squat 12 reps per leg')
