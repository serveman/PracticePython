def sum_n_ints(*args):
    print(type(args))
    return sum(args)
sum_n_ints(1,2,3,4,5,6,7,8,9,10)

def sum_n_ints(**kwargs):
    print(kwargs)
    print(type(kwargs))
    return sum(kwargs.values())
sum_n_ints(a=1, b=2, c=3)