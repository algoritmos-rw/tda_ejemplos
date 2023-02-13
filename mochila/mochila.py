import random
import sys
import greedy
import pd


def main(n, W):
    elementos = [(random.randint(1, 100), random.randint(1, W)) for _ in range(n)]
    print("Solucion por Algoritmo Greedy maximizando valor:",
          greedy.mochila_greedy(elementos, W, greedy.ordenar_por_mayor_valor))
    print("Solucion por Algoritmo Greedy minimizando peso:",
          greedy.mochila_greedy(elementos, W, greedy.ordenar_por_menor_peso))
    print("Solucion por Algoritmo Greedy maximizando v/w:",
          greedy.mochila_greedy(elementos, W, greedy.ordenar_por_mayor_relacion_valor_peso))
    print("Solucion exacta:", pd.mochila_pd(elementos, W))


if __name__ == "__main__":
    if len(sys.argv) > 2:
        n = int(sys.argv[1])
        w = int(sys.argv[2])
    else:
        n = 100
        w = 100
    main(n, w)
