version = "0.0.1"

def linear_search(array,target):
    for x in range(len(array)):
        if target == array[x]:
            return x
    return -1

def binary_search(array,target):
    array = quick_sort(array)
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if array[mid] > target:
            end = mid - 1
        elif array[mid] < target:
            start = mid + 1
        else:
            return mid
    return -1

def bubble_sort(array):
    length = len(array)
    for x in range(length):
        for y in range(0,length - x - 1):
            if array[y] > array[y + 1]:
                array[y],array[y + 1] = array[y + 1],array[y]
    return array

def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[len(array) // 2]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def insertion_sort(array):
    for x in range(1,len(array)):
        key = array[x]
        j = x - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

def selection_sort(array):
    for x in range(len(array)):
        min_index = x
        for y in range(x + 1,len(array)):
            if array[y] < array[min_index]:
                min_index = y
        array[x],array[min_index] = array[min_index],array[x]
    return array
