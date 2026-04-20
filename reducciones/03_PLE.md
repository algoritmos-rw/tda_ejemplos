---
lang: es
fontsize: 10pt
geometry: margin=1cm,top=1cm,bottom=1cm
math: true
---

# Programación Lineal Entera es NP-Completo

En este caso no estamos buscando un valor óptimo (no es problema de optimización sino de decisión) así que el funcional lo obviamos, solo nos importa que se cumplan las restricciones. 

## Validador

```python
def es_ple_correcto(variables, inecuaciones, valores_propuestos):
	for v in variables:
		if v not in valores_propuestos:
			return False
		v.asignar_valor(valores_propuestos[v])
	for inec in inecuaciones:
		if not inec.es_valida(variables):
			return False
	return True
```

En resumen, vamos por cada inecuación validando si con los valores de variables asignados llegamos a que todas las restricciones sean correctos. 

## Reducción propuesta

Podríamos utilizar varios de los problemas NP-Completos que ya vimos. Por simplificación vamos a utilizar Independent Set. Dejamos al lector revisar cómo planteábamos el modelo de IS en Programación lineal entera. 

**Decimos entonces que**:

El grafo tiene un IS de al menos K vértices $\iff$ El modelo de PLE definido tiene solución

### El grafo tiene un IS de al menos K vértices $\rightarrow$ El modelo de PLE definido tiene solución

Nuevamente, método directo. Tenemos nuestro IS de al menos K vértices. Entonces definimos que las variables binarias del modelo que corresponden a dichos vértices tengan valor 1, y las demás 0. 
Podemos notar que el modelo es compatible, por lo que hay solución al modelo de PLE. 

### El modelo de PLE definido tiene solución $\rightarrow$  El grafo tiene un IS de al menos K vértices

Lo mismo al revés. Si el modelo tiene solución, seleccionamos los vértices cuyas variables tienen valor 1 en la solución. Deben ser al menos K porque sino el modelo no habría encontrado solución. Esos K tienen que cumplir las otras restricciones, por lo que los vértices seleccionados conforman un Independent Set. 

## Conclusión

Con estos breves pasos, demostramos que Programación Lineal Entera es un problema NP-Completo. Notar que, justamente, si hubiera una forma de resolver el problema de PLE en tiempo polinomial, IS (y todos los demás problemas NP-Completos) serían resolubles en tiempo polinomial justamente. 

