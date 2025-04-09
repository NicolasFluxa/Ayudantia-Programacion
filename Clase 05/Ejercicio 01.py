
"""
Define una clase base Electrodomestico con un método descripcion().
Luego, crea dos clases derivadas Licuadora y Microondas, donde cada una
sobrescriba el método para mostrar una descripción específica del electrodoméstico.
Este ejercicio demuestra cómo distintas clases pueden compartir la misma
interfaz de método con diferentes implementaciones.
"""


# Definición de la clase base 'Electrodomestico'
class Electrodomestico:
    def descripcion(self):
        raise NotImplementedError("Este método debe ser implementado en una subclase")

# Clase 'Licuadora' que hereda de 'Electrodomestico'
class Licuadora(Electrodomestico):
    def descripcion(self):
        return "La licuadora mezcla y tritura alimentos."

# Clase 'Microondas' que hereda de 'Electrodomestico'
class Microondas(Electrodomestico):
    def descripcion(self):
        return "El microondas calienta y cocina alimentos rápidamente."

# Creación de instancias de electrodomésticos
licuadora = Licuadora()
microondas = Microondas()

# Impresión de la descripción de cada electrodoméstico
print(licuadora.descripcion())  # "La licuadora mezcla y tritura alimentos."
print(microondas.descripcion())  # "El microondas calienta y cocina alimentos rápidamente."


"""
Pregunta 1: ¿Por qué la clase Electrodomestico tiene un método sin implementación?
Respuesta: Para definir una interfaz común y garantizar que todas las subclases proporcionen su propia implementación.
Pregunta 2: ¿Cómo demuestra este código el concepto de polimorfismo?
Respuesta: Porque Licuadora y Microondas sobrescriben descripcion(), adaptándolo a sus propias funcionalidades.
Pregunta 3: ¿Qué pasaría si intentamos crear una instancia de Electrodomestico?
Respuesta: Se generaría un error porque la clase base no tiene una implementación concreta del método descripcion().
"""
