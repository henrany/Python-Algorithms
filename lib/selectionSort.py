
def selectionSort(l: list):
    temp = 0
    for i in range(len(l) - 1):
        min = i
        for j in range(min+1, len(l)):
            if l[j] < l[min]:
                temp = l[j]
                l[j] = l[min]
                l[min] = temp
    return l
