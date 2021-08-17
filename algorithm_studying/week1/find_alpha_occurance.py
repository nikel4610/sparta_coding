def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha(): #char -> 알파벳이 아니라면
            continue
        arr_index = ord(char) - ord("a") #0번째가 a부터 쭉쭉
        alphabet_occurrence_array[arr_index] += 1 #알파벳 빈도수 별로 +1

    return alphabet_occurrence_array


print(find_alphabet_occurrence_array("hello my name is sparta"))
