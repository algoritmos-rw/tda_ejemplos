import networkx as nx
from countries import show_map

map = show_map(2)

def crear_mapa():
    g = nx.Graph()
    g.add_nodes_from(["Argentina", "Brasil", "Uruguay", "Chile", "Perú", "Paraguay", "Bolivia", "Ecuador", "Venezuela",
                      "Colombia", "Surinam", "Guyana", "Guyana Francesa"])
    g.add_edges_from([("Argentina", "Uruguay"), ("Argentina", "Chile"), ("Argentina", "Bolivia"),
                      ("Argentina", "Brasil"), ("Argentina", "Paraguay"), ("Brasil", "Uruguay"), ("Brasil", "Paraguay"),
                      ("Brasil", "Bolivia"), ("Brasil", "Surinam"), ("Brasil", "Guyana Francesa"), ("Brasil", "Guyana"),
                      ("Brasil", "Venezuela"), ("Brasil", "Colombia"), ("Brasil", "Perú"), ("Chile", "Bolivia"),
                      ("Chile", "Perú"), ("Paraguay", "Bolivia"), ("Perú", "Bolivia"), ("Ecuador", "Perú"),
                      ("Ecuador", "Colombia"), ("Colombia", "Perú"), ("Colombia", "Venezuela"), ("Venezuela", "Guyana"),
                      ("Surinam", "Guyana"), ("Surinam", "Guyana Francesa")])
    return g


def es_compatible(grafo, colores, v):
    for w in grafo.neighbors(v):
        if w in colores and colores[w] == colores[v]:
            return False
    return True


def _coloreo_rec(grafo, k, colores, v):
    map.update(colores, v, "Elijo un vértice sin colorear")

    for color in range(k):
        colores[v] = color

        map.update(colores, v, "Elijo un color y avanzo si puedo")
        if not es_compatible(grafo, colores, v):
            map.update(colores, v, "Solución parcial inválida: elijo otro color")
            continue

        correcto = True
        for w in grafo.neighbors(v):
            if w in colores:
                continue
            map.update(colores, v, "Solución parcial válida: llamo recursivamente")
            if not _coloreo_rec(grafo, k, colores, w):
                correcto = False
                map.update(colores, v, "Solución parcial inválida: elijo otro color")
                break
        if correcto:
            return True
    del colores[v]
    map.update(colores, v, "Solución parcial inválida: vuelvo")
    return False


def coloreo(grafo, k):
    colores = {}
    if _coloreo_rec(grafo, k, colores, "Argentina"):
        map.update(colores, "", "Solución encontrada")
        print(colores)
        return True
    else:
        map.update(colores, "", "No se encontró solución")
        print(colores)
        return False


if __name__ == "__main__":
    print(coloreo(crear_mapa(), 4))
    map.wait_for_close()
