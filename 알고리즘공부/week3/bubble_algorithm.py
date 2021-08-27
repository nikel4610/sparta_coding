input = [4, 6, 2, 9, 1]

def bubble_sort(array):
    # 이 부분을 채워보세요!
    n = len(array)
    for i in range(n - 1):
        for j in range(n - i - 1): #버블정렬 틀
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1],array[j] #순서 바꾸기

    return


bubble_sort(input)
print(input)  
