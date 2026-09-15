vector = [64, 25, 12, 22, 11, 90, 45]

print("-----------------------------------------------")
print("Vector inicial: ", vector)
print("-----------------------------------------------\n")

for i in range(len(vector)):
    min_index = i

    for j in range(i + 1, len(vector)):
        if vector[j] < vector[min_index]:
            min_index = j
            print("Comparando", vector[j], " con indice ", j, " & ", vector[min_index], " con indice ", min_index)

    vector[i], vector[min_index] = vector[min_index], vector[i]

print("-----------------------------------------------")
print("Vector ordenado: ", vector)
print("-----------------------------------------------")
