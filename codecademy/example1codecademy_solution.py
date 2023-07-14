#1. Outline of solution: 
    #1. Iterate through list (i)
    #2. Iterate one over (j)
    #3. Iterate one over (k)
    #4. Square and compare a**2 + b**2 = c**2
#2. explicit inputs and outputs
    #1. [3,4,5] = True
    #2. [4] = False
    #3. [12,1,7,9] = False
#3. #code and communicate


def p_t(lst):
    lst.sort() #this will assume list is in ascending order
    for a in range(len(lst)): #iterate thru list "[a]"
        for b in range(a+1,len(lst)): #iterate again but one over i to avoid duplicate variables "b"
            for c in range(b+1,len(lst)): 
                if lst[a]**2 + lst[b]**2 == lst[c]**2:  #if element at index a^2 plus element at index b^2 is equal to element at index b 
                    return True
    return False


lst = [4,3,5]
print(p_t(lst))


