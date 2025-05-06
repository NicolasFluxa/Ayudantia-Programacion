
"""
Enunciado
Crea un sistema de operaciones aritméticas usando polimorfismo.
Define una clase abstracta Operacion con un método ejecutar(a, b)
que retorne el resultado. Luego implementa dos subclases:

Suma: implementa ejecutar(a, b) devolviendo a + b.

Multiplicacion: implementa ejecutar(a, b) devolviendo a * b.

Por último, escribe una función aplicar(operacion, a, b) que reciba
cualquier instancia de Operacion y llame a su método ejecutar.

"""


from abc import ABC, abstractmethod

# Clase base abstracta
class Operacion(ABC):
    @abstractmethod
    def ejecutar(self, a, b):
        # Método que debe implementar cada operación
        pass

# Suma hereda de Operacion
class Suma(Operacion):
    def ejecutar(self, a, b):
        return a + b  # Retorna la suma

# Multiplicacion hereda de Operacion
class Multiplicacion(Operacion):
    def ejecutar(self, a, b):
        return a * b  # Retorna el producto

class Division(Operacion):
    def ejecutar(self, a, b):
        if b == 0:
            pass
        else:
            return a / b

class Resta(Operacion):
    def ejecutar(self, a, b):
        return a - b

class Elevado(Operacion):
    def ejecutar(self, a, b):
        return a ** b

# Función que demuestra polimorfismo
def aplicar(operacion, a, b):
    return operacion.ejecutar(a, b)

# Ejemplo de uso
op1 = Suma()
op2 = Multiplicacion()
op3 = Division()
op4 = Resta()
op5 = Elevado()

print(aplicar(op1, 3, 5))         # 8
print(aplicar(op2, 3, 5))         # 15
print(aplicar(op3, 10, 5))        # 2.0
print(aplicar(op3, 10, 0))        # Error: No se puede dividir por cero.
print(aplicar(op4, 10, 5))        # 5
print(aplicar(op5, 2, 2))         # 4

"""
Pregunta 1
¿Qué ocurriría si llamas aplicar(Operacion(), 2, 3)?
Respuesta
Daría un TypeError al instanciar Operacion(), pues tiene método @abstractmethod sin implementar.

Pregunta 2
¿Por qué aplicar(op1, a, b) funciona igual para Suma y Multiplicacion?
Respuesta
Porque ambas subclases comparten la misma interfaz ejecutar(a, b), ilustrando polimorfismo.

Pregunta 3
¿Cómo cambiarías Multiplicacion para que devuelva a * b * 2 sin tocar Suma ni aplicar?

def ejecutar(self, a, b):
    return a * b * 2

"""