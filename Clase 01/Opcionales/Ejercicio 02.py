"""
Ejercicio : Clase Coche
Instrucciones:

Define una clase Coche con _velocidad (inicial 0).

Agrega un método acelerar(incremento) que aumente _velocidad solo si el incremento es positivo.

Crea un método frenar(decremento) que reduzca _velocidad, pero nunca por debajo de 0.
"""

class Coche:
    def __init__(self):
        self._velocidad = 0

    def get_velocidad(self):
        return self._velocidad

    def acelerar(self, incremento):
        # Solo aumenta si el incremento es positivo
        if incremento > 0:
            self._velocidad += incremento

    def frenar(self, decremento):
        # Reduce la velocidad sin caer debajo de 0
        self._velocidad = max(0, self._velocidad - decremento)


mi_coche = Coche()
mi_coche.acelerar(30)
print(mi_coche.get_velocidad())  # 30
mi_coche.frenar(40)
print(mi_coche.get_velocidad())  # 0



"""
¿Qué pasa si no validamos que el incremento sea positivo?

Sin validación, podríamos permitir valores negativos en el método para acelerar, lo que reduciría la velocidad del coche en lugar de incrementarla. Esto sería ilógico y podría causar errores en sistemas que dependen de la velocidad positiva.

¿Cómo podríamos agregar un límite máximo de velocidad?

Podríamos añadir una constante para la velocidad máxima y validarla en el método acelerar. Ejemplo:
MAX_VELOCIDAD = 120
def acelerar(self, incremento):
    nueva_velocidad = self.velocidad + incremento
    if nueva_velocidad <= MAX_VELOCIDAD:
        self.velocidad = nueva_velocidad
    else:
        print("Velocidad máxima alcanzada.")

"""