def comb(n,p):
    return fact(n) / (fact(n-p) * fact(p))
    
def fact (x) :
    if x == 0 :
        return 1
    else :
        return fact(x-1) * x

def PI() :
    eps = 0.0004
    T1 = 1
    T2 = T1 + (2*(1/(3*2)))
    n = 1
    while abs(T2 - T1) > eps :
        n = n + 1
        T1 = T2
        T2 = T1 + (1/(comb(2*n,n)*(2*n + 1))) * 2**n 
    return T2
print(PI() * 2)


