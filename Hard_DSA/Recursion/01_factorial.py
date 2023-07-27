def fact(n):
    assert n>=0 and int(n)==n, 'Input is invalid'
    if n in [0,1]:
        return 1
    else:
        return n*(n-1)
    

print(fact(-1))