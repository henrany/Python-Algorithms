from math import sqrt
class Search:

    def linearSearch(l:list, val):
        for value in l:
            if val == value:
                return True
        return False

    def binarySearch(l:list, val):
        a = 0
        b = len(l) - 1
        while a <= b:
            k = int((a+b)/2)
            if l[k] == val: return True
            elif l[k] > val: b = k - 1
            else: a = k+1
        return False

    def jumpsearch(l:list, val):
        gap = sqrt(len(l))
        left = 0
        while(l[int(min(gap, len(l))-1)]<val):
            left = gap
            gap = gap + sqrt(len(l))
            if(left >= len(l)):
                break
        if int(left) < len(l):
            while(l[int(left)]< val):
                left =left + 1
                if(left== min(gap, len(l))):
                    break
            if(l[int(left)]==val): return True
            else: return False
        return False