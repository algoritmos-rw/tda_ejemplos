from typing import List

import pulp
from pulp import LpAffineExpression as Sumatoria


def cargar_mochila(ruta):
    w = []
    v = []
    with open(ruta) as f:
        W = int(f.readline().strip())
        for l in f:
            vi, wi = l.strip().split(",")
            w.append(int(wi))
            v.append(int(vi))
    return v, w, W


def mochila_variable(v: List[int], w: List[int], W: int):
    y = []
    for i in range(len(v)):
        y.append(pulp.LpVariable("y" + str(i), cat="Binary"))

    problem = pulp.LpProblem("products", pulp.LpMaximize)
    problem += Sumatoria([(y[i], w[i]) for i in range(len(y))]) <= W
    problem += Sumatoria([(y[i], v[i]) for i in range(len(y))])

    problem.solve()
    return list(map(lambda yi: pulp.value(yi), y))


if __name__ == "__main__":
    valores, pesos, W = cargar_mochila("mochila.txt")
    y = mochila_variable(valores, pesos, W)
    print(y)
    print("Peso usado:", sum([pesos[i] * y[i] for i in range(len(y))]))
    print("Valor obtenido:", sum([valores[i] * y[i] for i in range(len(y))]))
