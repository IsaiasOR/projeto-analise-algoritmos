vector = [8, 7, 6, 5, 4, 3, 2, 1, 12, 3, 44, 6, 0]
iteraciones = 0

print("-----------------------------------------------")
print("Vector inicial: ", vector)
print("-----------------------------------------------\n")

for i in range(0, len(vector) - 1, 2):
    iteraciones += 1
    print("---------- Iteracion: ", iteraciones, "----------")

    if vector[i] > vector[i + 1]:
        vector[i], vector[i + 1] = vector[i + 1], vector[i]

    print("- Cambio: ", vector)

    element_menor = vector[i]
    element_mayor = vector[i + 1]

    j = i + 1
    while j > 1 and element_mayor < vector[j - 2]:
        vector[j] = vector[j - 2]
        j -= 1
        print("- Desplazamiento: ", vector)
    vector[j] = element_mayor

    k = j - 1
    while k > 0 and element_menor < vector[k - 1]:
        vector[k] = vector[k - 1]
        k -= 1
        print("- Desplazamiento: ", vector)
    vector[k] = element_menor

if len(vector) % 2 != 0:
    print("---------- Iteracion extra (Elemento impar) ----------")
    ultimo_idx = len(vector) - 1
    elemento_impar = vector[ultimo_idx]

    m = ultimo_idx
    # Se compara y desplaza hacia la derecha si los elementos son mayores
    while m > 0 and elemento_impar < vector[m - 1]:
        vector[m] = vector[m - 1]
        m -= 1
        print("- Desplazamiento (impar): ", vector)

    # Se inserta el elemento en su posición definitiva
    vector[m] = elemento_impar

print("-----------------------------------------------")
print("Vector ordenado: ", vector)
print("-----------------------------------------------")
