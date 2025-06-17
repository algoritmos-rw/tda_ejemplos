import random
import heapq

from backtracking.nreinas import n_reinas

INDIVIDUOS = 100
ITERACIONES = 50
SELECCION = int(0.3 * INDIVIDUOS)
ELITISTA = 5
PROB_MUTACION = 0.3


def swap(cont, i, j):
    aux = cont[i]
    cont[i] = cont[j]
    cont[j] = aux


def valor(individuo):
    suma = 0
    for v in individuo:
        suma += individuo[v]
    return suma


def aplicar_generacion(grafo, individuos):
    mas_aptos = heapq.nlargest(SELECCION, individuos, key=valor)
    siguiente_generacion = []
    while len(siguiente_generacion) < len(individuos) - ELITISTA:
        ind1, ind2 = random.sample(mas_aptos, 2)
        nuevo = {}
        for v in grafo:
            if ind1[v] == ind2[v]:
                nuevo[v] = ind1[v]
            elif random.choice((0, 1)) == 0:
                nuevo[v] = ind1[v]
            else:
                nuevo[v] = ind2[v]
        if es_is(grafo, nuevo):
            siguiente_generacion.append(nuevo)

    for ind in siguiente_generacion:
        if random.uniform(0, 1) < PROB_MUTACION:
            i, j = random.sample(list(grafo.nodes), 2)
            if ind[i] != ind[j]:
                swap(ind, i, j)
                if not es_is(grafo, ind):
                    swap(ind, i, j)

    for i in range(ELITISTA):
        siguiente_generacion.append(mas_aptos[i])
    return siguiente_generacion


def es_is(grafo, asignacion):
    isset = set(filter(lambda v: asignacion[v] == 1, grafo))
    for v in isset:
        for w in isset:
            if w in grafo[v]:
                return False
    return True


def independent_set(grafo):
    individuos = [{v: 0 for v in grafo} for i in range(INDIVIDUOS)]
    for ind in individuos:
        for vertice in grafo:
            if random.choice((0, 1)) == 1:
                ind[vertice] = 1
                if not es_is(grafo, ind):
                    ind[vertice] = 0

    for i in range(ITERACIONES):
        individuos = aplicar_generacion(grafo, individuos)
        
    return max(individuos, key=valor)

if __name__ == "__main__":
    tablero = n_reinas(8)
    solucion = independent_set(tablero)
    setsolucion = set(filter(lambda v: solucion[v] == 1, solucion))
    print(setsolucion)

