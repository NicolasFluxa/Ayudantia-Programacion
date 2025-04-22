
"""
Define una clase base Electrodomestico con un método consumo_energia().
Luego, crea dos clases derivadas Refrigerador y Lavadora, donde cada una
sobrescriba el método para calcular su consumo de energía específico.
Este ejercicio muestra cómo distintos electrodomésticos pueden compartir
la misma interfaz de método pero con valores particulares.
"""

# Definición de la clase base 'Electrodomestico'
class Electrodomestico:
    def consumo_energia(self):
        raise NotImplementedError("Este método debe ser implementado en una subclase")

# Clase 'Refrigerador' que hereda de 'Electrodomestico'
class Refrigerador(Electrodomestico):
    def consumo_energia(self):
        return "El refrigerador consume 150 kWh al mes."

# Clase 'Lavadora' que hereda de 'Electrodomestico'
class Lavadora(Electrodomestico):
    def consumo_energia(self):
        return "La lavadora consume 250 kWh al mes."

# Creación de instancias de electrodomésticos
refrigerador = Refrigerador()
lavadora = Lavadora()
# electrodomestico = Electrodomestico()

# Impresión del consumo de energía de cada electrodoméstico
print(refrigerador.consumo_energia())  # "El refrigerador consume 150 kWh al mes."
print(lavadora.consumo_energia())  # "La lavadora consume 250 kWh al mes."
# print(electrodomestico.consumo_energia())
"""
Pregunta 1: ¿Por qué Electrodomestico define consumo_energia() sin implementación?
Respuesta: Porque actúa como una clase base abstracta, dejando que cada subclase 
implemente su propio cálculo de consumo energético.
Pregunta 2: ¿Cómo se aplica el polimorfismo en este ejercicio?
Respuesta: Al definir consumo_energia() en la clase base y permitir que cada subclase 
sobrescriba su implementación según el electrodoméstico.
Pregunta 3: ¿Qué ventaja tiene estructurar una jerarquía como esta en lugar de manejar 
cada electrodoméstico por separado?
Respuesta: Permite un diseño más modular y reutilizable, facilitando la expansión con 
nuevos electrodomésticos sin modificar el código base.
"""
