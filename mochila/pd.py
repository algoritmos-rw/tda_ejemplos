IDX_VALOR = 0
IDX_PESO = 1


def mochila_pd(elementos, W):
    matriz = [[0 for j in range(W + 1)] for i in range(len(elementos) + 1)]
    for i in range(1, len(elementos) + 1):
        elem = elementos[i-1]
        for j in range(1, W + 1):
            if elem[IDX_PESO] > j:
                matriz[i][j] = matriz[i-1][j]
            else:
                matriz[i][j] = max(matriz[i-1][j], matriz[i-1][j - elem[IDX_PESO]] + elem[IDX_VALOR])
    return matriz[len(elementos)][W]
