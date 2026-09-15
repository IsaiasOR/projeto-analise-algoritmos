vector = [38, 27, 43, 3, 9, 82, 10]

def heap_sort(vector):
    print("Vector original:", vector)
    n = len(vector)

    # Construye el max heap
    for i in range(n // 2 - 1, -1, -1):
        sift(vector, n, i)

    for i in range(n - 1, 0, -1):
        vector[0], vector[i] = vector[i], vector[0]
        sift(vector, i, 0)
    return vector

def sift(vector, size, root):
    largest = root
    left = 2 * root + 1
    right = 2 * root + 2
    if left < size and vector[left] > vector[largest]:
        largest = left

    if right < size and vector[right] > vector[largest]:
        largest = right

    if largest != root:
        vector[root], vector[largest] = vector[largest], vector[root]
        sift(vector, size, largest)

print("------------------ Heapsort ------------------")
print("Vector ordenado:", heap_sort(vector))
