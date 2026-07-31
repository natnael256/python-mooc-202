import math



def grede_det(e_e_list, exam_list):
    grade = 0
    grade_list = []

    for i ,exam in zip(e_e_list, exam_list):

        if int (exam)< 10:
            grade = 0  
        elif i < 15:
            grade = 0   
        elif i >= 14 and i <= 17:
            grade = 1
        elif i >= 17 and i <= 20:
            grade = 2
        elif i >= 20 and i <= 23:
            grade = 3
        elif i >= 24 and i <= 27:
            grade = 4
        elif i >= 28 and i <= 30:
            grade = 5

        grade_list.append(grade)
    return grade_list


def convert_to_exam_and_exercise_point (exam_list ,exer_list ):
    exam_and_exer_list = []
    index = 0
    for i in exer_list:

        i = (int(i) / 100 ) * 10
        i = math.floor(i)
       # print(f"thsi is i = {i} || this is exam_list[index] {exam_list[index]}")
      
        i = int(i) + int (exam_list[index])

        exam_and_exer_list.append(i)
      
        index += 1

    return exam_and_exer_list


exam_point_list = []
exercises_point_list = []

def grade_dist (grade_out_put_list):

    for i in range(5, -1, -1):

        count = grade_out_put_list.count(i)

        print(f"  {i}: {'*' * count}")

def pass_perc(grade_out_put_list):

     
    fail = len(grade_out_put_list)
    for i in grade_out_put_list:

        if i == 0:          
            fail -= 1

    return (fail / len(grade_out_put_list)) * 100
    
    

    




def main():
    while True: 

        input_int = input("Exam points and exercises completed: ")
        if input_int != "": 
            exam_point , exercises_point = input_int.split(maxsplit=1)
            exam_point_list.append(exam_point)
            exercises_point_list.append(exercises_point)
        else: 
            break

    
    # print (f"input list {exam_point_list}")
    # print (f"input list {exercises_point_list}")
    # print(f"from the conv func: { convert_to_exam_and_exercise_point(exam_point_list,exercises_point_list)}")
    exam_and_exer_point  = convert_to_exam_and_exercise_point(exam_point_list,exercises_point_list)
    grade_dist_out_put = grede_det(exam_and_exer_point, exam_point_list)
    #print(grede_det(exam_and_exer_point))
    # pass_perc(grade_dist_out_put)

    print("Statistics:")
    print(f"Points average: {sum(exam_and_exer_point) / len(exam_and_exer_point):.1f}")
    print(f"Pass percentage: {pass_perc(grade_dist_out_put):.1f}")
    print("Grade distribution:")
    grade_dist(grade_dist_out_put)
    

main()
    




