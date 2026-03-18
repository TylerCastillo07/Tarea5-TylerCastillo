# ---------------------------------------------------------
# Módulo: ordenamientos.py
# Aquí implementarán sus funciones de ordenamiento.
#
# Cada función debe:
#   - Recibir una lista de strings (nombres)
#   - Tener el parámetro ascendente=True por omisión
#   - Ordenar la lista in-place (sin crear una copia)
#   - Regresar la lista ordenada
#
# Algoritmos a implementar:
#   1. Bubble Sort
#   2. Insertion Sort
#   3. Selection Sort
#   4. Shell Sort
#   5. Merge Sort
#   6. QuickSort (solo pivote central)
# ---------------------------------------------------------
#Nombre del alumno: Tyler Gabriel Castillo Lozano 2163447 x60

def bubble_sort(lista, ascendente=True):
    """
    Implementa el algoritmo Bubble Sort.
    Ordena la lista in-place.
    """
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1):

            if ascendente:
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
            else:
                if lista[j] < lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista
    



def insertion_sort(lista, ascendente=True):
    """
    Implementa el algoritmo Insertion Sort.
    Ordena la lista in-place.
    """
    for i in range(1, len(lista)):

        actual = lista[i]
        j = i - 1

        if ascendente:
            while j >= 0 and lista[j] > actual:
                lista[j + 1] = lista[j]
                j -= 1
        else:
            while j >= 0 and lista[j] < actual:
                lista[j + 1] = lista[j]
                j -= 1

        lista[j + 1] = actual

    return lista



def selection_sort(lista, ascendente=True):
    """
    Implementa el algoritmo Selection Sort.
    Ordena la lista in-place.
    """
    n = len(lista)

    for i in range(n):

        pos = i

        for j in range(i + 1, n):

            if ascendente:
                if lista[j] < lista[pos]:
                    pos = j
            else:
                if lista[j] > lista[pos]:
                    pos = j

        lista[i], lista[pos] = lista[pos], lista[i]

    return lista



def shell_sort(lista, ascendente=True):
    """
    Implementa el algoritmo Shell Sort.
    Ordena la lista in-place.
    """
    n = len(lista)
    gap = n // 2

    while gap > 0:

        for i in range(gap, n):

            temp = lista[i]
            j = i

            if ascendente:
                while j >= gap and lista[j - gap] > temp:
                    lista[j] = lista[j - gap]
                    j -= gap
            else:
                while j >= gap and lista[j - gap] < temp:
                    lista[j] = lista[j - gap]
                    j -= gap

            lista[j] = temp

        gap //= 2

    return lista



def merge_sort(lista, ascendente=True):
    """
    Implementa el algoritmo Merge Sort.
    Debe regresar la lista ordenada.
    Puede usar funciones auxiliares si lo desean.
    """
    if len(lista) > 1:

        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]

        merge_sort(izquierda, ascendente)
        merge_sort(derecha, ascendente)

        i = j = k = 0

        while i < len(izquierda) and j < len(derecha):

            if ascendente:
                if izquierda[i] < derecha[j]:
                    lista[k] = izquierda[i]
                    i += 1
                else:
                    lista[k] = derecha[j]
                    j += 1
            else:
                if izquierda[i] > derecha[j]:
                    lista[k] = izquierda[i]
                    i += 1
                else:
                    lista[k] = derecha[j]
                    j += 1

            k += 1

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1

    return lista



def quick_sort(lista, ascendente=True):
    """
    Implementa QuickSort usando pivote central.
    Debe ordenar la lista in-place.
    Puede usar funciones auxiliares si lo desean.
    """
    def quicksort_aux(inicio, fin):

        if inicio >= fin:
            return

        pivote = lista[(inicio + fin) // 2]
        i = inicio
        j = fin

        while i <= j:

            if ascendente:
                while lista[i] < pivote:
                    i += 1
                while lista[j] > pivote:
                    j -= 1
            else:
                while lista[i] > pivote:
                    i += 1
                while lista[j] < pivote:
                    j -= 1

            if i <= j:
                lista[i], lista[j] = lista[j], lista[i]
                i += 1
                j -= 1

        quicksort_aux(inicio, j)
        quicksort_aux(i, fin)

    quicksort_aux(0, len(lista) - 1)
    return lista
