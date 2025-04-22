from abc import ABC, abstractmethod

"""
Ejercicio 2: Catálogo de Productos con Clases Abstractas
Enunciado:
Implementa un sistema de catálogo de productos aplicando abstracción y polimorfismo.
Crea una clase abstracta llamada Producto que contenga un método obligatorio mostrar_info(
 que deberá ser implementado por todas sus subclases.

Luego, define tres tipos de productos que hereden de Producto:

Libro (atributos: titulo, autor, precio)

VideoJuego (atributos: nombre, consola, precio)

Pelicula (atributos: nombre, director, precio)

Cada tipo de producto debe implementar el método mostrar_info() para mostrar 
su información de forma personalizada.

Crea una lista con objetos de diferentes tipos y recórrela mostrando la 
información de cada producto. También calcula el total acumulado del precio 
de todos los productos del catálogo.
"""


# Clase base abstracta que obliga a mostrar_info en todas las subclases
class Producto(ABC):
    @abstractmethod
    def mostrar_info(self):
        """Imprime los detalles del producto."""
        pass

class Libro(Producto):
    def __init__(self, titulo, autor, precio):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio

    def mostrar_info(self):
        print(f"Libro: '{self.titulo}' de {self.autor} - ${self.precio:.2f}")

class VideoJuego(Producto):
    def __init__(self, nombre, consola, precio):
        self.nombre = nombre
        self.consola = consola
        self.precio = precio

    def mostrar_info(self):
        print(f"Videojuego: '{self.nombre}' para {self.consola} - ${self.precio:.2f}")

class Pelicula(Producto):
    def __init__(self, nombre, director, precio):
        self.nombre = nombre
        self.director = director
        self.precio = precio

    def mostrar_info(self):
        print(f"Película: '{self.nombre}' dirigida por {self.director} - ${self.precio:.2f}")

# Crear catálogo mixto
catalogo = [
    Libro("1984", "George Orwell", 12.99),
    VideoJuego("Zelda: Breath of the Wild", "Switch", 59.99),
    Pelicula("Inception", "Christopher Nolan", 14.50)
]

# Mostrar info y calcular total
total = 0
for prod in catalogo:
    prod.mostrar_info()  # Llamada polimórfica
    total += prod.precio
print(f"Total del catálogo: ${total:.2f}")

"""
Preguntas y respuestas

¿Qué permite llamar mostrar_info() sin conocer el tipo de prod?

El polimorfismo junto a la abstracción impuesta por @abstractmethod.

Si creas class Album(Producto), ¿qué debes implementar?

El método mostrar_info(self).

¿Cómo se calcula el total del catálogo?

Iterando con for y acumulando prod.precio en una variable total.
"""