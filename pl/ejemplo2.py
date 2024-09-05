import pulp


def ejemplo():
    problem = pulp.LpProblem("products", pulp.LpMinimize)
    vp = pulp.LpVariable("vp")
    ss = pulp.LpVariable("ss")
    problem += vp <= 40
    problem += ss <= 30
    problem += 5 * ss >= 50  # mostrar cambiando a 51
    problem += vp + 2 * ss >= 50  # mostrar cambiando a 51
    problem += 1 * vp + 6 * ss
    problem.solve()
    return pulp.value(vp), pulp.value(ss)


def ejemplo_cajas_enteras():
    vp = pulp.LpVariable("vp")
    ss = pulp.LpVariable("ss", cat="Integer")
    problem = pulp.LpProblem("products", pulp.LpMinimize)
    problem += vp <= 40
    problem += ss <= 30
    problem += 5 * ss >= 51
    problem += vp + 2 * ss >= 51
    problem += 1 * vp + 6 * ss
    problem.solve()
    return pulp.value(vp), pulp.value(ss)


if __name__ == "__main__":
    x, y = ejemplo()
    print("Cantidad de kgr a Valle Patagua:", x, " - Cantidad de cajas de Salud Sustentable:", y)
    print("Costo:", x + 6 * y)
