import networkx as nx


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
    for color in range(k):
        colores[v] = color
        if not es_compatible(grafo, colores, v):
            continue
        correcto = True
        for w in grafo.neighbors(v):
            if w in colores:
                continue
            if not _coloreo_rec(grafo, k, colores, w):
                correcto = False
                break
        if correcto:
            return True
    del colores[v]
    return False


def coloreo(grafo, k):
    colores = {}
    if _coloreo_rec(grafo, k, colores, "Argentina"):
        print(colores)
        return True
    else:
        print(colores)
        return False


if __name__ == "__main__":
    print(coloreo(crear_mapa(), 4))
