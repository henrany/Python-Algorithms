
def bubbleSort(l: list ):
    temp = 0
    for i in range(len(l)):
        for j in range(len(l) - 1):
            if l[j] > l[j+1]:
                temp = l[j]
                l[j] = l[j+1]
                l[j+1] = temp
    return l