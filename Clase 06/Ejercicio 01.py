
"""
Define una clase Animal con el método especial __str__,
que permite representar a los animales como cadena de texto.
Luego, crea dos clases derivadas Perro y Pez, cada una con su
propia versión de __str__. Este ejercicio demuestra cómo el polimorfismo
se puede aplicar a métodos especiales de Python.
"""


# Definición de la clase base 'Animal'
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f"Animal: {self.nombre}"

# Clase 'Perro' que hereda de 'Animal'
class Perro(Animal):
    def __str__(self):
        return f"Perro: {self.nombre}, hace 'Guau!'"

# Clase 'Pez' que hereda de 'Animal'
class Pez(Animal):
    def __str__(self):
        return f"Pez: {self.nombre}, vive en el agua."

# Creación de instancias
perro = Perro("Rex")
pez = Pez("Nemo")

# Uso del método especial __str__
print(perro)  # "Perro: Rex, hace 'Guau!'"
print(pez)  # "Pez: Nemo, vive en el agua."

"""
Pregunta 1: ¿Cuál es la ventaja de sobrescribir __str__ en estas clases?
Respuesta: Permite que la representación de los objetos sea más clara y adaptada a su naturaleza cuando se usa print().
Pregunta 2: ¿Qué pasaría si Pez no sobrescribe __str__?
Respuesta: Se usaría la versión de Animal, mostrando solo "Animal: Nemo", sin información específica del pez.
Pregunta 3: ¿Cómo podríamos extender esta clase para incluir más tipos de animales con diferentes características?
Respuesta: Simplemente creando nuevas clases que hereden de Animal y sobrescriban __str__.
"""

