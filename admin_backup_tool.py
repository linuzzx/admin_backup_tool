import json
import os

grade_weights = {
    "SA": 2,
    "M": 1
}


def import_data(filepath):
    if not os.path.exists('data.json'):
        print("data.json not found, creating empty...")
        with open('data.json', 'w') as f:
            json.dump({}, f)
            print("data.json created.")

    with open(filepath, "r") as f:
        return json.load(f)


def export_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)


def get_student(data, name):
    return data[name]


def add_student(data, name):
    data[name] = []


def remove_student(data, name):
    data.pop(name)


def add_grade(data, name, grade_type, grade):
    data[name].append([grade_type, grade])


def remove_grade(data, name, grade_type, grade):
    data[name].remove([grade_type, grade])


def get_averages(data):
    averages = []

    for student in data:
        grade_sum = 0
        grade_n = 0

        for grade in data[student]:
            if grade[0] in grade_weights:
                grade_sum += grade[1]*grade_weights[grade[0]]
                grade_n += grade_weights[grade[0]]
            else:
                grade_sum += grade[1]
                grade_n += 1

        if grade_n != 0:
            average = grade_sum/grade_n
            averages.append([student, average])

    averages = sorted(averages, key=lambda average: average[1])

    return averages