def solution(a, *args):
    a_list = []
    for arg in args:
        a_list.append(arg)

    print(a_list)
    result = a.join(a_list)
    return eval(result)

print(solution('-', 1, 2, 3, 4, 5))