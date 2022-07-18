from numpy import zeros, random

def mergesort(arr):
    if len(arr) > 1:
        m = len(arr)//2
        left = arr[:m]
        right = arr[m:]

        left = mergesort(left)
        right = mergesort(right)

        return merge(left,right)
    else:
        return arr

def merge(one, two):
    arrlen = len(one) + len(two)
    array = [0]*arrlen
    for i in range(arrlen):
        if not any(one):
            array[i] = two[0]
            two = two[1:]
            continue
        if not any(two):
            array[i] = one[0]
            one = one[1:]
            continue
        if one[0] < two[0]:
            array[i] = one[0]
            one = one[1:]
        else:
            array[i] = two[0]
            two = two[1:]
    return array

def insertsort(arr):
    for i in range(1,len(arr)):
        for j in range(i):
            if arr[i] < arr[j]:
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp
    return arr

def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
    return arr

if __name__ == "__main__":
    arr = random.randint(1, 10000, 5000)
    #arr = [5, 3, 4, 2, 1]
    print(arr)
    x = mergesort(arr)
    print(x)