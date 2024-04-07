import math

NULL_ELEM = 0
PIOLA = True
ALTERNATIVAS = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G"}
# ALTERNATIVAS = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
TAM = len(ALTERNATIVAS)
DIV_CUADRANTE = int(math.sqrt(TAM))


def resolver_sudoku_piola(matriz):
    faltantes = set()
    for i in range(TAM):
        for j in range(TAM):
            if matriz[i][j] == NULL_ELEM:
                faltantes.add((i, j))
    if not _resolver_sudoku_bt(matriz, faltantes):
        return None
    else:
        return matriz


def alternativas_validas(matriz, pos):
    alternativas = set(ALTERNATIVAS)
    posi, posj = pos
    # Me fijo por fila:
    for i in range(TAM):
        if i != posi and matriz[i][posj] != NULL_ELEM and matriz[i][posj] in alternativas:
            alternativas.remove(matriz[i][posj])
    # Me fijo por columna:
    for j in range(TAM):
        if j != posj and matriz[posi][j] != NULL_ELEM and matriz[posi][j] in alternativas:
            alternativas.remove(matriz[posi][j])
    # Me fijo por cuadrante:
    ini_i, fin_i, ini_j, fin_j = posiciones_cuadrante(pos)
    for i in range(ini_i, fin_i):
        for j in range(ini_j, fin_j):
            if (i != posi or j != posj) and matriz[i][j] != NULL_ELEM and matriz[i][j] in alternativas:
                alternativas.remove(matriz[i][j])
    return alternativas


def posiciones_cuadrante(pos):
    sectori, sectorj = pos[0] // DIV_CUADRANTE, pos[1] // DIV_CUADRANTE
    return sectori * DIV_CUADRANTE, (sectori + 1) * DIV_CUADRANTE, sectorj * DIV_CUADRANTE, (sectorj + 1) * DIV_CUADRANTE


def _resolver_sudoku_bt(matriz, faltantes):
    if len(faltantes) == 0:
        return True
    # de las faltantes nos quedamos con la que menos alternativas le falten:
    alternativas_por_faltante = {pos: alternativas_validas(matriz, pos) for pos in faltantes}
    siguiente = min(faltantes, key=lambda pos: len(alternativas_por_faltante[pos]))
    i, j = siguiente
    alternativas_siguiente = alternativas_por_faltante[siguiente]
    if len(alternativas_siguiente) == 0:
        return False
    faltantes.remove(siguiente)
    for alternativa in alternativas_siguiente:
        matriz[i][j] = alternativa
        if _resolver_sudoku_bt(matriz, faltantes):
            return True
    faltantes.add(siguiente)
    matriz[i][j] = NULL_ELEM
    return False


def resolver_sudoku_naive(matriz):
    if _resolver_sudoku_naive_bt(matriz, (0, 0)):
        return matriz
    else:
        return None


def _resolver_sudoku_naive_bt(matriz, actual):
    i, j = actual
    if i == TAM:
        return True
    siguiente = siguiente_de(actual)
    if matriz[i][j] != NULL_ELEM:
        return _resolver_sudoku_naive_bt(matriz, siguiente)
    for alternativa in alternativas_validas(matriz, actual):
        matriz[i][j] = alternativa
        if _resolver_sudoku_naive_bt(matriz, siguiente):
            return True
    matriz[i][j] = NULL_ELEM
    return False


def siguiente_de(actual):
    i, j = actual
    siguientei = i if j < TAM - 1 else i + 1
    siguientej = j + 1 if j < TAM - 1 else 0
    return siguientei, siguientej


def main(path):
    matriz = []
    with open(path) as f:
        for l in f:
            matriz.append(list(map(lambda v: NULL_ELEM if len(v.strip()) == 0 else v, l.strip().split("|"))))
    if PIOLA:
        resuelto = resolver_sudoku_piola(matriz)
    else:
        resuelto = resolver_sudoku_naive(matriz)
    if resuelto is None:
        print("No hay solucion")
    else:
        for fila in resuelto:
            print(fila)


if __name__ == "__main__":
    main("sudoku_16_experto.txt")
