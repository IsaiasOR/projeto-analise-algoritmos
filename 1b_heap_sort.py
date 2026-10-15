def heap_sort(vector, k = None):
    if k is None:
        k = 2

    k = max(k, 2)

    n = len(vector)

    # Construye el max heap
    # Se empieza en el ultimo nodo no hoja
    for i in range((n - 2) // k, -1, -1):
        sift(vector, n, i, k)

    # Se extrae el máximo repetidamente
    for i in range(n - 1, 0, -1):
        # Se envia el maximo a su posicion definitiva (final del heap)
        vector[0], vector[i] = vector[i], vector[0]
        sift(vector, i, 0, k)
    return vector

def sift(vector, size, root, k):
    # Se supone que los subarboles de los hijos de root ya son heaps.
    # Solo root puede violar la propiedad; sift lo hunde hasta repararla.
    largest = root
    first = k * root + 1

    # Se recorren los hijos y se corta en size para evitar comparar hijos que no existen
    for child in range(first, min(first + k, size)):
        if vector[child] > vector[largest]:
            largest = child  # se recuerda al mayor visto hasta ahora

    # Recien tras ver a todos los hijos se sabe cual es el mayor.
    if largest != root:
        vector[root], vector[largest] = vector[largest], vector[root]
        # El elemento que bajo puede violar la propiedad en su nueva posicion.
        sift(vector, size, largest, k)


print("------------------ K = 1 ------------------")
vector = [38, 27, 43, 3, 9, 82, 10]
print("Vector original:", vector)
print("Vector ordenado:", heap_sort(vector))

print("------------------ k = 2 ------------------")

vector = [38, 27, 43, 3, 9, 82, 10]
print("Vector original:", vector)
print("Vector ordenado:", heap_sort(vector, 2))   # [3, 9, 10, 27, 38, 43, 82]

print("---------- k = 3 (mismo vector) ----------")
vector = [38, 27, 43, 3, 9, 82, 10]
print("Vector original:", vector)
print("Vector ordenado:", heap_sort(vector, 3))   # [3, 9, 10, 27, 38, 43, 82]

print("---------- Vector vacio ----------")
vector = []
print("Vector original:", vector)
print("Vector ordenado:", heap_sort(vector, 3))   # []

print("---------- Un solo elemento ----------")
vector = [5]
print("Vector original:", vector)
print("Vector ordenado:", heap_sort(vector, 3))   # [5]

print("---------- k = 1 (lista enlazada) ----------")
vector = [4, 1, 3, 2]
print("Vector original:", vector)
print("Vector ordenado:", heap_sort(vector, 1))   # [1, 2, 3, 4]

print("---------- k mayor que n ----------")
vector = [9, 4, 7]
print("Vector original:", vector)
print("Vector ordenado:", heap_sort(vector, 10))  # [4, 7, 9]

print("---------- Elementos repetidos ----------")
vector = [5, 3, 5, 1, 3, 5]
print("Vector original:", vector)
print("Vector ordenado:", heap_sort(vector, 3))   # [1, 3, 3, 5, 5, 5]

print("---------- Orden inverso, k = 4 ----------")
vector = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print("Vector original:", vector)
print("Vector ordenado:", heap_sort(vector, 4))   # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("---------- Negativos y repetidos ----------")
vector = [-3, 0, 12, -7, 5, 5, -1]
print("Vector original:", vector)
print("Vector ordenado:", heap_sort(vector, 2))   # [-7, -3, -1, 0, 5, 5, 12]
