numbers = [1, 1, 1, 1, 1]
target_number = 3

#numbers = [2, 3, 1]
#target_number = 0

result_count = 0

def get_all_ways_to_by_plus_or_minus(array, target, current_index, current_sum):
    if current_index == len(numbers):
        if current_sum == target:
            global result_count
            result_count += 1
        return

    get_all_ways_to_by_plus_or_minus(
        array, target, current_index + 1, current_sum + numbers[current_index]
    )
    get_all_ways_to_by_plus_or_minus(
        array, target, current_index + 1, current_sum - numbers[current_index]
    )

print(get_all_ways_to_by_plus_or_minus(numbers, target_number, 0, 0))  # 5를 반환해야 합니다!
print(result_count)
