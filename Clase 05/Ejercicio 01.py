"""
Ejercicio 4: Sumar Duraciones de Películas con Sobrecarga de Operadores
Enunciado:
Implementa una clase Pelicula que tenga los atributos titulo y duracion (en minutos).
Luego, sobrecarga el operador + (mediante el método __add__) para que puedas sumar
dos películas y obtener como resultado un nuevo objeto Pelicula, cuyo título sea la
concatenación de ambos títulos y su duración sea la suma de ambas.

Además, sobrecarga el método __str__ para que cuando se imprima un objeto de tipo
Pelicula, se muestre un mensaje legible con su título y duración.

Este ejercicio tiene como objetivo aplicar la sobrecarga de operadores, crear
objetos combinados y mejorar la representación textual de los objetos.
"""

class Pelicula:
    def __init__(self, titulo, duracion):
        self.titulo = titulo      # Nombre de la película
        self.duracion = duracion  # Duración en minutos

    def __add__(self, otra):
        """
        Sobrecarga del operador +.
        Si la otra es Pelicula, retorna nueva Pelicula con títulos concatenados
y suma de duraciones.
        """
        if not isinstance(otra, Pelicula):
            return NotImplemented
        nuevo_titulo = f"{self.titulo} + {otra.titulo}"
        total_min = self.duracion + otra.duracion
        return Pelicula(nuevo_titulo, total_min)

    def __str__(self):
        # Representación legible para print()
        return f"{self.titulo}: {self.duracion} min"

# Ejemplo de uso
p1 = Pelicula("Movie A", 120)
p2 = Pelicula("Movie B", 90)
p3 = p1 + p2           # Usa __add__
print(p3)              # Usa __str__: "Movie A + Movie B: 210 min"

"""
Preguntas y respuestas

¿Qué pasa al hacer p1 + 5?

Como 5 no es Pelicula, __add__ devuelve NotImplemented, resultando en TypeError.

¿Cómo modificar para que retorne sólo la suma de minutos (int)?

def __add__(self, otra):
    if isinstance(otra, Pelicula):
        return self.duracion + otra.duracion
    return NotImplemented

¿Por qué definimos __str__()?

Para mostrar información legible al imprimir el objeto; sin él, print(p1) mostraría su referencia de memoria.
"""