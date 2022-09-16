'''
#Insertion Sort

def insertionSort(n):
    for i in range(0, len(n)):
        for j in range(i-1, -1, -1):
            if n[i] < n[j]:
                n[j], n[i] = n[i], n[j]
                i = i-1
                j = j-1
            else:
                break
    return n
n=[2,5,5,1,7,3,8,4,4,0,1,-1]
print(insertionSort(n))
'''


