
def binarySearch(l:list, val):
    a = 0
    b = len(l) - 1
    while a <= b:
        k = int((a+b)/2)
        if l[k] == val: return True
        elif l[k] > val: b = k - 1
        else: a = k+1
    return False
