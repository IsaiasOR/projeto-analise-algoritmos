def quick_sort(vector, left = 0, right = None, k = 1):
    if right is None:
        right = len(vector) - 1

    if k <= 0:
        k = 1

    if left < right:
        positions_pivots = partition(vector, left, right, k)

        # Marca desde dónde se empieza a procesar el siguiente sub-vector
        inicio = left

        for pivot in positions_pivots:
            # Ordena los elementos que quedaron a la izquierda del pivote actual
            quick_sort(vector, inicio, pivot - 1, k)
            # El primer elemento a la derecha del pivote que se acaba de usar
            inicio = pivot + 1

        quick_sort(vector, inicio, right, k) # Última región
    return vector

def partition(vector, left, right, k):
    # Se evita usar más pivotes que la cantidad de elementos del sub-vector
    k_efectivo = min(k, right - left + 1)
    # Se toman los primeros k elementos del vector y se ordenan
    valores = sorted(vector[left:left + k_efectivo])

    positions = []
    inicio = left

    for v in valores:
        # Se busca el índice del pivote actual en el sub-vector
        # .index(v) busca desde la posición 0 del segmento recortado, por eso se suma inicio (pasar de un indice relativo a absoluto)
        idx_pivote = vector[inicio:right + 1].index(v) + inicio

        # Se mueve el pivote a la primera posición del sub-vector de trabajo
        vector[inicio], vector[idx_pivote] = vector[idx_pivote], vector[inicio]

        l = inicio + 1
        r = right

        while True:
            while l <= r and vector[l] < v:
                l = l + 1
            while r >= l and vector[r] >= v:
                r = r - 1

            if l >= r:
                break

            vector[l], vector[r] = vector[r], vector[l]

        #Se intercambia el pivote (que estaba guardado en inicio) a su posición final r
        vector[inicio], vector[r] = vector[r], vector[inicio]

        positions.append(r)

        # Se actualiza inicio para el siguiente pivote
        inicio = r + 1

    return positions

# --- Tests ---
vector = [38, 27, 43, 3, 9, 82, 10]
print("-----------------------------------------------")
print("Vector inicial con 7 elementos y 2 pivots: ", vector)
result = quick_sort(vector, k=2)
print("Vector ordenado con 7 elementos y 2 pivots: ", result)
print("-----------------------------------------------\n")

vector = [10]
print("-----------------------------------------------")
print("Vector inicial con 1 elemento: ", vector)
result = quick_sort(vector)
print("Vector ordenado con 1 elemento: ", result)
print("-----------------------------------------------\n")

vector = []
print("-----------------------------------------------")
print("Vector inicial con ningún elemento: ", vector)
result = quick_sort(vector)
print("Vector ordenado: ", vector)
print("-----------------------------------------------\n")
