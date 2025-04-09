"""
Define una clase Empleado con un método calcular_salario().
Luego, crea dos clases derivadas Gerente y Desarrollador,
cada una con su propia forma de calcular el salario.
Este ejercicio demuestra cómo cada rol tiene una implementación
diferente del mismo método.
"""


# Definición de la clase base 'Empleado'
class Empleado:
    def calcular_salario(self):
        raise NotImplementedError("Este método debe ser implementado en una subclase")

# Clase 'Gerente' que hereda de 'Empleado'
class Gerente(Empleado):
    def calcular_salario(self):
        return "Salario base más bonificaciones: $5000"

# Clase 'Desarrollador' que hereda de 'Empleado'
class Desarrollador(Empleado):
    def calcular_salario(self):
        return "Salario base más horas extras: $3500"

# Creación de instancias de empleados
gerente = Gerente()
desarrollador = Desarrollador()

# Impresión del salario de cada empleado
print(gerente.calcular_salario())  # $5000
print(desarrollador.calcular_salario())  # $3500

"""
Pregunta 1: ¿Por qué calcular_salario() es diferente en Gerente y Desarrollador?
Respuesta: Porque cada tipo de empleado tiene una forma distinta de calcular su salario.
Pregunta 2: ¿Cómo facilita el polimorfismo la gestión de diferentes tipos de empleados?
Respuesta: Permite que distintas clases respondan de manera única a la misma llamada 
de método sin cambiar la interfaz común.
Pregunta 3: ¿Qué sucedería si agregamos una nueva clase Freelancer con una implementación propia de calcular_salario()?
Respuesta: Se integraría perfectamente, sin modificar las demás clases, manteniendo el polimorfismo.
"""
