
"""
Define una clase MetodoPago con un método procesar_pago().
Luego, crea dos clases derivadas TarjetaCredito y PayPal, donde cada una sobrescriba
el método para reflejar su proceso de pago específico. Este ejercicio ilustra cómo
distintas formas de pago pueden implementar un método de forma única pero compartiendo la misma interfaz.
"""

# Definición de la clase base 'MetodoPago'
class MetodoPago:
    def procesar_pago(self, monto):
        raise NotImplementedError("Este método debe ser implementado en una subclase")

# Clase 'TarjetaCredito' que hereda de 'MetodoPago'
class TarjetaCredito(MetodoPago):
    def procesar_pago(self, monto):
        return f"Pago de ${monto} procesado con tarjeta de crédito."

# Clase 'PayPal' que hereda de 'MetodoPago'
class PayPal(MetodoPago):
    def procesar_pago(self, monto):
        return f"Pago de ${monto} procesado con PayPal."

# Creación de instancias de métodos de pago
tarjeta = TarjetaCredito()
paypal = PayPal()

# Procesamiento de pagos con diferentes métodos
print(tarjeta.procesar_pago(100))  # "Pago de $100 procesado con tarjeta..."
print(paypal.procesar_pago(150))  # "Pago de $150 procesado con PayPal..."


"""
Pregunta 1: ¿Por qué procesar_pago() tiene diferentes implementaciones en TarjetaCredito y PayPal?
Respuesta: Porque cada forma de pago sigue un procedimiento diferente, 
por lo que requieren implementaciones personalizadas.
Pregunta 2: ¿Cómo ayuda el polimorfismo en este caso?
Respuesta: Permite que distintos métodos de pago sean tratados de manera 
uniforme, sin necesidad de modificar el código cada vez que se agregue uno nuevo.
Pregunta 3: ¿Podríamos extender esta implementación para incluir más métodos de pago, 
como Criptomonedas?
Respuesta: Sí, simplemente creando una nueva clase que sobrescriba procesar_pago(), 
manteniendo la estructura polimórfica del programa.
"""
