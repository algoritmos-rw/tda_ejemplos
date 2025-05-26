
def crear_red(calles, casa, escuela):
    red = Grafo(es_dirigido=True)
    for esquina in calles:
        red.agregar_vertice(esquina)
    visitados = set()
    ficticios = {}
    for esquina in calles:
        for conectada in calles.adyacentes(esquina):
            if conectada in visitados:
                continue
            elif esquina == casa or conectada == escuela:
                red.arista(esquina, conectada, peso=1)
            elif esquina == escuela or conectada == casa:
                red.arista(conectada, esquina, peso=1)
            else:
                red.agregar_vertice(esquina + conectada)
                red.arista(esquina, conectada, peso=1)
                red.arista(conectada, esquina + conectada, peso=1)
                red.arista(esquina + conectada, esquina, peso=1)
                ficticios[esquina + conectada] = (esquina, conectada)
        visitados.add(esquina)
        return red, ficticios

def carlos(calles, cant_hijos, casa, escuela):
    red, ficticios = crear_red(calles, casa, escuela)
    flujo = flujoMaximo(red)
    cantCaminos = 0
    for conectada in red.adyacentes(casa):
        if flujo[casa][conectada] > 0:
            cantCaminos += 1
    if cantCaminos < cant_hijos:
        return None

    # corregimos los flujos para que se cancelen si van ida y vuelta:
    for ficticio in ficticios:
        v, w = ficticios[ficticio]
        if flujo[v][w] == 1 and flujo[ficticio][v] == 1:
            flujo[v][w] = 0
            flujo[w][ficticio] = 0
            flujo[ficticio][v] = 0

    caminos = []
    for i in range(cant_hijos):
        camino = []
        camino.append(casa)
        v = casa
        while v != escuela:
            for w in red.adyacentes(v):
                if flujo[v][w] == 1:
                    flujo[v][w] = 0
                    v = w
                    if v not in ficticios:
                        camino.append(v)
                    break
        caminos.append(camino)
    return caminos