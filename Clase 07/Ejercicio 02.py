
"""
Implementa una jerarquía de vehículos usando herencia.
Crea una clase Vehiculo con atributos marca y modelo, y un método descripcion() que retorne una cadena.
Luego define dos subclases:

Auto: añade atributo puertas y extiende descripcion() para incluirlo.

Camion: añade atributo capacidad_toneladas y extiende descripcion().

Utiliza super() para reutilizar la implementación del método padre.

"""

# Clase base
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca                   # Marca del vehículo
        self.modelo = modelo                 # Modelo del vehículo

    def descripcion(self):
        return f"{self.marca} {self.modelo}" # Descripción base

# Subclase Auto
class Auto(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)      # Inicializa marca y modelo
        self.puertas = puertas               # Añade puertas

    def descripcion(self):
        base = super().descripcion()         # Llama a la versión padre
        return f"{base}, {self.puertas} puertas"

# Subclase Camion
class Camion(Vehiculo):
    def __init__(self, marca, modelo, capacidad_toneladas):
        super().__init__(marca, modelo)
        self.capacidad_toneladas = capacidad_toneladas

    def descripcion(self):
        base = super().descripcion()
        return f"{base}, capacidad: {self.capacidad_toneladas} t"

# Ejemplo de uso
a = Auto("Toyota", "Corolla", 4)
c = Camion("Volvo", "FH16", 18)
print(a.descripcion())  # Toyota Corolla, 4 puertas
print(c.descripcion())  # Volvo FH16, capacidad: 18 t


"""
Pregunta 1
¿Por qué usamos super().__init__() en las subclases?
Respuesta
Para reutilizar la lógica de inicialización de la clase padre (Vehiculo) y evitar duplicarla.

Pregunta 2
¿Qué pasaría si Auto.descripcion() no llama a super().descripcion()?
Respuesta
La descripción base (marca y modelo) no aparecería, solo veríamos "X puertas".

Pregunta 3
¿Cómo crearías otra subclase Motocicleta con atributo cilindrada?

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada

    def descripcion(self):
        return f"{super().descripcion()}, {self.cilindrada}cc"

"""