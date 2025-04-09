
"""
Define una clase base Transporte con un método modo_transporte().
Luego, crea dos clases derivadas Avion y Barco, donde cada una sobrescriba
el método para indicar cómo se transporta cada uno. Este ejercicio demuestra cómo
distintos medios de transporte pueden compartir la misma interfaz de método con
diferentes implementaciones.
"""



# Definición de la clase base 'Transporte'
class Transporte:
    def modo_transporte(self):
        raise NotImplementedError("Este método debe ser implementado en una subclase")

# Clase 'Avion' que hereda de 'Transporte'
class Avion(Transporte):
    def modo_transporte(self):
        return "El avión vuela por el cielo."

# Clase 'Barco' que hereda de 'Transporte'
class Barco(Transporte):
    def modo_transporte(self):
        return "El barco navega por el océano."

# Creación de instancias de transporte
avion = Avion()
barco = Barco()

# Impresión del modo de transporte de cada vehículo
print(avion.modo_transporte())  # "El avión vuela por el cielo."
print(barco.modo_transporte())  # "El barco navega por el océano."

"""
Pregunta 1: ¿Por qué la clase Transporte define modo_transporte() sin implementación?
Respuesta: Para asegurarse de que todas las clases derivadas implementen su
propia versión del método, siguiendo el principio del polimorfismo.
Pregunta 2: ¿Qué sucedería si Avion y Barco no sobrescriben modo_transporte()?
Respuesta: Se generaría un error al intentar llamar al método, ya que Transporte
no tiene una implementación concreta.
Pregunta 3: ¿Cómo podríamos extender esta implementación para incluir más medios de transporte?
Respuesta: Creando nuevas clases que hereden de Transporte y sobrescriban modo_transporte() con su propia lógica.
"""
