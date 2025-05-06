"""
Enunciado
Diseña un sistema de inventario con distintos tipos de productos y sobrecarga de operadores.
Crea una clase abstracta Producto con atributos nombre y precio, y método costo() abstracto.

Implementa:
ProductoSimple (solo nombre, precio).
ProductoEmpacado (añade costo_empaque y su costo() suma ambos).
Crea un mixin DescuentoMixin que reciba porcentaje y ofrezca método aplicar_descuento(monto).
Define ProductoDescontado que herede de ProductoSimple y DescuentoMixin, y su costo() aplique el descuento.
Construye la clase Inventario que lleve una lista de productos, métodos agregar() y total(), y sobrecargue:
__add__ para añadir un Producto o combinar dos inventarios.
__len__ para contar productos.
"""


from abc import ABC, abstractmethod

# 1. Producto abstracto
class Producto(ABC):
    def __init__(self, nombre, precio):
        self.nombre = nombre           # Nombre del producto
        self.precio = precio           # Precio base

    @abstractmethod
    def costo(self):
        # Debe retornar coste final
        pass

# 2a. Producto simple
class ProductoSimple(Producto):
    def costo(self):
        return self.precio             # Solo precio base

# 2b. Producto con empaque
class ProductoEmpacado(Producto):
    def __init__(self, nombre, precio, costo_empaque):
        super().__init__(nombre, precio)
        self.costo_empaque = costo_empaque  # Coste adicional

    def costo(self):
        return self.precio + self.costo_empaque

# 3. Mixin de descuento
class DescuentoMixin:
    def __init__(self, descuento):
        self.descuento = descuento     # Ej. 0.10 para 10%

    def aplicar_descuento(self, monto):
        return monto * (1 - self.descuento)

# 4. Producto descontado (múltiple herencia)
class ProductoDescontado(ProductoSimple, DescuentoMixin):
    def __init__(self, nombre, precio, descuento):
        ProductoSimple.__init__(self, nombre, precio)
        DescuentoMixin.__init__(self, descuento)

    def costo(self):
        # Primer coste base
        base = super().costo()
        # Aplica descuento
        return self.aplicar_descuento(base)

# 5. Inventario con lista y sobrecargas
class Inventario:
    def __init__(self):
        self.items = []                # Lista interna

    def agregar(self, producto):
        self.items.append(producto)    # Añade un producto

    def total(self):
        return sum(p.costo() for p in self.items)

    def __add__(self, otro):
        if isinstance(otro, Producto):
            nuevo = Inventario()
            nuevo.items = self.items.copy()
            nuevo.items.append(otro)
            return nuevo
        if isinstance(otro, Inventario):
            nuevo = Inventario()
            nuevo.items = self.items.copy() + otro.items.copy()
            return nuevo
        return NotImplemented

    def __len__(self):
        return len(self.items)

# Uso de métodos de lista:
# - copy() para clonar la lista sin modificar la original
# - sum(... for ...) para sumar dinámicamente los costos

if __name__ == "__main__":
    inv = Inventario()
    inv = inv + ProductoSimple("Lapicero", 1.5)
    inv = inv + ProductoEmpacado("Café", 3.0, 0.5)
    inv2 = Inventario()
    inv2.agregar(ProductoDescontado("Taza", 5.0, 0.2))
    combinado = inv + inv2
    print("Total inventario combinado:", combinado.total())
    print("Cantidad productos:", len(combinado))


"""
Pregunta 1
¿Cómo se implementa la herencia múltiple en ProductoDescontado y qué obtiene con ello?
Respuesta
Hereda de ProductoSimple para obtener nombre/precio y de DescuentoMixin para la lógica de descuento; así combina ambas funcionalidades.

Pregunta 2
¿Por qué Inventario.__add__ usa self.items.copy() antes de añadir o concatenar?
Respuesta
Para clonar la lista y no mutar el inventario original, respetando la inmutabilidad funcional.

Pregunta 3
¿Qué método de Python permite sumar de forma concisa todos los costos en total()?
Respuesta
La función sum() junto con una comprensión generadora: sum(p.costo() for p in self.items).


"""