def merge(left, right):
    result = []
    i,j = 0,0
    while (i < len(left)) and (j < len(right)):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def mergeSort(lst):
    if len(lst) < 2:
        return lst

    middle = int(len(lst) / 2)
    left = mergeSort(lst[:middle])
    right = mergeSort(lst[middle:])
    return merge(left, right)

def quicksort(x):
    if len(x) == 1 or len(x) == 0:
        return x
    else:
        pivot = x[0]
        i = 0
        for j in range(len(x)-1):
            if x[j+1] < pivot:
                x[j+1],x[i+1] = x[i+1], x[j+1]
                i += 1
        x[0],x[i] = x[i],x[0]
        first_part = quicksort(x[:i])
        second_part = quicksort(x[i+1:])
        first_part.append(x[i])
        return first_part + second_part

if __name__ == '__main__':
    lst = [12, 11, 13, 5, 6, 7, 15]
    lst2 = [7, 9, 5, 0, 10, 3, 6, 15, 22]
    print mergeSort(lst)
    print quicksort(lst2)
