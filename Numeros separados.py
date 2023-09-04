entrada = input("Ingrese una serie de números separados por espacios: ")
numeros_cadenas = entrada.split()
numeros_enteros = [int(numero) for numero in numeros_cadenas]
def seleccion_sort(lista):
    n = len(lista)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]
seleccion_sort(numeros_enteros)
print("Lista ordenada:", numeros_enteros)
