"""
Crea un pequeño gestor de tareas que permita definir tareas simples y
tareas complejas mediante herencia múltiple.

Define una clase abstracta Tarea con el método abstracto ejecutar()
que no recibe parámetros.

Implementa dos subclases concretas:
TareaImprimir: recibe un mensaje y su ejecutar() imprime dicho mensaje.
TareaCalculo: recibe dos números y su ejecutar() imprime la suma.

Luego define TareaMixta que herede de ambas (TareaImprimir, TareaCalculo),
reciba mensaje, a y b, y cuyo ejecutar() primero imprima el mensaje y luego la suma.
Finalmente, maneja una lista de Tarea y recorre todas llamando a ejecutar().
"""

from abc import ABC, abstractmethod

# 1. Clase base abstracta
class Tarea(ABC):
    @abstractmethod
    def ejecutar(self):
        # Debe ser implementado por cada subclase
        pass

# 2a. Tarea que imprime un mensaje
class TareaImprimir(Tarea):
    def __init__(self, mensaje):
        self.mensaje = mensaje         # El texto a mostrar

    def ejecutar(self):
        print(self.mensaje)            # Imprime el mensaje

# 2b. Tarea que hace un cálculo
class TareaCalculo(Tarea):
    def __init__(self, a, b):
        self.a = a                     # Primer sumando
        self.b = b                     # Segundo sumando

    def ejecutar(self):
        resultado = self.a + self.b    # Suma de los dos números
        print("Resultado:", resultado) # Muestra el resultado

# 3. Herencia múltiple
class TareaMixta(TareaImprimir, TareaCalculo):
    def __init__(self, mensaje, a, b):
        # Inicializa ambas bases
        TareaImprimir.__init__(self, mensaje)
        TareaCalculo.__init__(self, a, b)

    def ejecutar(self):
        # Primero la parte de imprimir
        TareaImprimir.ejecutar(self)
        # Luego la parte de cálculo
        TareaCalculo.ejecutar(self)

# 4. Uso con lista de tareas
if __name__ == "__main__":
    tareas = [
        TareaImprimir("¡Hola, mundo!"),
        TareaCalculo(7, 5),
        TareaMixta("Comenzando mezcla:", 10, 20)
    ]
    for t in tareas:
        t.ejecutar()  # Polimorfismo: cada clase responde adecuadamente


"""
Pregunta 1
¿Por qué podemos almacenar instancias de TareaImprimir, TareaCalculo y TareaMixta en la misma lista y luego llamar a ejecutar() sin diferenciar el tipo?
Respuesta
Porque todas heredan de Tarea y implementan el mismo método ejecutar(). Python invoca la versión concreta correspondiente en cada objeto (polimorfismo).

Pregunta 2
¿Cómo invoca TareaMixta las implementaciones de sus dos padres en ejecutar()?
Respuesta
Llamando explícitamente a TareaImprimir.ejecutar(self) y luego a TareaCalculo.ejecutar(self), combinando ambas funcionalidades.

Pregunta 3
¿Qué pasaría si quitas la llamada a TareaCalculo.__init__ en el constructor de TareaMixta?
Respuesta
El atributo self.a y self.b nunca existirían, provocando un AttributeError al ejecutar la parte de cálculo.
"""