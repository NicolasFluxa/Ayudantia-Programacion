
"""
Define una clase Electrodomestico con un método encender().
Luego, define otra clase Conectividad con un método conectar_wifi().
Finalmente, crea una clase Televisor que herede de ambas,
mostrando cómo funciona la herencia múltiple y el polimorfismo.
"""



# Definición de la clase base 'Electrodomestico'
class Electrodomestico:
    def encender(self):
        return "El electrodoméstico se ha encendido."

# Definición de la clase 'Conectividad'
class Conectividad:
    def conectar_wifi(self):
        return "El dispositivo está conectado a WiFi."

# Clase 'Televisor' con herencia múltiple
class Televisor(Electrodomestico, Conectividad):
    def encender(self):
        return "El televisor se ha encendido y está listo para usarse."

# Creación de instancia de Televisor
tv = Televisor()

# Uso de métodos heredados
print(tv.encender())  # "El televisor se ha encendido..."
print(tv.conectar_wifi())  # "El dispositivo está conectado a WiFi."

"""
Pregunta 1: ¿Qué ventaja tiene la herencia múltiple en este caso?
Respuesta: Permite que Televisor combine funcionalidades de
Electrodomestico y Conectividad sin necesidad de redefinirlas desde cero.
Pregunta 2: ¿Qué sucede si Televisor no sobrescribe encender()?
Respuesta: Se usaría la versión de Electrodomestico, aunque podríamos
personalizarla con una implementación específica.
Pregunta 3: ¿Cuándo puede ser problemática la herencia múltiple en Python?
Respuesta: Puede generar conflictos si dos clases base tienen métodos con el
mismo nombre, lo que llevaría a ambigüedades en la ejecución del código.
"""
