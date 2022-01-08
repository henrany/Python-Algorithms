
class Sorting:
    def bubbleSort(l: list ):
        temp = 0
        for i in range(len(l)):
            for j in range(len(l) - 1):
                if l[j] > l[j+1]:
                    temp = l[j]
                    l[j] = l[j+1]
                    l[j+1] = temp
        return l

    def insertionSort(l: list):  
        for i in range(1, len(l)):  
            value = l[i]  
            j = i - 1  
            while j >= 0 and value < l[j]:  
                l[j + 1] = l[j]  
                j -= 1  
            l[j + 1] = value 
        return l 

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