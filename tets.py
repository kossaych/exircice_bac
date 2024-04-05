from math import sqrt # racine carré 

""" j'ai utilisé des techniques comme <python list comprehension> ...
 pour réduire la quantité de code , mais on peut les remplacer avec des fonctions
 ou avec des des bloques de code facilement si nous voulons adhérer au programme officiel  """

 
# retourne toutes les combinaison posible de longeur k dans un tableau t
def combinations(t, k):
    
    if k == 1 : 
        list_combinations = [ [case] for case in t] 
        return list_combinations
    
    list_combinations =  []
    
    for i in range(0,len(t)-1) :
        debut = t[i] 
        reste = t[i+1:]
   
        next_combinations = combinations(reste, k-1)  
        
        for comb in next_combinations :
            comb.append(debut)
            
            
            
        list_combinations.extend(next_combinations)  # extend c'est pour fusionner deux liste
    
    return  list_combinations



# decomposition d'un nombre en sommes de nombre carré
# et ca fonctionne avec toute type de nombre naturel non seulement avec les  entier parfait
def decomp(n) :
    k = int(sqrt(n))  # k c'est le racine caré du  n
    tab = [i for i in range(1,k) ] # remplir un tableau   de 1  a k-1
 
    tab2 = [] # pour stocker les resultas finales
    # cette boucle sert a faire toutes combinaison de longeur 2 >>> k-1  
    for i in range(2,k) : 
        combs = combinations(tab,i) # toutes les combinaison de longeur  i
        # gérer  chaque combinaison
        for comb in combs :
            # verifier si  la somme des carré des nombres de la comainisan  = n  
            if sum([ x**2 for x in comb ]) == n :
                # formation de l'expresion
                tab2.append( '\n'+str(n) +' = '+'^2 + '.join([ str(y) for y in comb]) + '^2' )
 
            for j in range(4,k) :
                non_unique_combination = comb
                while sum([ r**2 for r in non_unique_combination ])  < n :
                    non_unique_combination.append(j)
                
                if sum([ r**2 for r in non_unique_combination ]) == n :
                    # formation de l'expresion
                    tab2.append( '\n\n'+str(n) +' = '+'^2 + '.join([ str(z) for z in non_unique_combination]) + '^2' )
            
   
    
    return tab2
  
# exemple 121  
#print(*decomp(121))
#print(*decomp(49))


 
#############################  exercice 2 ##################################


def decomp_monnaies(somme,*pièces) :
    # initialisation de données
    pièces_prep = list(set(pièces))
    
    
    pièces_prep.sort()
    
 
    pièces_prep = [*enumerate(pièces_prep)]
    
    
    pièces = list(pièces)
    for i  in range(len(pièces)) :
        for pre_pièce in pièces_prep :
            if pièces[i] == pre_pièce[1] :
                pièces[i] = pre_pièce
            
                
        
   
    
    # preparation de combinaison
    combinaisons_pièces = []
    for i in range(1,len(pièces)+1) :
        combinaisons_pièces.extend(combinations([*pièces],i))
   
     
    decompositions = [] 
    for comb in combinaisons_pièces : 
        if sum([term[1] for term in comb]) == somme   :
            decompositions.append(comb) 
    
 
    
    """min_length = len(decompositions[0])
 
    for comb in decompositions :
        if len(comb) < min_length   :
            
             min_length = len(comb)
 
    decompositions = [ decomp for decomp in decompositions if len(decomp) == min_length]
    """
    
    unique_decompositions = []
    for decomp in decompositions :
        if decomp not in unique_decompositions :
            unique_decompositions.append(decomp)
    
    decompositions = unique_decompositions
      
    if len(decompositions) == 0 :  decompositions.append('il ya aucune decomp')
  
     
    return  [ decomp  for decomp in decompositions  ]
        
    
#print(*decomp_monnaies(5000, 5000,2500,2500, 1000, 500, 200, 100, 50)) 
#print(* decomp_monnaies(500,200,100,100,100,100,50,50,50,50) ,sep = '\n')
 
 
 
for decomp in decomp_monnaies(500,200,100,100,100,100,50,50,50,50) :
    somme_indx = 0
    for pièce in decomp :
        somme_indx += pièce[0]
    long = len(decomp)
    print(decomp,somme_indx)
        
     