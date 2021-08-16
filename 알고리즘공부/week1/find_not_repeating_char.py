input = "abacabade"


def find_not_repeating_character(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():  # char -> 알파벳이 아니라면
            continue
        arr_index = ord(char) - ord("a")  # 0번째가 a부터 쭉쭉
        alphabet_occurrence_array[arr_index] += 1  # 알파벳 빈도수 별로 +1

    not_repeating_character_array = []
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]
        if alphabet_occurrence == 1:
            not_repeating_character_array.append(chr(index + ord("a")))

    for char in string:
        if char in not_repeating_character_array:
            return char
    



result = find_not_repeating_character(input)
print(result)
