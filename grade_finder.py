import json
import os

NUM_STUDENTS = 1000
SUBJECTS = ["math", "science", "history", "english", "geography"]


def load_report_card(directory, student_number):
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(directory, f"{student_number}.json")
    path = os.path.join(base_path, file_path)

    try:
        with open(path, "r") as file:
            report_card = json.load(file)
    except FileNotFoundError:
        return {}

    return report_card


report_list = []  # loading student report cards individually
# start_time = datetime.now()

grade_set = set()
for idx in range(NUM_STUDENTS):
    # print(f'Loading student: {idx}')
    current_report = load_report_card('students', idx)
    report_list.append(current_report)
    grade_set.add(current_report['grade'])

print(grade_set)
