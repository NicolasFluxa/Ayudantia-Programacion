"""
Ejercicio 1: Clase CuentaBancaria
Objetivo: Crear una clase que gestione un saldo con métodos explícitos.
Pasos:

Define la clase CuentaBancaria con un atributo privado _saldo inicializado en 0.

Crea un método get_saldo() que retorne el valor de _saldo.

Crea un método set_saldo(nuevo_saldo) que asigne _saldo = nuevo_saldo solo si el valor es positivo.

Agrega un método depositar(monto) que sume al _saldo si monto > 0.
"""

class CuentaBancaria:
    def __init__(self):
        # Inicializamos el saldo de la cuenta bancaria con un valor de 0
        self._saldo = 0

    def get_saldo(self):
        # Método getter: Devuelve el saldo actual de la cuenta
        return self._saldo

    def set_saldo(self, nuevo_saldo):
        # Método setter: Permite establecer un nuevo saldo
        # El saldo debe ser mayor o igual a 0
        if nuevo_saldo >= 0:
            self._saldo = nuevo_saldo
        else:
            # Si el saldo es negativo, muestra un mensaje de error
            print("Error: Saldo no puede ser negativo.")

    def depositar(self, monto):
        # Método para depositar dinero en la cuenta
        # Solo se permite depositar montos positivos
        if monto > 0:
            self._saldo += monto


# Importa la clase CuentaBancaria desde tu archivo o código fuente
# Crea una instancia de la clase
cuenta = CuentaBancaria()

# Obtén el saldo inicial
print("Saldo inicial:", cuenta.get_saldo())

# Deposita dinero en la cuenta
cuenta.depositar(100)
print("Saldo después del depósito:", cuenta.get_saldo())

# Cambia el saldo a un valor válido
cuenta.set_saldo(200)
print("Saldo actualizado:", cuenta.get_saldo())

# Intenta establecer un saldo negativo
cuenta.set_saldo(-50)  # Esto mostrará un mensaje de error


"""
¿Qué pasa si no validamos el monto en depositar()?

Si no se valida el monto, el código podría aceptar valores negativos o no numéricos, lo que causaría inconsistencias en el saldo (por ejemplo, disminuirlo con depósitos negativos). Esto puede llevar a resultados inesperados y errores en el uso práctico de la clase.

¿Por qué es útil tener un método get_saldo()?

Este método permite acceder al saldo de forma controlada, sin exponer directamente el atributo privado _saldo. Esto fortalece la encapsulación, protege la integridad del dato y facilita la validación o modificaciones futuras sin afectar el funcionamiento del programa.
"""