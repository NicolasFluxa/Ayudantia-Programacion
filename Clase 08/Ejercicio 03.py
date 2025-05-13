
"""
Enunciado
Construye un sistema de inventario donde los productos pueden ser simples, empacados o con descuento, y exista la posibilidad de crear combos. Integra listas, sobrecarga de operadores, herencia múltiple y manejo de errores.

Define ProductoSimple(nombre, precio) y ProductoEmpacado(nombre, precio, costo_empaque), ambos con método costo().

Crea un mixin DescuentoMixin(descuento) con aplicar_descuento(monto).

Implementa ProductoDescontado por herencia múltiple de ProductoSimple y DescuentoMixin, sobreescribiendo costo() para aplicar el descuento.

Crea Combo(nombre, descuento) (hereda de DescuentoMixin), mantiene lista de ProductoSimple/ProductoEmpacado/ProductoDescontado, método agregar(item) y costo_total() que recorre lista con try/except y suma item.costo(), luego aplica el descuento del combo.

En Inventario, mantiene lista de combos y productos; sobrecarga __add__ para añadir un Producto o combinar dos inventarios, y en __len__, retorna total de ítems. Usa try/except en __add__ para validar tipos.
"""
from abc import ABC, abstractmethod

# 1. Productos básicos
class ProductoSimple:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def costo(self):
        return self.precio

class ProductoEmpacado(ProductoSimple):
    def __init__(self, nombre, precio, costo_empaque):
        super().__init__(nombre, precio)
        self.costo_empaque = costo_empaque

    def costo(self):
        return self.precio + self.costo_empaque

# 2. Mixin de descuento
class DescuentoMixin:
    def __init__(self, descuento):
        self.descuento = descuento  # ej. 0.15 = 15%

    def aplicar_descuento(self, monto):
        return monto * (1 - self.descuento)

# 3. Producto con descuento (múltiple herencia)
class ProductoDescontado(ProductoSimple, DescuentoMixin):
    def __init__(self, nombre, precio, descuento):
        ProductoSimple.__init__(self, nombre, precio)
        DescuentoMixin.__init__(self, descuento)

    def costo(self):
        base = super().costo()
        return self.aplicar_descuento(base)

# 4. Combo de productos
class Combo(DescuentoMixin):
    def __init__(self, nombre, descuento):
        DescuentoMixin.__init__(self, descuento)
        self.nombre = nombre
        self.items = []  # lista de productos

    def agregar(self, item):
        self.items.append(item)

    def costo_total(self):
        total = 0
        for p in self.items:
            try:
                total += p.costo()
            except Exception as e:
                print(f"Error calculando costo de {p.__class__.__name__}: {e}")
        return self.aplicar_descuento(total)

# 5. Inventario con sobrecarga y manejo de errores
class Inventario:
    def __init__(self):
        self.elementos = []  # combos y productos

    def __add__(self, otro):
        try:
            if isinstance(otro, (ProductoSimple, ProductoEmpacado, ProductoDescontado, Combo)):
                nuevo = Inventario()
                nuevo.elementos = self.elementos.copy()
                nuevo.elementos.append(otro)
                return nuevo
            if isinstance(otro, Inventario):
                nuevo = Inventario()
                nuevo.elementos = self.elementos.copy() + otro.elementos.copy()
                return nuevo
            raise TypeError("Tipo no soportado en Inventario")
        except TypeError as e:
            print("Error al añadir al inventario:", e)
            return self

    def __len__(self):
        return len(self.elementos)

# Prueba de uso
if __name__ == "__main__":
    inv = Inventario()
    inv = inv + ProductoSimple("Lapicero", 1.0)
    inv = inv + ProductoEmpacado("Café", 3.0, 0.5)
    inv = inv + ProductoDescontado("Cuaderno", 2.0, 0.1)
    combo = Combo("Desayuno", 0.20)
    combo.agregar(ProductoSimple("Bagel", 2.5))
    combo.agregar(ProductoEmpacado("Mantequilla", 1.0, 0.2))
    # Forzamos error: obj sin costo()
    combo.agregar("NoProducto")
    print("Costo combo:", combo.costo_total())
    inv = inv + combo
    inv2 = Inventario()
    inv2 = inv2 + combo
    total = inv + inv2
    print("Total elementos inventario:", len(total))

"""
Pregunta 1
¿Cómo valida Inventario.__add__ que solo se añadan tipos permitidos y qué ocurre si no?
Respuesta
Usa isinstance(otro, ...); si no es válido, lanza TypeError que captura e imprime el error, y retorna el inventario original.

Pregunta 2
¿De qué forma Combo.costo_total() gestiona productos inválidos en su lista?
Respuesta
Dentro del bucle usa try/except en cada p.costo(), capturando excepción e imprimiendo error, permitiendo seguir sumando los demás.

Pregunta 3
Explique cómo ProductoDescontado combina lógica de precio base y descuento.
Respuesta
Hereda el cálculo base de ProductoSimple y llama a aplicar_descuento del mixin para reducir el monto devuelto.
"""