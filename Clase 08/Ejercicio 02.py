"""
Enunciado
Diseña un gestor de tareas combinando herencia múltiple, listas y manejo de errores.

Crea una clase abstracta Tarea con método ejecutar() (sin decoradores salvo @abstractmethod).

Implementa TareaImprimir(mensaje) y TareaCalculo(a, b) que hereden de Tarea.

Define TareaMixta que herede de ambas, reciba (mensaje, a, b), e implemente ejecutar() llamando primero a imprimir y luego al cálculo.

En la clase Gestor, mantiene una lista de tareas, con métodos agregar(tarea) y ejecutar_todas() que recorra y llame ejecutar() en cada tarea dentro de un bloque try/except, capturando cualquier excepción para que no detenga las demás.
"""

from abc import ABC, abstractmethod

# 1. Clase base abstracta
class Tarea(ABC):
    @abstractmethod
    def ejecutar(self):
        pass  # Deben implementarlo las subclases

# 2a. Tarea que imprime un mensaje
class TareaImprimir(Tarea):
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def ejecutar(self):
        print(self.mensaje)  # Muestra el texto

# 2b. Tarea que suma dos números
class TareaCalculo(Tarea):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def ejecutar(self):
        resultado = self.a + self.b
        print(f"Resultado: {resultado}")

# 3. Herencia múltiple
class TareaMixta(TareaImprimir, TareaCalculo):
    def __init__(self, mensaje, a, b):
        TareaImprimir.__init__(self, mensaje)
        TareaCalculo.__init__(self, a, b)

    def ejecutar(self):
        TareaImprimir.ejecutar(self)
        TareaCalculo.ejecutar(self)

# 4. Gestor de tareas con manejo de errores
class Gestor:
    def __init__(self):
        self.tareas = []  # Lista de Tarea

    def agregar(self, tarea):
        self.tareas.append(tarea)

    def ejecutar_todas(self):
        for t in self.tareas:
            try:
                t.ejecutar()
            except Exception as e:
                print(f"Error en tarea {t.__class__.__name__}: {e}")
        print("Ejecución de todas las tareas finalizada.")

# Prueba de uso
if __name__ == "__main__":
    gestor = Gestor()
    gestor.agregar(TareaImprimir("¡Hola!"))
    gestor.agregar(TareaCalculo(5, 7))
    # Intencional: tarea con error (string + número)
    gestor.agregar(TareaCalculo("cinco", 3))
    gestor.agregar(TareaMixta("Comienzo mixto:", 10, 20))
    gestor.ejecutar_todas()


"""
Pregunta 1
¿Por qué la tercera tarea no detiene la ejecución de las demás al generar un error?
Respuesta
Porque en ejecutar_todas() cada t.ejecutar() está dentro de un try/except, que captura la excepción e imprime el error, permitiendo continuar.

Pregunta 2
¿Cómo combina TareaMixta las funcionalidades de las dos clases padres?
Respuesta
Hereda de ambas y en su ejecutar() llama primero TareaImprimir.ejecutar(self) y luego TareaCalculo.ejecutar(self).

Pregunta 3
¿Qué pasaría si en Gestor.ejecutar_todas() quitamos el bloque try/except?
Respuesta
La primera excepción abortaría el bucle y las tareas siguientes no se ejecutarían.
"""
