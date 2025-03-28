
"""
Ejercicio 3: Clase CuentaBancaria con Historial (Encapsulación)
Objetivo: Refinar la clase del Ejercicio 1 agregando un historial de transacciones.
Requerimientos:

Atributos privados: _saldo (float), _transacciones (lista de strings).

Métodos:

depositar(monto): Registra la operación en _transacciones.

retirar(monto): Valida que el saldo no sea negativo después de retirar.

get_historial(): Retorna las últimas 5 transacciones.
"""
class CuentaBancaria:
    def __init__(self):
        # Constructor: Inicializa saldo en 0 y lista de transacciones
        self._saldo = 0.0
        self._transacciones = []

    # Getter para obtener el saldo actual
    def get_saldo(self):
        return self._saldo

    # Método para depositar dinero y registrar la transacción
    def depositar(self, monto):
        if monto > 0:
            self._saldo += monto
            self._transacciones.append(f"Depósito: +${monto}")
        else:
            print("Error: El monto debe ser positivo.")

    # Método para retirar dinero con validación de fondos
    def retirar(self, monto):
        if 0 < monto <= self._saldo:
            self._saldo -= monto
            self._transacciones.append(f"Retiro: -${monto}")
        else:
            print("Error: Fondos insuficientes o monto inválido.")

    # Getter para obtener las últimas 5 transacciones
    def get_historial(self):
        return self._transacciones[-5:] if self._transacciones else []

"""
¿Por qué se usa self._transacciones[-5:] en get_historial()?
Para retornar solo las últimas 5 transacciones, usando slicing. Si la lista está vacía, retorna una lista vacía.

¿Qué ocurre si se deposita un monto negativo?
El método depositar imprime un error y no modifica el saldo ni el historial.
"""

# Crear una cuenta
cuenta_ana = CuentaBancaria()

# Depositar y retirar fondos
cuenta_ana.depositar(500)
cuenta_ana.depositar(200)
cuenta_ana.retirar(300)
print(f"Saldo: ${cuenta_ana.get_saldo()}")      # 400.0

# Intentar retiro inválido
cuenta_ana.retirar(500)                         # Error: Fondos insuficientes.

# Generar múltiples transacciones
cuenta_ana.depositar(100)
cuenta_ana.retirar(50)
cuenta_ana.depositar(300)

# Ver historial (últimas 5 transacciones)
print("Historial:", cuenta_ana.get_historial())
# Salida: ['Depósito: +$500', 'Depósito: +$200', 'Retiro: -$300', 'Depósito: +$100', 'Retiro: -$50']