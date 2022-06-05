import json
import os
from datetime import datetime
from report_functions import *


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
start_time = datetime.now()

for idx in range(NUM_STUDENTS):
    # print(f'Loading student: {idx}')
    report_list.append(load_report_card('students', idx))

end_time = datetime.now()
time_taken = end_time - start_time

print(f'Time taken to fetch: {time_taken}')
print()

# calculate required data summary metrics
average_all_students = get_all_average(report_list)
hardest_subject = get_hardest_subject(report_list)
easiest_subject = get_easiest_subject(report_list)
best_grade = get_best_grade(report_list)
worst_grade = get_worst_grade(report_list)
best_student = get_best_student(report_list)
worst_student = get_worst_student(report_list)


# display data
print(f'Average Student Grade: {average_all_students}')
print(f'Hardest Subject: {hardest_subject}')
print(f'Easiest Subject: {easiest_subject}')
print(f'Best Performing Grade: {best_grade}')
print(f'Worst Performing Grade: {worst_grade}')
print(f'Best Student ID: {best_student}')
print(f'Worst Student ID: {worst_student}')
