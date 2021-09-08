from collections import deque  # queue 사용할때 대신 이거 사용하기

# 2019년 상반기 LINE 인턴 채용 코딩 테스트
# 코니는 처음 위치에서 C, C+1, C+3, C+6 ... 만큼 움직인다
# 브라운은 현재 위치 B에서 B-1, B+1, B*2 중 하나만 움직일 수 있다
# 브라운이 코니를 잡거나 코니가 멀리 달아나버리면 끝난다
# 코니와 브라운의 위치는 0이상 200000 이하를 만족한다
# 브라운이 코니를 잡는데 걸리는 최소 시간을 구하시오

# 코니의 위치 변화 -> 증가 속도가 1초마다 1씩 증가
# => 1 2 3 4 ... 순으로 증가
# => 코니의 위치: 3, 4, 6, 9 ... / 시간에 따라 더하기 : 반복문

# 브라운의 위치 변화 -> 선택 가능
# 모든 경우의 수 사용 -> BFS

# 잡았다 = 똑같은 시간에 똑같은 위치에 존재한다
# 규칙적 -> 배열 / 자유자재 -> dict
# 각 시간마다 브라운이 갈 수 있는 위치 저장 -> 배열 안에 dict

c = 11
b = 2


def catch_me(cony_loc, brown_loc):
    time = 0
    queue = deque()
    queue.append((brown_loc, 0))  # 위치와 시간 동시에 담아두기
    visited = [{} for _ in range(200001)]  # 성공 조건 저장 {}배열을 200000개 생성
    # visited[위치][시간]
    while cony_loc <= 200000:
        cony_loc += time  # 시간만큼 더해짐 +1, +2, +3 ...
        if time in visited[cony_loc]:
            return time
        
        for i in range(0, len(queue)):
            current_position, current_time = queue.popleft()

            new_time = current_time + 1
            new_position = current_position - 1
            if 0 <= new_position <= 200000:
                queue.append((new_position, new_time))

            new_position = current_position + 1
            if 0 <= new_position <= 200000:
                queue.append((new_position, new_time))

            new_position = current_position * 1
            if 0 <= new_position <= 200000:
                queue.append((new_position, new_time))

    return -1


print(catch_me(c, b))  # 5가 나와야 합니다!
