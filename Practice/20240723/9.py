import re

def solution(my_string):
    numbers = list(map(int, re.findall(r'-?\d+', my_string)))
    operators = re.findall(r'[+-]', my_string)
    
    answer = numbers[0]
    for i, op in enumerate(operators):
        if op == '+':
            answer += numbers[i + 1]
        elif op == '-':
            answer -= numbers[i + 1]

        i += 1

    return answer

print(solution("3 + 4 + 1 - 1 + 11 - 40 + 20 + 77"))