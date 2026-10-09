def quick_sort(array, left=0, right=None):
    if right is None:
        right = len(array) - 1

    if left < right:
        p = partition(array, left, right)
        quick_sort(array, left, p - 1)
        quick_sort(array, p + 1, right)

    return array

def partition(array, left, right):
    pivot = array[right]
    i = left - 1
    for j in range(left, right):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[right] = array[right], array[i + 1]
    return i + 1


array = [38, 27, 43, 3, 9, 82, 10]
print("-----------------------------------------------")
print("Array inicial: ", array)
print("-----------------------------------------------\n")

result = quick_sort(array)
print("-----------------------------------------------")
print("Array ordenado: ", result)
print("-----------------------------------------------\n")
