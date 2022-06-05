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


def sort_grade(report_list):  # return [best_grade, worst_grade]
    grade_dict = {}
    grade_set = set()

    for student in report_list:
        grade_set.add(student['grade'])

    for grade in grade_set:
        sum_holder = 0
        count_holder = 0
        for student in report_list:
            if student['grade'] == grade:
                sum_holder += get_student_average(student) * 5
                count_holder += 1

        average_holder = sum_holder / count_holder
        # print(f'Grade: {grade}')
        # print(f'Count: {count_holder}')
        # print(f'Average: {average_holder}')
        grade_dict[str(grade)] = average_holder

    # print(grade_dict)

    best_grade = max(grade_dict, key=grade_dict.get)
    worst_grade = min(grade_dict, key=grade_dict.get)

    return [best_grade, worst_grade]


def sort_student(report_list):  # return [best_student, worst_student]
    student_dict = {
        student_id: get_student_average(report_list[student_id]) for student_id in range(1000)}

    best_student = max(student_dict, key=student_dict.get)
    worst_student = min(student_dict, key=student_dict.get)

    return [best_student, worst_student]
