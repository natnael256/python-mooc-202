import math



# def grede_det(exam_and_exercise_points):
#     grade = 0
#     if exam_and_exercise_points <= 14:
#         grade = 0
#     elif exam_and_exercise_points >= 14 and exam_and_exercise_points <= 17:
#         grade = 1
#     elif exam_and_exercise_points >= 17 and exam_and_exercise_points <= 20:
#         grade = 2
#     elif exam_and_exercise_points >= 20 and exam_and_exercise_points <= 23:
#         grade = 3
#     elif exam_and_exercise_points >= 24 and exam_and_exercise_points <= 27:
#         grade = 4
#     elif exam_and_exercise_points >= 28 and exam_and_exercise_points <= 30:
#         grade = 5
#     return grade


def convert_to_exam_and_exercise_point (exam_list ,exer_list ):
    exam_and_exer_list = []
    index = 0
    for i in exer_list:

        i = (int(i) / 100 ) * 10
        i = math.floor(i)
        exam_and_exercise_points = int(i) + int (exam_list[index])
        exam_and_exer_list.append(exam_and_exercise_points)
        index += 1

    return exam_and_exercise_points


exam_point_list = []
exercises_point_list = []


def main():
    while True: 

        input_int = input("Exam points and exercises completed: ")
        if input_int != "": 
            exam_point , exercises_point = input_int.split(maxsplit=1)
            exam_point_list.append(exam_point)
            exercises_point_list.append(exercises_point)
        else: 
            break

    
    print (f"input list {exam_point_list}")
    print (f"input list {exercises_point_list}")

    print (convert_to_exam_and_exercise_point(exam_point_list,exercises_point_list))

if __name__ == "__main__":
    main()


