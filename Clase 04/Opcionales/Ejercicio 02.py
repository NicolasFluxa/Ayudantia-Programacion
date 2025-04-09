"""
Crea una clase Vehiculo con un método obtener_velocidad_maxima().
Luego, define dos clases derivadas Coche y Bicicleta, cada una
con su propia implementación del método. Este ejemplo demuestra
cómo distintos tipos de vehículos pueden compartir la misma interfaz
de método pero con valores específicos.
"""

# Definición de la clase base 'Vehiculo'
class Vehiculo:
    def obtener_velocidad_maxima(self):
        raise NotImplementedError("Este método debe ser implementado en una subclase")

# Clase 'Coche' que hereda de 'Vehiculo'
class Coche(Vehiculo):
    def obtener_velocidad_maxima(self):
        return "Velocidad máxima: 200 km/h"

# Clase 'Bicicleta' que hereda de 'Vehiculo'
class Bicicleta(Vehiculo):
    def obtener_velocidad_maxima(self):
        return "Velocidad máxima: 25 km/h"

# Creación de instancias de vehículos
coche = Coche()
bicicleta = Bicicleta()

# Llamadas al método polimórfico
print(coche.obtener_velocidad_maxima())  # 200 km/h
print(bicicleta.obtener_velocidad_maxima())  # 25 km/h


"""
Pregunta 1: ¿Qué ventaja tiene definir obtener_velocidad_maxima() en la clase Vehiculo?
Respuesta: Permite que todas las clases derivadas mantengan una interfaz común y coherente.
Pregunta 2: ¿Cómo se demuestra el polimorfismo en este ejercicio?
Respuesta: A través de la sobreescritura del método en Coche y Bicicleta,
 cada objeto responde de manera diferente a la misma llamada de método.
Pregunta 3: ¿Podríamos agregar más clases de vehículos sin modificar Vehiculo?
Respuesta: Sí, simplemente creando nuevas clases que sobrescriban obtener_velocidad_maxima().
"""
