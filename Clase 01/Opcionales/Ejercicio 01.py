"""
Ejercicio 1: Clase Libro
Instrucciones:

Crea una clase Libro con atributos privados _titulo y _autor.

Implementa métodos get_titulo(), get_autor(), set_titulo(), set_autor().

En set_titulo(), asegúrate de que el título no supere 50 caracteres.
"""


class Libro:
    def __init__(self, titulo, autor):
        self._titulo = titulo
        self._autor = autor

    def get_titulo(self):
        return self._titulo

    def set_titulo(self, nuevo_titulo):
        # Limita el título a 50 caracteres
        if len(nuevo_titulo) > 50:
            self._titulo = nuevo_titulo[:50]
        else:
            self._titulo = nuevo_titulo

    def get_autor(self):
        return self._autor

    def set_autor(self, nuevo_autor):
        self._autor = nuevo_autor



"""
¿Qué pasa si no limitamos la longitud del título?

Si no limitamos la longitud, podríamos tener títulos excesivamente largos que dificulten su uso en bases de datos,
interfaces gráficas o impresiones. Validar la longitud asegura que los datos sean manejables y estéticamente agradables.

¿Cómo podríamos validar que el autor solo contenga letras y espacios?

Podríamos usar expresiones regulares para asegurarnos de que el atributo autor solo 
incluya caracteres alfabéticos y espacios. Ejemplo:

import re
def validar_autor(autor):
    if re.match("^[a-zA-Z\s]+$", autor):
        return True
    else:
        return False

"""