def aficher(T,N,d,f) :
     if d < f :
         print(T[d])
         aficher(T,N,d+1,f)
          
 

def read_file(file) :
    line = file.readline() 
    if line != '' :
        print(line)
        read_file(file)
            
 
 
 
 
 
 
 
T = [1,2,3,4,5]
#tout_sommes_posible(T,len(T))
            
def toutes_les_sommes_possibles(tableau):
    sommes = []
    n = len(tableau)
    for i in range(1, 2**n):
        s = 0 
        for j in range(n) :
            if (i >> j) & 1 : 
                s += tableau[j]      
        sommes.append(s) 
    return sommes


# Exemple d'utilisation
tableau = [1, 2,3,4]
resultat = toutes_les_sommes_possibles(tableau)
print("Toutes les sommes possibles dans le tableau sont :", resultat,len(resultat))
