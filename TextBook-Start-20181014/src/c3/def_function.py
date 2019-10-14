

def mul(a,b):
    '''
    掛け算を行う関数
    e.g. mul(1,2) = 1 * 2  = 2
    '''
    return a*b

print(mul(100,100))
print(mul(b=100,a=0.5))
# help(mul)

test_lambda = lambda a,b : a*b / 2

print(test_lambda(10,20))
