
"""
Modela un sistema bancario con:

Una clase base Cuenta que encapsule el titular y el saldo (privados), e implemente métodos depositar(monto), retirar(monto) y un getter get_balance().

Dos subclases:

CuentaAhorro (atributo extra: tasa de interés, método aplicar_interes())

CuentaCorriente (atributo extra: límite de descubierto, sobreescribe retirar para permitir sobregiro)

Sobrecarga de:

__add__ para sumar saldos de dos cuentas (retorna un número).

__gt__ para comparar balances (>).

Manejo de una lista de cuentas para imprimir estados y compararlas.
"""
from abc import ABC

# 1. Clase base
class Cuenta(ABC):
    def __init__(self, titular, saldo_inicial=0):
        self.__titular = titular
        self.__balance = saldo_inicial

    def depositar(self, monto):
        if monto > 0:
            self.__balance += monto

    def retirar(self, monto):
        # Retiro estándar: no permite saldo negativo
        if 0 < monto <= self.__balance:
            self.__balance -= monto

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f"{self.__titular}: ${self.__balance:.2f}"

    # Sobrecarga de +
    def __add__(self, otra):
        if isinstance(otra, Cuenta):
            return self.__balance + otra.__balance
        return NotImplemented

    # Sobrecarga de >
    def __gt__(self, otra):
        if isinstance(otra, Cuenta):
            return self.__balance > otra.__balance
        return NotImplemented

# 2a. Cuenta de ahorro
class CuentaAhorro(Cuenta):
    def __init__(self, titular, saldo_inicial, tasa_interes):
        super().__init__(titular, saldo_inicial)
        self.__tasa = tasa_interes

    def aplicar_interes(self):
        interes = self.get_balance() * self.__tasa
        self.depositar(interes)

# 2b. Cuenta corriente
class CuentaCorriente(Cuenta):
    def __init__(self, titular, saldo_inicial, limite_descubierto):
        super().__init__(titular, saldo_inicial)
        self.__limite = limite_descubierto

    def retirar(self, monto):
        # Permite sobregiro hasta el límite
        if monto > 0 and monto <= self.get_balance() + self.__limite:
            # Acceder al balance privado de la clase base
            self._Cuenta__balance -= monto

# --- Uso cotidiano ---
if __name__ == "__main__":
    c1 = CuentaAhorro("Ana", 1000, 0.02)
    c2 = CuentaCorriente("Luis", 200, 500)

    # Operaciones
    c1.depositar(200)
    c1.aplicar_interes()
    c2.retirar(600)  # Usa sobregiro
    c2.depositar(100)

    cuentas = [c1, c2]
    for c in cuentas:
        print(c)

    # Comparar y sumar
    print("¿Ana tiene más que Luis?", c1 > c2)
    print("Total fondos banco:", c1 + c2)


"""
¿De qué manera se logra el encapsulamiento del saldo, y por qué se accede a self._Cuenta__balance en CuentaCorriente?

El atributo __balance es privado en la clase Cuenta, inaccesible directamente fuera de ella.

Python lo “manglea” a _Cuenta__balance, así que para modificarlo en la subclase (CuentaCorriente) debe usarse esa forma, garantizando que nadie sobrescriba el saldo sin pasar por los métodos adecuados.

Explique cómo CuentaAhorro y CuentaCorriente usan el mismo método retirar de forma diferente (polimorfismo).

CuentaAhorro conserva el comportamiento base (no permite saldo negativo).

CuentaCorriente sobrescribe retirar para permitir sobregiros hasta un límite, cambiando la lógica interna.

Ambas responden a la misma llamada cuenta.retirar(monto), pero con implementaciones distintas.

¿Qué devuelven las sobrecargas __add__ y __gt__ cuando se usan c1 + c2 y c1 > c2?

c1 + c2 devuelve la suma numérica de ambos saldos (float o int).

c1 > c2 devuelve un booleano indicando si el balance de c1 es mayor que el de c2.
"""
