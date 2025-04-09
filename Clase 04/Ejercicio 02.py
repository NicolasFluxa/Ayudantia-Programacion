
"""
Define una clase Dispositivo con un método encender().
Luego, crea dos clases derivadas Telefono y Computadora,
cada una con su propia implementación del método encender().
Este ejercicio muestra cómo diferentes dispositivos pueden compartir
la misma interfaz de método pero con comportamientos distintos.
"""

# Definición de la clase base 'Dispositivo'
class Dispositivo:
    def encender(self):
        raise NotImplementedError("Este método debe ser implementado en una subclase")

# Clase 'Telefono' que hereda de 'Dispositivo'
class Telefono(Dispositivo):
    def encender(self):
        return "El teléfono se enciende y muestra la pantalla de inicio."

# Clase 'Computadora' que hereda de 'Dispositivo'
class Computadora(Dispositivo):
    def encender(self):
        return "La computadora arranca y carga el sistema operativo."

# Creación de instancias de dispositivos
telefono = Telefono()
computadora = Computadora()

# Impresión del encendido de cada dispositivo
print(telefono.encender())  # "El teléfono se enciende..."
print(computadora.encender())  # "La computadora arranca..."

"""
Pregunta 1: ¿Por qué Dispositivo tiene el método encender() sin implementación?
Respuesta: Porque Dispositivo actúa como una clase base abstracta, 
dejando que sus subclases definan su propia lógica de encendido.
Pregunta 2: ¿Cómo demuestra este código el concepto de polimorfismo?
Respuesta: Porque Telefono y Computadora sobrescriben encender() con su 
propia implementación, permitiendo que cada dispositivo tenga un comportamiento único.
Pregunta 3: ¿Qué pasaría si agregamos una nueva clase Tablet con su propia versión de encender()?
Respuesta: Se integraría perfectamente dentro del sistema sin afectar otras clases, 
gracias a la estructura polimórfica del diseño.
"""
