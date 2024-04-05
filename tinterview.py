def the_first_non_repetible_caracter (string): 
    for index_main_let in range(len(string)) :
        index = 0
        while index < len(string)-1 and (string[index] !=  string[index_main_let] or index == index_main_let)  :
            index = index + 1
        if index == len(string)-1 and (string[index] !=  string[index_main_let] or index == index_main_let) :
            return  index_main_let
    return -1

     
print(the_first_non_repetible_caracter('abegfddgfsassj')) 