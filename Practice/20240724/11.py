def solution(my_string):
    return eval(my_string)  # 'my_string의 내용을 코드처럼 그대로 사용하는 점'이 보안문제때문에 실제 Web 에서는 권하지 않는 방식임

print(solution('3 + 2 + 1 - 6 + 8'))
