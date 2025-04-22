from abc import ABC, abstractmethod

"""
Enunciado:
Desarrolla un sistema de gestión de empleados utilizando los conceptos de programación orientada a objetos,
específicamente herencia, abstracción y polimorfismo.
Debes crear una clase abstracta llamada Empleado, que incluya el atributo nombre 
y un método abstracto calcular_sueldo().
Luego, define dos subclases:

EmpleadoFijo: representa empleados con un sueldo mensual fijo.

EmpleadoPorHoras: representa empleados cuyo sueldo se calcula en base a la cantidad
de horas trabajadas y el valor por hora. Además, estos empleados reciben un bono fijo de $50.

Llena una lista con instancias de ambas clases y recorre dicha lista llamando al 
método calcular_sueldo() para mostrar el sueldo de cada empleado, sin necesidad de diferenciar entre tipos concretos.
Esto permitirá observar cómo el polimorfismo funciona al usar una misma interfaz para distintos tipos de empleados.
"""

# Clase base abstracta que define la interfaz de Empleado
class Empleado(ABC):
    def __init__(self, nombre):
        self.nombre = nombre  # Nombre del empleado

    @abstractmethod
    def calcular_sueldo(self):
        """
        Método abstracto: debe ser implementado por todas las subclases.
        Retorna el sueldo calculado.
        """
        pass

# Empleado con salario fijo mensual
class EmpleadoFijo(Empleado):
    def __init__(self, nombre, sueldo_base):
        super().__init__(nombre)
        self.sueldo_base = sueldo_base  # Sueldo mensual fijo

    def calcular_sueldo(self):
        # Simplemente retorna el sueldo base
        return self.sueldo_base

# Empleado que cobra por horas trabajadas
class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, horas_trabajadas, valor_por_hora):
        super().__init__(nombre)
        self.horas_trabajadas = horas_trabajadas  # Horas trabajadas en el período
        self.valor_por_hora = valor_por_hora      # Pago por cada hora

    def calcular_sueldo(self):
        # Calcula sueldo según horas y añade un bono fijo de $50
        return (self.horas_trabajadas * self.valor_por_hora) + 50

# Instanciar empleados variados
empleados = [
    EmpleadoFijo("ana",2000),
    EmpleadoPorHoras("Luis", 40, 15),
    EmpleadoFijo("María", 1500),
    EmpleadoPorHoras("Carlos", 30, 20)
]

# Mostrar el sueldo de cada empleado usando la misma interfaz
for emp in empleados:
    print(f"{emp.nombre}: ${emp.calcular_sueldo():.2f}")



"""
Preguntas y respuestas

¿Qué pasaría si intentas instanciar directamente Empleado("Paco")?

Se lanzaría un TypeError indicando que no se pueden instanciar clases 
con métodos abstractos sin implementar (calcular_sueldo).

¿Por qué emp.calcular_sueldo() funciona igual para EmpleadoFijo y EmpleadoPorHoras?

Porque gracias a la abstracción y el polimorfismo ambas subclases implementan 
la misma interfaz calcular_sueldo(), permitiendo al cliente no diferenciar el tipo concreto.

¿Cómo modifica el código el bono fijo de $50 en EmpleadoPorHoras y por qué?

Se añade + 50 al resultado de horas * valor por hora dentro de calcular_sueldo().
El bono fija asegura un ingreso mínimo.


"""