
"""
Define una clase Libro con los métodos __str__ para representar
el libro como cadena y __len__ para obtener la cantidad de páginas.
Luego, crea dos clases derivadas Novela y Enciclopedia, donde cada
una sobrescriba estos métodos para adaptarlos a su contexto.
"""



# Definición de la clase base 'Libro'
class Libro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas

    def __str__(self):
        return f"Libro: {self.titulo}, {self.paginas} páginas"

    def __len__(self):
        return self.paginas

# Clase 'Novela' que hereda de 'Libro'
class Novela(Libro):
    def __str__(self):
        return f"Novela: {self.titulo}, {self.paginas} páginas"

# Clase 'Enciclopedia' que hereda de 'Libro'
class Enciclopedia(Libro):
    def __str__(self):
        return f"Enciclopedia: {self.titulo}, {self.paginas} páginas"

# Creación de instancias
novela = Novela("Cien años de soledad", 450)
enciclopedia = Enciclopedia("Enciclopedia Universal", 1200)

# Impresión de la representación de los libros
print(novela)  # "Novela: Cien años de soledad, 450 páginas"
print(enciclopedia)  # "Enciclopedia: Enciclopedia Universal, 1200 páginas"
print(len(enciclopedia))  # 1200

"""
Pregunta 1: ¿Cuál es el propósito del método __str__ en este código?
Respuesta: Definir cómo se representa un objeto Libro cuando se usa print(), haciendo que su salida sea más clara y detallada.
Pregunta 2: ¿Por qué Novela y Enciclopedia sobrescriben __str__?
Respuesta: Para personalizar el formato del libro según su categoría, diferenciando una novela de una enciclopedia.
Pregunta 3: ¿Cómo nos beneficia el uso de __len__?
Respuesta: Permite obtener la cantidad de páginas de un libro de manera directa con len(), mejorando la manipulación de objetos en el código.
"""
