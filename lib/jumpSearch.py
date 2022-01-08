from math import sqrt

def jumpsearch(l:list, val):
    gap = sqrt(len(l))
    left = 0
    while(l[int(min(gap, len(l))-1)]<val):
        left = gap
        gap = gap + sqrt(len(l))
        if(left>=len(l)):
            break
    while(l[int(left)]<val):
        left =left + 1
        if(left== min(gap, len(l))):
            break
    if(l[int(left)]==val): return True
    else: return False

print(jumpsearch([2,3,4,5,6,7],7))