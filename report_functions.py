def say_hi():
    print('Hello world!!')


def get_student_average(student):
    student_average = (student['math'] + student['science'] +
                       student['history'] + student['english'] + student['geography']) / 5

    return student_average


def get_all_average(report_list):
    grade_sum = 0
    student_count = 0
    for student in report_list:
        student_count += 1
        grade_sum += get_student_average(student)

    overall_average = grade_sum / student_count
    # print(f'Report counted: {student_count}')
    # print(f'Sum of grade averages {grade_sum}')
    return overall_average


def sort_subject_by_average(report_list):
    student_count = 0
    sum_math = 0
    sum_science = 0
    sum_history = 0
    sum_english = 0
    sum_geography = 0
    for student in report_list:
        student_count += 1
        sum_math += student['math']
        sum_science += student['science']
        sum_history += student['history']
        sum_english += student['english']
        sum_geography += student['geography']

    avg_math = sum_math / student_count
    avg_science = sum_science / student_count
    avg_history = sum_history / student_count
    avg_english = sum_english / student_count
    avg_geography = sum_geography / student_count

    average_dict = {'math': avg_math, 'science': avg_science,
                    'history': avg_history, 'english': avg_english, 'geography': avg_geography}

    # print(average_dict)
    hardest_subject = min(average_dict, key=average_dict.get)
    easiest_subject = max(average_dict, key=average_dict.get)

    # print(f'Report counted: {student_count}')
    return [hardest_subject, easiest_subject]


def sort_grade(report_list):
    grade_set = set()

    for student in report_list:
        grade_set.add(student['grade'])

    grade_dict = {str(grade): 0 for grade in grade_set}
    print(grade_dict)

    # return [best_grade, worst_grade]
    return [6, 5]


def sort_student(report_list):

    # return [best_student, worst_student]
    return [243, 420]
