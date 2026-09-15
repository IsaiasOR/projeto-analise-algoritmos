def merge_sort(vector, start=0, end=None):
    if end is None:
        end = len(vector) - 1
    if start >= end:
        return
    mid = (start + end) // 2
    merge_sort(vector, start, mid)
    merge_sort(vector, mid + 1, end)
    merge(vector, start, mid, end)

def merge(vector, start, mid, end):
    temp = []
    i = start
    j = mid + 1
    while i <= mid and j <= end:
        if vector[i] <= vector[j]:
            temp.append(vector[i])
            i += 1
        else:
            temp.append(vector[j])
            j += 1
    while i <= mid:
        temp.append(vector[i])
        i += 1
    while j <= end:
        temp.append(vector[j])
        j += 1
    for k in range(len(temp)):
        vector[start + k] = temp[k]

vector = [38, 27, 43, 3, 9, 82, 10]
print("------------------ Merge Sort ------------------")
print("Vector original:", vector)
merge_sort(vector)
print("Vector ordenado:", vector)
