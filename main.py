import csv


def calculate(csv_location):
    student_scores = {}
    average = {}
    with open(csv_location, "r") as csv_read:
        header = csv_read.readline().strip().split(",")
        name_index = header.index("FullName")
        scores_index = header.index("Score")

        for row in csv_read:
            values = row.strip().split(",")


            student_name = values[name_index]
            student_score = int(values[scores_index])
            if student_name in student_scores:
                student_scores[student_name].append(student_score)
            else:
                student_scores[student_name] = [student_score]
    for student, score in student_scores.items():
        average[student] = sum(score) / len(score)
    return average



print(calculate('new_csv.csv'))

