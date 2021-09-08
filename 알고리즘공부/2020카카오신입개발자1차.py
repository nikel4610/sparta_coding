input = "abcabcabcabcdededededede"

# 2020카카오 신입 개발자 블라인드 채용 1차 코딩테스트
# 1개 이상 단위의 문자열로 잘라 압축하여 표현한 문자열 중 가장 짧은 것의 길이를 return

def string_compression(string):
    n = len(string)
    compresseion_length_array = []
    for split_size in range(1, n//2 + 1):
        #splited = []
        #for i in range(0, n, split_size):
        #    splited.append(string[i:i + split_size])]
        splited = [string[i:i + split_size] for i in range(0, n, split_size)]
        compressed = ""
        count = 1

        for j in range(1, len(splited)):
            prev, cur = splited[j - 1], splited[j]
            if prev == cur:
                count += 1
            else:
                if count > 1:
                    compressed += str(count) + prev
                else:
                    compressed += prev
                count = 1

        if count > 1:
            compressed += str(count) + splited[-1]
        else:
            compressed += splited[-1]
        compresseion_length_array.append(len(compressed))

    return min(compresseion_length_array)

print(string_compression(input))
