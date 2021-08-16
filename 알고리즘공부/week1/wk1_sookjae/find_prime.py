input = 20


def find_prime_list_under_number(number):
    prime_list = []
    for n in range(2, number +1): #2부터 number까지
        #for i in range(2, n):  -> 2부터 n-1까지
        for i in prime_list: #2부터 n-1까지중 소수
            if n % i == 0 and i * i <= n: #and~ 개선 추가
                break
        else:
            prime_list.append(n)

    return prime_list


result = find_prime_list_under_number(input)
print(result)
