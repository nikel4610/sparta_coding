input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):

    #숫자 비교하는 형식
    #for num in array:
    #   for compare_num in array:
    #        if num < compare_num:
    #            break
    #    else:
    #        return num
    #배열에 넣고 비교하기
    max_num = array[0]
    for num in array:
        if num > max_num:
            max_num = num
    return max_num


result = find_max_num(input)

print(result)
