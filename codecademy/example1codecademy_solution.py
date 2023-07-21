#1. Outline of solution: 
    #1. Iterate through list (i)
    #2. Iterate one over (j)
    #3. Iterate one over (k)
    #4. Square and compate
#2. explicit inputs and outputs
    #1. [3,4,5] = True
    #2. [4] = False
    #3. [12,1,7,9] = False
#3. #code and communicate


def p_t(lst):
    for i in range(len(lst)): #iterate thru list "a"
        for j in range(i+1,len(lst)): #iterate again but one over i to avoid duplicate variables "b"
            for k in range(j+1,len(lst)): #"c"
                if lst[i]**2 + lst[j]**2 == lst[k]**2 #if element at index i^2 plus element at index j^2 is equal to element at index j 
                    return True
    return False


lst = [3,4,5]
print(p_t(lst))



