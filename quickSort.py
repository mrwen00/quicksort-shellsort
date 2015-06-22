

def partition(A, p, q, m1, m2):


    i = p
    x = A[i]
    for j in range(i+1, q):
        if(A[j] < x):
            A[i+1], A[j] = A[j], A[i+1]
            i = i + 1
    A[i], A[p] = A[p], A[i]
    return i


    

def QuickSort(A, p, q):
    if p < q:
        r = partition(A,p, q)
        QuickSort(A, p, r)
        QuickSort(A, r+1, q)





A = [6,10,13,5,8,3,2,11]
QuickSort(A,0,len(A))
print A
