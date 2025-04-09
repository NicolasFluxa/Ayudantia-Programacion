

"""
Define una clase Vehiculo con atributos marca y modelo,
y sobrescribe el método especial __eq__ para comparar si
dos vehículos son iguales. Luego, crea dos instancias y prueba
la comparación. Este ejercicio muestra cómo el polimorfismo se
puede aplicar en métodos de comparación.
"""



# Definición de la clase base 'Vehiculo'
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def __eq__(self, otro):
        # Sobreescritura del método de comparación
        return self.marca == otro.marca and self.modelo == otro.modelo

# Creación de instancias
auto1 = Vehiculo("Toyota", "Corolla")
auto2 = Vehiculo("Toyota", "Corolla")
auto3 = Vehiculo("Ford", "Focus")

# Comparación de vehículos
print(auto1 == auto2)  # True (Son iguales)
print(auto1 == auto3)  # False (Son diferentes)

"""
Pregunta 1: ¿Cuál es la función del método especial __eq__ en este código?
Respuesta: Define una forma personalizada de comparar objetos Vehiculo,
en lugar de la comparación predeterminada de Python.
Pregunta 2: ¿Por qué auto1 == auto2 devuelve True?
Respuesta: Porque ambos tienen la misma marca y modelo, cumpliendo la condición establecida en __eq__.
Pregunta 3: ¿Cómo podríamos extender esta comparación para incluir más atributos como el año de fabricación?
Respuesta: Modificando __eq__ para incluir self.año == otro.año como condición en la comparación.
"""
