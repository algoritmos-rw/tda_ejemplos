---
lang: es
fontsize: 10pt
geometry: margin=1cm,top=1cm,bottom=1cm
math: true
---

# Problema de inflación

Tenemos unos productos dados por un arreglo $R$, donde $R[i]$ nos dice el precio del producto (todos mayores o iguales a 1). Cada día debemos comprar uno (y sólo uno) de los productos, pero vivimos en una era de inflación y los precios aumentan todo el tiempo. 
El precio del producto $i$ el día $j$ es $R[i]^{j + 1}$ ($j$ comenzando en 0). 
Implementar un algoritmo greedy que nos indique el precio mínimo al que podemos comprar todos los productos.

Este ejercicio es uno que resolvemos rápido. Somos buenos manejando esta situación. Expertos, podríamos decir, de las compras con inflación. Dado un día, compramos el más caro de los productos que nos faltan comprar. 

¿Es greedy? totalmente. Dado un día, elegimos el más caro (regla greedy). ¿Cuál es el óptimo local? Obtener ahora el más caro reduce cuánto va a costar en total este elemento, y al ser el más caro, exponenciarlo por algo más grande nos perjudica más, así que lo compramos lo antes posible para que esto suceda lo mínimo posible. 

¿Es óptimo? Si!

Podemos demostrarlo por inversiones: supongamos que tenemos una solución que tenga al menos una inversión (planteándolo al revés). Es decir, que exista un producto que compramos en el día $i$ y otro en el día $i+1$, y que le del día $i$ sea más barato. Es decir, $A < B$, siendo $A$ el valor de compra del valor $i$ y $B$ el de la siguiente. Entonces tenemos que la suma que estos dos aportan es $A^i + B^{i+1}$. Proponemos invertir esta compra, y que se haga al revés, con lo cual el costo que tendríamos sería $B^i + A^{i+1}$. ¿Podemos asegurar que alguno sea menor? Necesariamente el segundo. Si $A < B \rightarrow A^i < B^i$. 

Planteamos: 
$B^i + A^{i+1} < B^{i+1} + A^i \rightarrow B^i (B-1) > A^i (A-1)$. 
Recordamos lo que dijimos antes: $A^i < B^i$, y además $B > A \rightarrow B - 1 > A -1$, ambos términos de las multiplicaciones de la izquierda son superiores a los correspondientes de la derecha, entonces esa inecuación es cierta para cualquier valor de $A$ y $B$ y también de $i$. Entonces dar vuelta la compra es beneficioso. Aplicamos esto por cada vez que nos topamos con estas inversiones, entonces mejoramos en cada caso. Es decir, ¿mejoramos el óptimo? Imposible. _Absurdo_. Es decir, que no podían existir las inversiones desde el inicio. Es decir, no podía existir esta situación que planteamos. Necesariamente en la solución óptima no existe ningún caso donde un valor sea inferior a su siguiente, con lo cual la solución propuesta por nuestro algoritmo no es solo óptima, sino _la_ óptima (solo equiparable a otra con alguna variación en productos de mismo precio). 




