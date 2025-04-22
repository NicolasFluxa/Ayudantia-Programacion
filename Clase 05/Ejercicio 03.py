
"""
Ejercicio 6: Transporte Polimórfico con Duck Typing
Enunciado:
Define tres clases sin relación de herencia entre sí: Auto, Bicicleta y Avion.
Cada clase debe tener dos métodos con el mismo nombre: moverse() y detenerse(),
que deben mostrar un mensaje representativo del tipo de transporte.

Luego, implementa una función llamada simular_transporte(transporte) que reciba
cualquier objeto, verifique dinámicamente si tiene ambos métodos requeridos,
y si los tiene, los ejecute. Si el objeto no cumple con esta "interfaz implícita",
debe lanzar un error.

Este ejercicio tiene como objetivo aplicar el principio de duck typing de Python,
que permite tratar objetos por su comportamiento en lugar de su tipo explícito.
También se introducen verificaciones con hasattr() para asegurar que los objetos
cumplen con la interfaz esperada.
"""


class Auto:
    def moverse(self):
        print("El auto se desplaza por carretera.")
    def detenerse(self):
        print("El auto se frena y se detiene.")

class Bicicleta:
    def moverse(self):
        print("La bicicleta avanza pedaleando.")
    def detenerse(self):
        print("La bicicleta frena con las zapatas.")

class Avion:
    def moverse(self):
        print("El avión despega y vuela por el aire.")
    def detenerse(self):
        print("El avión aterriza y frena en pista.")

# Función genérica que utiliza duck typing
def simular_transporte(transporte):
    if not all(hasattr(transporte, m) for m in ("moverse", "detenerse")):
        raise TypeError("El objeto no implementa moverse() y detenerse()")
    transporte.moverse()
    transporte.detenerse()

# Pruebas
for veh in (Auto(), Bicicleta(), Avion()):
    simular_transporte(veh)
    print("—" * 30)


"""

Preguntas y respuestas

¿Por qué no necesitan heredar de la misma clase?

Gracias al duck typing, basta con que tengan los métodos esperados.

¿Qué pasa si Barco sólo define moverse()?

Al llamar detenerse(), se lanza TypeError por la verificación del hasattr.

¿Cómo verificar que tiene ambos métodos antes de usarlos?

Usamos all(hasattr(transporte, m) for m in ("moverse","detenerse")).
"""