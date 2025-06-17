import random
import heapq
INDIVIDUOS = 100
ITERACIONES = 50
SELECCION = int(0.3 * INDIVIDUOS)
ELITISTA = 5
PROB_MUTACION = 0.2

def tan_bien_ordenado(arreglo):
    rta = 0
    for i in range(1, len(arreglo)):
        if arreglo[i] >= arreglo[i-1]:
            rta += 1
    return rta


def conteo_inversiones_rec(arreglo):
    # si, tecnicamente estamos ordenando, pero sirve para el ejemplo, con la funcion de arriba va a dar peores
    # resultados (que tienen sentido). Podriamos implementar esto de forma cuadratica sin ordenar pero me haria
    # ejecutar mas lentoe el ejemplo
    if len(arreglo) <= 1:
        return arreglo, 0
    izq = arreglo[:len(arreglo)//2]
    der = arreglo[len(arreglo)//2:]
    izq_ord, conteos_izq = conteo_inversiones_rec(izq)
    der_ord, conteos_der = conteo_inversiones_rec(der)
    ord, conteos_aca = intercalar(izq_ord, der_ord)
    return ord, conteos_aca + conteos_izq + conteos_der


def conteo_inversiones(arreglo):
    _, inversiones = conteo_inversiones_rec(arreglo)
    return inversiones


def intercalar(izq, der):
    i = 0
    j = 0
    resultado = []
    conteos = 0
    while i < len(izq) and j < len(der):
        if izq[i] <= der[j]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1
            conteos += len(izq) - i

    while i < len(izq):
        resultado.append(izq[i])
        i += 1
    while j < len(der):
        resultado.append(der[j])
        j += 1
    return resultado, conteos


def aplicar_generacion(individuos):
    mas_aptos = heapq.nsmallest(SELECCION, individuos, key=conteo_inversiones)
    siguiente_generacion = []
    while len(siguiente_generacion) < len(individuos) - ELITISTA:
        ind1, ind2 = random.sample(mas_aptos, 2)
        nuevo = []
        usados = set()
        for i in range(len(ind1)):
            if ind1[i] in usados and ind2[i] in usados:
                # print("ups")
                break
            rnd = random.choice((1, 2))
            if ind1[i] in usados or (rnd == 2 and ind2[i] not in usados):
                usados.add(ind2[i])
                nuevo.append(ind2[i])
            else:
                usados.add(ind1[i])
                nuevo.append(ind1[i])
        else:
            siguiente_generacion.append(nuevo)

    for ind in siguiente_generacion:
        if random.uniform(0, 1) < PROB_MUTACION:
            i, j = random.sample(range(len(ind)), 2)
            aux = ind[i]
            ind[i] = ind[j]
            ind[j] = aux

    for i in range(ELITISTA):
        siguiente_generacion.append(mas_aptos[i])
    return siguiente_generacion


def ordenar(arreglo):
    individuos = [arreglo[:] for i in range(INDIVIDUOS)]
    for arr in individuos:
        random.shuffle(arr)

    for i in range(ITERACIONES):
        # for i in individuos:
        #    print(i)
        # input("---")
        individuos = aplicar_generacion(individuos)

    # print(individuos)
    return min(individuos, key=conteo_inversiones)


if __name__ == "__main__":
    print(ordenar([0, 18, 9, 7, 4, 6, 5, 22, 13, 11, 16, 8, 19, 21, 3, 2, 14, 20, 1, 10, 23, 15, 24, 17, 12]))
