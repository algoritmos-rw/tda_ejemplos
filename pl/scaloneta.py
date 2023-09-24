import pulp
TIEMPO_SCALONI = 0
TIEMPO_AYUD = 1


def cargar(path):
    resul = []
    with open(path) as f:
        f.readline()
        for l in f:
            si, ai = l.strip().split(",")
            resul.append((int(si), int(ai)))
    return resul


def filter_not_none(col):
    return list(filter(lambda i: i is not None, col))


def sort_by_p_i(equipos, p):
    nuevo = equipos[:]
    for i in range(len(equipos)):
        nuevo[int(p[i].value())] = equipos[i]
    return nuevo


def orden_pl(equipos):
    problem = pulp.LpProblem("products", pulp.LpMinimize)

    y = []
    for i in range(len(equipos)):
        y.append([])
        for j in range(len(equipos)):
            if i == j:
                y[i].append(None)  # para que no moleste al indexar
            else:
                y[i].append(pulp.LpVariable("y_" + str(i) + "," + str(j), cat="Binary"))

    for i in range(len(equipos)):
        problem += pulp.lpSum(filter_not_none(y[i])) <= 1

    for j in range(len(equipos)):
        problem += pulp.lpSum(filter_not_none([y[i][j] for i in range(len(y))])) <= 1

    p = []
    for i in range(len(equipos)):
        p_i = pulp.LpAffineExpression(filter_not_none([(y[i][j], j) if y[i][j] is not None else None for j in range(len(y))]))
        p.append(p_i)

    z = []
    M = len(equipos) + 1
    for i in range(len(equipos)):
        z.append([])
        for k in range(len(equipos)):
            if i == k:
                z[i].append(None)  # para que no molesten los rangos
                continue
            z[i].append(pulp.LpVariable("z_" + str(i) + "," + str(k), cat="Binary"))
            problem += p[i] >= p[k] + 1 - M * (1 - z[i][k])
            problem += p[k] >= p[i] + 1 - M * z[i][k]

    t = []
    for i in range(len(equipos)):
        t_i = pulp.LpAffineExpression(filter_not_none([(z[i][k], equipos[k][TIEMPO_SCALONI]) if i != k else None for k in range(len(y))])) + \
              equipos[i][TIEMPO_SCALONI] + equipos[i][TIEMPO_AYUD]
        t.append(t_i)

    resul = pulp.LpVariable("resultado")
    for t_i in t:
        problem += resul >= t_i

    problem += resul
    problem.solve()

    return sort_by_p_i(equipos, p)


def tiempo_consumido(elems):
    tiempos_finales = []
    t_scaloni = 0
    for si, ai in elems:
        t_scaloni += si
        tiempos_finales.append(t_scaloni + ai)
    return max(tiempos_finales)


if __name__ == "__main__":
    # Optimo para 3: 10; opt para 10: 29; opt para 100: 5223
    elems = cargar("scaloneta_100.txt")
    print(tiempo_consumido(elems))
    print(tiempo_consumido(orden_pl(elems)))
