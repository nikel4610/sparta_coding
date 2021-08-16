input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alphabet_array = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
                      'o','p','q','r','s','t','u','v','w','x','y','z']
    #1. alphabet_array에서 하나하나 꺼내서 비교
    #max_occurance = 0
    #max_alphabet = alphabet_array[0]
    #for alphabet in alphabet_array:
    #    occurance = 0
    #    for char in string:
    #        if char == alphabet: #알파벳 동일하면
    #            occurance += 1 #빈도수 +1
    #    if occurance > max_occurance: #크면
    #        max_occurance = occurance #업데이트
    #        max_alphabet = alphabet

    #return max_alphabet

    #2.
    alphabet_occurrence_array = [0] * 26
    for char in string:

        if not char.isalpha():  # char -> 알파벳이 아니라면
            continue
        arr_index = ord(char) - ord("a")  # 0번째가 a부터 쭉쭉
        alphabet_occurrence_array[arr_index] += 1  # 알파벳 빈도수 별로 +1

    max_occurance = 0
    max_alphabet_index = 0
    for index in range(len(alphabet_occurrence_array)):
        #index 0 (인덱스 0번째가 a) -> occurrance 3(3번나와서 3임)
        alphabet_occurrence = alphabet_occurrence_array[index]

        if alphabet_occurrence > max_occurance:
            max_alphabet_index = index
            max_occurance = alphabet_occurrence
        # 0 -> 0+ord(a) = 97 -> chr(97) -> a // 인덱스를 문자로 이런과정으로 바꿈
        return chr(max_alphabet_index + ord("a"))
    
result = find_max_occurred_alphabet(input)
print(result)
