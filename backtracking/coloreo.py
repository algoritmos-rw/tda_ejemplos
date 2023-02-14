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


def coloreo(grafo, k):
    return None


if __name__ == "__main__":
    print(coloreo(crear_mapa(), 4))
