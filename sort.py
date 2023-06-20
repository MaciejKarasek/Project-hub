from numpy import random

# Merge sort algorithm
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

# Insertion sort algorithm
def insertsort(arr):
    for i in range(1,len(arr)):
        for j in range(i):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

# Bubble sort algorithm
def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Quick sort algorithm
def quicksort(arr, low, high):
    if low < high:

        pi = part(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)


def part(arr, low, high):
    pivot = arr[high]

    n = low - 1
    for i in range(low, high):
        if arr[i] <= pivot:
            n += 1
            arr[n], arr[i] = arr[i], arr[n]
    
    arr[n + 1], arr[high] = arr[high], arr[n + 1]

    return n + 1

# Select sorting algorithm
def select(arr):
    for i in range(len(arr) - 1):
        min = arr[i]
        x = i
        for j in range(i + 1,len(arr)):
            if arr[j] < min:
                x = j
                min = arr[j]

        if x != i:
            arr[i], arr[x] = arr[x], arr[i]

if __name__ == "__main__":
    arr = random.randint(1, 5000, 5000)
    #arr = [4,7,3,1,8,5432, 5623, 532 ,324 ,12 ,5, 32 ,52 ,43 ,42, 4,32, 5,32 ,532]
    #print(arr)
    quicksort(arr, 0, len(arr) - 1)
    #print(arr)