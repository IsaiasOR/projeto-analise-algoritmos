array = [38, 27, 43, 3, 9, 82, 10]
print("-----------------------------------------------")
print("Array inicial: ", array)
print("-----------------------------------------------\n")

def multi_quick_sort(array, k, left=0, right=None):
    if right is None:
        right = len(array) - 1

    if left >= right:
        return array

    current_k = min(k, right - left)

    p_indices = partition(array, left, right, current_k)

    multi_quick_sort(array, k, left, p_indices[0] - 1)

    for i in range(len(p_indices) - 1):
        multi_quick_sort(array, k, p_indices[i] + 1, p_indices[i + 1] - 1)

    multi_quick_sort(array, k, p_indices[-1] + 1, right)

    return array

def partition(array, left, right, k):
    pivots = sorted(array[right - k + 1 : right + 1])
    buckets = [[] for _ in range(k + 1)]

    for j in range(left, right - k + 1):
        element = array[j]
        placed = False
        for p_idx in range(k):
            if element <= pivots[p_idx]:
                buckets[p_idx].append(element)
                placed = True
                break
        if not placed:
            buckets[k].append(element)

    index = left
    final_pivot_indices = []

    for i in range(k):
        for item in buckets[i]:
            array[index] = item
            index += 1

        array[index] = pivots[i]
        final_pivot_indices.append(index)
        index += 1

    for item in buckets[k]:
        array[index] = item
        index += 1

    print(f"Partición con pivotes {pivots}: {array[left:right+1]}")
    return final_pivot_indices

cantidad_pivotes = 5
result = multi_quick_sort(array, cantidad_pivotes)
print("-----------------------------------------------")
print("Array ordenado: ", result)
print("-----------------------------------------------\n")
