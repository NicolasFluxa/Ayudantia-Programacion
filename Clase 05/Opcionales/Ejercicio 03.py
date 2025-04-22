
"""
Ejercicio 3: Análisis de Calificaciones con Listas
Enunciado:
Crea un programa que utilice listas para almacenar calificaciones de estudiantes
y realizar operaciones básicas sobre ellas.
Debes seguir estos pasos:

Inicializa una lista con varias calificaciones numéricas (enteros entre 0 y 100).

Calcula y muestra:

El promedio de las calificaciones.

La calificación más alta.

La calificación más baja.

Agrega una nueva calificación a la lista.

Elimina la primera calificación que esté por debajo de 60 (nota desaprobatoria).

Ordena la lista en orden descendente (de mayor a menor).

Este ejercicio tiene como propósito practicar el manejo de listas, uso de
funciones como append, remove, sort, y recorrer listas usando ciclos.
"""


# Lista inicial de calificaciones
calificaciones = [78, 92, 85, 67, 90, 55, 88]

# Estadísticas básicas
promedio = sum(calificaciones) / len(calificaciones)
maxima = max(calificaciones)
minima = min(calificaciones)
print(f"Promedio: {promedio:.2f}")
print(f"Calificación más alta: {maxima}")
print(f"Calificación más baja: {minima}")

# Agregar nueva nota y remover primer suspenso (<60)
calificaciones.append(73)
print("Después de append:", calificaciones)
for nota in calificaciones:
    if nota < 60:
        calificaciones.remove(nota)
        break  # Evitar errores al modificar durante la iteración
print("Después de remove:", calificaciones)

# Ordenar de mayor a menor
calificaciones.sort(reverse=True)
print("Ordenadas desc:", calificaciones)

"""
Preguntas y respuestas

¿Por qué se usa break tras remove()?

Para salir inmediatamente y no continuar iterando con la lista modificada.

¿Qué haría pop(0) en lugar de remove(nota)?

Eliminaría el elemento en índice 0 sin chequear su valor.

¿Cómo ordenar de mayor a menor?

Usando calificaciones.sort(reverse=True).
"""