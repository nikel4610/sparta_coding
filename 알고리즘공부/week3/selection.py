input = [4, 6, 2, 9, 1]


def selection_sort(array):
    # 이 부분을 채워보세요!
    n = len(array)
    for i in range (1,n):
        for j in range(i):
            if array[i-j-1] > array[i-j]:
                array[i-j-1], array[i-j] = array[i-j], array[i-j-1]
            else:
                break #시간복잡도 줄이기

    return


selection_sort(input)
print(input)
