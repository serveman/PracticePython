def solution(my_string):
    return sum(int(number) for number in my_string.replace(' - ', ' + -').split(' + '))

print(solution('3 + 4 + 5 - 2 - 10 + 45 - 22 + 1 - 6'))