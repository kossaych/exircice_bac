def TOTO (A,B) :
    if A == 1 :
        return  B
    else :
        if A % 2 == 1 :
            return B + TOTO(A//2,B*2)
        else :
            return TOTO(A//2,B*2)
        
import numpy as np

def remplir (N) :
    global M_B
    M_B = np.array([[5]*N]*N)
    for i in range(0,N) :
        for j in range(0,N) :
            
            if i == 0 or j == 0 :
                M_B[i][j] = 1
            elif j >= i :
                M_B[i][j] = pow(2,i)
            else :
                M_B[i][j] =  M_B[i-1][j] + M_B[i-1][j-1]
    return M_B

remplir(6)
print(M_B)

def Afficher () :
    T = [1,3,2,-1,-3,-2]
    f = open("Nombre.txt", "r")  
    N = f.readline() 
    nb = N
    while(N != "") :  
        s = 11 # nombre aléa  pour verifier   s>=10 
         
        if N[len(N)-1:] == '\n' :
           N = N[:len(N)-1] 
        while s >= 10 :
            s = 0 
            for i in range(len(N)-1,-1,-1) :
                 s = s + T[(len(N) -i -1) % 6] * int(N[i])
                
            if s >= 10 :
                N = str(s) 
                 
        if  s==0 or s == 7 :
            print(str(nb) +"est divisible par 7") 
        N = f.readline()
        nb = N
         
Afficher()
def somme(N1,N2,B) :
    ret = 0
    ch = ""
    for i in range(len(N1)-1,-1,-1) :
        
        s = eqvd(N2[i]) + eqvd (N1[i]) + ret
        if s > B :
            ret = 1
            ch = eqvh(s-B) + ch
        else :
            ch = eqvh(s) + ch
            ret = 0
    
    
    return ch
        

def eqvd(c) :
    if ord(c) >= ord('A') and ord(c) <= ord('F') :
        return ord(c)-55
    else : return int(c)
    
def eqvh(x) :
    if x >= 10 :
        return chr(x+55)
    else :
        return str(x)

print(somme('0FA','A1E',16))
