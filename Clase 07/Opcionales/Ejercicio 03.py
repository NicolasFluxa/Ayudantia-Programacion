"""
Enunciado
Programa un sistema de menú y combos para un restaurante, que emplee listas,
polimorfismo, herencia múltiple y sobrecarga.
Crea la clase abstracta MenuItem con atributos nombre y precio_base,
y método precio_final() abstracto.
Implementa:
Plato: añade tiempo_preparacion, precio_final() = precio_base.
Bebida: añade volumen_ml, precio_final() = precio_base.
Define un mixin DescuentoCombo que reciba porcentaje y ofrezca aplica_combo(precio_total).
Implementa Combo con herencia múltiple (DescuentoCombo, MenuItem),
que contenga self.items (lista de MenuItem), y su precio_final() sume precio_final() de cada item y aplique el descuento.
Crea la clase Carta que aloje una lista de MenuItem, y sobrecargue:
__add__ para añadir un MenuItem o combinar dos cartas.
__len__ para contar ítems.
"""

from abc import ABC, abstractmethod

# 1. Item de menú abstracto
class MenuItem(ABC):
    def __init__(self, nombre, precio_base):
        self.nombre = nombre            # Nombre
        self.precio_base = precio_base  # Precio inicial

    @abstractmethod
    def precio_final(self):
        pass                          # Debe retornar precio final

# 2a. Plato concreto
class Plato(MenuItem):
    def __init__(self, nombre, precio_base, tiempo_preparacion):
        super().__init__(nombre, precio_base)
        self.tiempo_preparacion = tiempo_preparacion

    def precio_final(self):
        return self.precio_base       # No hay recargo adicional

# 2b. Bebida concreta
class Bebida(MenuItem):
    def __init__(self, nombre, precio_base, volumen_ml):
        super().__init__(nombre, precio_base)
        self.volumen_ml = volumen_ml

    def precio_final(self):
        return self.precio_base       # Sin recargo

# 3. Mixin de descuento para combos
class DescuentoCombo:
    def __init__(self, descuento):
        self.descuento = descuento     # Ej. 0.15 = 15%

    def aplica_combo(self, precio_total):
        return precio_total * (1 - self.descuento)

# 4. Combo con herencia múltiple
class Combo(DescuentoCombo, MenuItem):
    def __init__(self, nombre, descuento):
        DescuentoCombo.__init__(self, descuento)
        MenuItem.__init__(self, nombre, 0)
        self.items = []                # Lista de MenuItem

    def agregar(self, item):
        self.items.append(item)        # Añade Plato o Bebida

    def precio_final(self):
        total = sum(i.precio_final() for i in self.items)
        return self.aplica_combo(total)

# 5. Carta de restaurante
class Carta:
    def __init__(self):
        self.ofertas = []              # Lista de MenuItem

    def add(self, item):
        self.ofertas.append(item)

    def __add__(self, otro):
        if isinstance(otro, MenuItem):
            nueva = Carta()
            nueva.ofertas = self.ofertas.copy()
            nueva.ofertas.append(otro)
            return nueva
        if isinstance(otro, Carta):
            nueva = Carta()
            nueva.ofertas = self.ofertas.copy() + otro.ofertas.copy()
            return nueva
        return NotImplemented

    def __len__(self):
        return len(self.ofertas)

# Uso cotidiano
if __name__ == "__main__":
    c = Carta()
    c = c + Plato("Ensalada", 5.0, 10)
    c = c + Bebida("Agua", 1.5, 500)

    combo = Combo("Combo Ligero", 0.10)
    combo.agregar(Plato("Sándwich", 7.0, 5))
    combo.agregar(Bebida("Jugo", 2.5, 250))
    print("Precio combo:", combo.precio_final())
    carta2 = Carta()
    carta2.add(combo)

    carta_total = c + carta2
    print("Elementos en carta:", len(carta_total))


"""
Pregunta 1
¿Cómo usa Combo la herencia múltiple para combinar la lógica de MenuItem y DescuentoCombo?
Respuesta
Inicializa ambas bases (DescuentoCombo y MenuItem), luego en precio_final() suma precios de items y aplica el descuento del mixin.

Pregunta 2
¿Qué rol cumple la lista self.items en Combo y cómo se manipula?
Respuesta
Almacena los MenuItem del combo; se añade con append() y luego se recorre con sum(... for ...) para calcular el total.

Pregunta 3
Explique la sobrecarga de __add__ en Carta para sumar un MenuItem o dos Carta.
Respuesta
Si el operando es un MenuItem, clona la lista y añade el item; si es otra Carta, concatena ambas listas en un nuevo objeto.
"""
