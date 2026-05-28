---
lang: es
fontsize: 10pt
geometry: margin=1cm,top=1cm,bottom=1cm
math: true
---

# ¿Qué tan cierto es que todo lo que está en NP se puede reducir a un NP-Completo?

A veces surge, sea en clase, sea por slack, o sea por ustedes mismos sin siquiera llegar a consultarnos, la gran duda "es tan así que realmente se puede reducir cualquier problema que está en NP a un NP-Completo? No es una exageración?". Yendo más a una consulta particular que nos han hecho: 

> _Significa que todos los problemas NP siempre se pueden reducir a ese problema? Algo tan simple como la suma por ejemplo se puede terminar resolviendo (rebuscandosela) con vertex cover? O pasa que para ciertos problemas NP completos hay problemas NP "simples" que no se le puede reducir polinomialmente._

La respuesta es categórica: **TODO** problema en NP puede reducirse (polinomialmente) a un problema NP-Completo. 

Vamos a plantear el problema de la suma como un problema de decisión, y vamos a demostrar que el problema se puede reducir efectivamente a Vertex Cover (se podría usar otro problema, pero este fue el consultado). 

El problema de la suma lo podemos definir como: "Dados 3 valores `a`, `b` y `c`, ¿es cierto que `a + b = c`?". Vamos a suponer todos los valores positivos (se puede plantear también para negativos, y corregir algunas cosas, pero a la cuestión didáctica que vamos a estar viendo dudo que sea de valor meternos en ese terreno).

Creo que es medianamente evidente que este problema está en NP y vamos a saltear el validador (que no recibe una solución en sí... sino que directamente lo valida y ya). 

## Reducción propuesta

Vamos a reducir el problema de la suma al problema de Vertex Cover. 

1. Vamos a crear un grafo no dirigido **completo** de `a + b` vértices (lo cual nos consume $\mathcal{O}\left((a+b)^2\right)$.
2. Vamos a invocar a Vertex Cover con `c-1` y `c-2`. 

**Decimos entonces que**:

`a + b = c` $\iff$ Hay un Vertex Cover de a los sumo `c-1` vértices pero **no** hay uno de a lo sumo `c-2` vértices. 

Algo clave para las demostraciones es entender el grafo. Al ser completo, el vertex cover mínimo es de la cantidad de vértices - 1 (en nuestro caso, de `a + b - 1`). Si dejamos afuera a 2 vértices, la arista entre estos 2 (que existe, por ser completo) no va a estar cubierta. 

### `a + b = c` $\rightarrow$ Hay un Vertex Cover de a los sumo `c-1` vértices pero **no** hay uno de a lo sumo `c-2` vértices. 

Vamos a ver por método directo. Suponemos que, en efecto, `a + b = c`. Entonces, por la explicación dada antes, al buscar por un vertex cover de a lo sumo `c - 1` vértices estamos buscando un vertex cover de a lo sumo `a + b - 1` vértices. Este en efecto existe (todos los vértices salvo 1). 
Ahora similar, con `c - 2` equivale a buscar uno de a lo sumo `a + b - 2` vértices. Como ya dijimos antes, al ser completo no es posible encontrar un Vertex Cover de a lo sumo esa cantidad de vértices, porque estamos dejando afuera a al menos 2, y esos 2 tienen una arista entre sí no cubierta. 

### Hay un Vertex Cover de a los sumo `c-1` vértices pero **no** hay uno de a lo sumo `c-2` vértices $\rightarrow$ `a + b = c` 

Nuevamente, supongamos que en efecto tenemos un vertex cover de a lo sumo `c-1` pero no tenemos uno de a lo sumo `c-2`. Al ser un grafo completo, este salto se produce al pasar de buscar de `a + b - 1` a buscar con `a + b - 2`. No puede ser en otro coso. Si no encontramos un vertex cover de a lo sumo `c-1` vértices, es que `c` es necesariamente menor a `a+b`. Ahora bien, si encontramos, significa que `c` es al menos `a+b` (podría ser mayor). Por ejemplo, si `a = 1, b = 1, c = 1700`, va a ser cierto que vamos a encontrar un vertex cover de **a lo sumo** 1699 vértices (1, o 2, es, a lo sumo, 1699). Ahora bien, si no encontramos uno de `c-2`, significa que `c-1` es necesariamente menor a `a+b`, entonces si `c-1` es menor a `a+b`, pero `c` es al menos `a+b`, no queda otra a que `c = a+b`.

## Conclusión

En si no demostramos nada. Redujimos un problema en NP a uno NP-Completo, lo cual es (parte de) la definición de un problema NP-Completo. El punto fue partir de una pregunta que muchos pueden tener como "bueno, tampoco es que podés reducir una simple suma a Vertex Cover" y decir "sí, justamente, sí se puede". 

