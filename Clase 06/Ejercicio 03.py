
"""
Define una clase abstracta Empleado con un método calcular_bono().
Luego, crea dos clases derivadas Gerente y Desarrollador, donde cada
una sobrescriba el método según su política de bonos. Este ejercicio
demuestra cómo estructurar un sistema de empleados con polimorfismo.
"""

from abc import ABC, abstractmethod

# Definición de la clase abstracta 'Empleado'
class Empleado(ABC):
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    @abstractmethod
    def calcular_bono(self):
        pass

# Clase 'Gerente' que hereda de 'Empleado'
class Gerente(Empleado):
    def calcular_bono(self):
        return self.salario * 0.20  # 20% de bono

# Clase 'Desarrollador' que hereda de 'Empleado'
class Desarrollador(Empleado):
    def calcular_bono(self):
        return self.salario * 0.10  # 10% de bono

# Creación de instancias
gerente = Gerente("Laura", 5000)
desarrollador = Desarrollador("Carlos", 3500)

# Impresión de los bonos
print(f"Bono de {gerente.nombre}: ${gerente.calcular_bono()}")
print(f"Bono de {desarrollador.nombre}: ${desarrollador.calcular_bono()}")


"""
Pregunta 1: ¿Por qué Empleado es una clase abstracta en este caso?
Respuesta: Para definir una estructura común y forzar la implementación
de calcular_bono() en todas las clases derivadas.
Pregunta 2: ¿Cómo refleja este ejercicio el concepto de polimorfismo?
Respuesta: Aunque Gerente y Desarrollador tienen la misma interfaz,
cada uno implementa calcular_bono() de manera diferente.
Pregunta 3: ¿Cómo podríamos agregar más roles de empleados sin modificar la clase Empleado?
Respuesta: Creando nuevas clases que hereden de Empleado y sobrescriban
calcular_bono() con su propia lógica.
"""
