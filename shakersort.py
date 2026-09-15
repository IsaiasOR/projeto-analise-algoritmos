vector = [20, 1, 15, 5, 25, 5, 10] # C1
inicio = 0 # C2
fin = len(vector) - 1 # C3
intercambio = True # C4
pasos = 0 # C5

print("Vector inicial: ", vector)

while intercambio: # C6
    intercambio = False # C7

    for i in range(inicio, fin): # C8

        if vector[i] > vector[i + 1]: # C9
            vector[i], vector[i + 1] = vector[i + 1], vector[i] # C10
            pasos += 1 # C11
            intercambio = True # C12
            print(pasos, "→ Nuevo cambio: ", vector)
    fin -= 1 # C13

    if not intercambio: # C14
        break

    intercambio = False # C15

    for i in range(fin, inicio, -1): # C16

        if vector[i - 1] > vector[i]: # C17
            vector[i - 1], vector[i] = vector[i], vector[i - 1] # C18
            pasos += 1 # C19
            intercambio = True # C20
            print(pasos, ". Nuevo cambio: ", vector)
    inicio += 1 # C21

print("Vector ordenado: ", vector)
