from collections import deque

balanced_parentheses_string = "()))((()"

# 모든 괄호를 뽑아 올바른 순서대로 괄호 문자열을 배치

# 올바른 괄호 문자열?
def is_correct_parentheses(string):
    stack = []
    for s in string:
        if s == '(':
            stack.append(s)
        elif stack:
            stack.pop()
    return len(stack) == 0

def seperate_u_to_v(string):
    queue = deque(string)
    left, right = 0, 0
    u, v = "", ""
    while queue:
        char = queue.popleft()  # 문자열 w를 두 균형잡힌 괄호 문자열 u, v로 분리
        u += char               # 단 u는 균형잡힌 괄호 문자열로 더이상 분리 x
        if char == '(':         # v는 빈 문자열이 될 수 있다
            left += 1           # ( ) 개수가 같아야한다
        else:
            right += 1
        if left == right:
            break

    v = ''.join(list(queue))  # 문자열 다 합쳐줌
    return u, v

def reverse_parentheses(string):
    reversed_string = ""
    for char in string:
        if char == '(':
            reversed_string += ')'
        else:
            reversed_string += '('
    return reversed_string

def change_to_correct_parentheses(string):
    if string == "":  # 입력이 빈 문자열인 경우 그대로 반환
        return ""
    u, v = seperate_u_to_v(string)

    # 문자열 u가 올바른 괄호 문자열 일때 문자열 v에 대해 처음부터 다시 수행
    # 수행한 결과 문자열을 u에 이어 붙이고 반환
    # def change_to.. 다시 수행
    if is_correct_parentheses(u):
        return u + change_to_correct_parentheses(v)

    # 문자열 u가 올바른 괄호 문자열이 아니라면
    # 빈 문자열에 첫번째 문자로 (를 붙인다
    # v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙인다
    # )를 다시 붙인다
    # u의 첫번째 문자와 마지막 문자를 제거하고 나머지 문자열의 괄호 방향을 뒤집어서 붙인다
    else:
        return "(" + change_to_correct_parentheses(v) + ")" + reverse_parentheses(u[1:-1])

def get_correct_parentheses(balanced_parentheses_string):
    if is_correct_parentheses(balanced_parentheses_string):
        return balanced_parentheses_string
    else:
        return change_to_correct_parentheses(balanced_parentheses_string)


print(get_correct_parentheses(balanced_parentheses_string))  # "()(())()"가 반환 되어야 합니다!
