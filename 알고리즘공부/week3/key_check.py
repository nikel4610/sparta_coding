all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]

def get_absent_student(all_array, present_array):
    student_dict = {}
    for key in all_array:
        student_dict[key] = True #all_students 키 등록

    for key in present_array:
        del student_dict[key] #present_students 키 제거

    for key in student_dict.keys():
        return key #제거하고 남은 key반환

print(get_absent_student(all_students, present_students))
