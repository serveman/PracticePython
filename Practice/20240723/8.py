import re

def solution(my_string):
    answer = 0

    numbers = my_string[:].replace('-', '+').replace(' ', '').split('+')
    operators = re.split('[^\+\-]+', my_string[:].replace(' ', ''))
    for num in numbers:
        print(num)
    
    i = 0
    answer = int(numbers[0])
    for op in operators:
        print(op)
        if op == '+': answer += int(numbers[i])
        elif op == '-': answer -= int(numbers[i])

        i += 1

    print(answer)

solution("3 + 4")