import random
import math

def generar_puntos(n):
    generadosx = set()
    generadosy = set()
    resultado = []
    for i in range(n):
        while True:
            x, y = random.randint(0, 100), random.randint(0, 100)
            if x not in generadosx and y not in generadosy:
                resultado.append((x, y))
                generadosx.add(x)
                generadosy.add(y)
                break
    return resultado


def distancia(x, y):
    return math.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)

def comparacion_3(px):
    if len(px) == 2:
        return px[0], px[1]
    d01 = distancia(px[0], px[1])
    d02 = distancia(px[0], px[2])
    d12 = distancia(px[1], px[2])
    if d01 <= d02 and d01 <= d12:
        return px[0], px[1]
    elif d02 <= d01 and d02 <= d12:
        return px[0], px[2]
    else:
        return px[1], px[2]


def construir_qyry(py, x_quiebre):
    qy = []
    ry = []
    for punto in py:
        if punto[0] < x_quiebre:
            qy.append(punto)
        else:
            ry.append(punto)
    return qy, ry


def construir_sy(py, x_quiebre, d):
    sy = []
    for punto in py:
        if abs(punto[0] - x_quiebre) < d:
            sy.append(punto)
    return sy

def puntos_mas_cercanos_dyc(px, py):
    if len(px) <= 3:
        return comparacion_3(px)
    mitad = len(px) // 2
    qx = px[:mitad]
    rx = px[mitad:]
    qy, ry = construir_qyry(py, px[mitad][0])
    q0, q1 = puntos_mas_cercanos_dyc(qx, qy)
    r0, r1 = puntos_mas_cercanos_dyc(rx, ry)
    if distancia(q0, q1) < distancia(r0, r1):
        d = distancia(q0, q1)
        min0 = q0
        min1 = q1
    else:
        d = distancia(r0, r1)
        min0 = r0
        min1 = r1
    sy = construir_sy(py, px[mitad][0], d)
    for i in range(len(sy)):
        for j in range(i+1, min(i+16, len(sy))):
            if distancia(sy[i], sy[j]) < d:
                d = distancia(sy[i], sy[j])
                min0 = sy[i]
                min1 = sy[j]
    return min0, min1


def mas_cercanos(puntos):
    px = sorted(puntos, key=lambda p: p[0])
    py = sorted(puntos, key=lambda p: p[1])
    p0, p1 = puntos_mas_cercanos_dyc(px, py)
    return p0, p1


puntos = generar_puntos(32)
print(puntos)
p0, p1 = mas_cercanos(puntos)
print(p0, p1, distancia(p0, p1))
