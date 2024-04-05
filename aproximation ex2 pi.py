 
 
def racine_carré(A,eps) :
    
     X0 = (1+A)/2
     X1 = 0.5 * (X0 + A/X0)
     
     while X1 - X0 > eps :
         X0 = X1
         X1 = 0.5 * (X0 + A/X0)
         
     return X1
print(racine_carré(2,10**-4))