#input = 20 숫자가 크면 느림


#def fibo_recursion(n):
    # 구현해보세요!
    #if n == 1 or n == 2: #fibo_recursion(3) = fibo_recursion(2) + fibo_recursion(1)
    #   return 1
    #return fibo_recursion(n - 1) + fibo_recursion(n - 2)


#print(fibo_recursion(input))  # 6765

input = 50 #숫자가 커도 빠름

# memo 라는 변수에 Fibo(1)과 Fibo(2) 값을 저장해놨습니다!
memo = {
    1: 1,
    2: 1
}

def fibo_dynamic_programming(n, fibo_memo):
    # 구현해보세요!
    if n in fibo_memo:
        return fibo_memo[n]

    nth_fibo = fibo_dynamic_programming(n-1,fibo_memo) + fibo_dynamic_programming(n-2, fibo_memo)
    fibo_memo[n] = nth_fibo
    return nth_fibo

print(fibo_dynamic_programming(input, memo))
