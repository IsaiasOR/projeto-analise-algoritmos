def bubble_sort(vector):
    print("Vector original:", vector)

    n = len(vector)
    for i in range(n - 1):
        print("Paso", i + 1)
        for j in range(n - i - 1):
            if vector[j] > vector[j + 1]:
                vector[j], vector[j + 1] = vector[j + 1], vector[j]
                print(" - Swap:", vector)
    return vector

vector = [38, 27, 43, 3, 9, 82, 10]
print("------------------ Bubblesort ------------------")
print("Vector ordenado:", bubble_sort(vector))
