
"""
Crea una clase base Figura con un método calcular_area(). Luego, define dos clases derivadas:
Cuadrado y Circulo, que sobrescriban el método para calcular el área de cada figura.
Este ejercicio mostrará cómo distintos objetos pueden compartir la
misma interfaz pero con diferentes implementaciones.
"""
import math


# Definición de la clase base 'Figura'
class Figura:
    def calcular_area(self):
        # Método que será sobreescrito por las subclases
        raise NotImplementedError("Este método debe ser implementado por una subclase")


# Clase 'Cuadrado' que hereda de 'Figura'
class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado  # Atributo que almacena el lado del cuadrado

    def calcular_area(self):
        # Sobreescritura del método para calcular el área de un cuadrado
        return self.lado ** 2


# Clase 'Circulo' que hereda de 'Figura'
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio  # Atributo que almacena el radio del círculo

    def calcular_area(self):
        # Sobreescritura del método para calcular el área de un círculo
        return math.pi * (self.radio ** 2)


# Creación de instancias de figuras
cuadrado = Cuadrado(4)
circulo = Circulo(3)

# Impresión del área de cada figura
print(f"Área del cuadrado: {cuadrado.calcular_area()}")  # 16
print(f"Área del círculo: {circulo.calcular_area()}")  # 28.27...

"""
Pregunta 1: ¿Por qué Figura tiene el método calcular_area() sin implementación?
Respuesta: Porque es una clase base y solo define una interfaz común. 
La implementación debe ser proporcionada por sus subclases.
Pregunta 2: ¿Por qué las clases Cuadrado y Circulo sobrescriben el método calcular_area()?
Respuesta: Para adaptar la funcionalidad a cada figura geométrica y calcular su área correctamente.
Pregunta 3: ¿Qué sucede si intentamos crear una instancia de Figura y llamar calcular_area()?
Respuesta: Se generará un error porque la clase base no proporciona una implementación válida del método.
"""

