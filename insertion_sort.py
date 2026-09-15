vector = [45, 7, 3, 89, 23, 6, 1, 8]
print("-----------------------------------------------")
print("Vector inicial: ", vector)
print("-----------------------------------------------\n")

for i in range(1, len(vector)):
    print("-----------------------------------------------")
    print("Passo ", i, ": ", vector)

    key = vector[i]
    j = i - 1

    while j >= 0 and vector[j] > key:
        vector[j + 1] = vector[j]
        print("- Cambio: ", vector)
        j -= 1

    vector[j + 1] = key

print("-----------------------------------------------")
print("Vector ordenado: ", vector)
print("-----------------------------------------------")
