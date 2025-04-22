
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