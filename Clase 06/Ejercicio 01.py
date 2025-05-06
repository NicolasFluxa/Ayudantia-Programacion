
"""
Implementa un sistema de carrito de compras que maneje productos de distintos tipos:
Una clase abstracta Producto que encapsule nombre y precio en atributos privados,
 y defina un método detalles() (interfaz).
Dos subclases concretas:
Alimento (atributo extra: fecha de caducidad)
Electronico (atributo extra: garantía en meses)
Una clase Carrito que:
Almacene los productos en una lista privada.
Tenga métodos para agregar productos, mostrar detalles y calcular el total.
Sobrecargue el operador + para:
Añadir un Producto a un Carrito (devuelve un nuevo carrito).
Combinar dos carritos en uno (concatenando sus listas).
Sobrecargue __len__ para devolver el número de ítems.
"""
from abc import ABC, abstractmethod
from datetime import date

# 1. Clase base abstracta
class Producto(ABC):
    def __init__(self, nombre, precio):
        self.__nombre = nombre    # Atributo privado
        self.__precio = precio    # Atributo privado

    @property
    def nombre(self):
        return self.__nombre

    @property
    def precio(self):
        return self.__precio

    @abstractmethod
    def detalles(self):
        """Retorna una cadena con información del producto."""
        pass

# 2a. Subclase Alimento
class Alimento(Producto):
    def __init__(self, nombre, precio, caducidad: date):
        super().__init__(nombre, precio)
        self.__caducidad = caducidad  # Atributo privado específico

    def detalles(self):
        return (f"Alimento: {self.nombre} — ${self.precio:.2f} "
                f"(caduca: {self.__caducidad.isoformat()})")

# 2b. Subclase Electronico
class Electronico(Producto):
    def __init__(self, nombre, precio, garantia_meses: int):
        super().__init__(nombre, precio)
        self.__garantia = garantia_meses

    def detalles(self):
        return (f"Electrónico: {self.nombre} — ${self.precio:.2f} "
                f"(garantía: {self.__garantia} meses)")

# 3. Carrito de compras
class Carrito:
    def __init__(self):
        self.__items = []  # Lista privada de Productos

    def agregar(self, producto: Producto):
        self.__items.append(producto)

    def mostrar_items(self):
        for p in self.__items:
            print(p.detalles())

    def total(self):
        return sum(p.precio for p in self.__items)

    # Sobrecarga del operador +
    def __add__(self, otro):
        if isinstance(otro, Producto):
            nuevo = Carrito()
            nuevo.__items = self.__items.copy()
            nuevo.__items.append(otro)
            return nuevo
        if isinstance(otro, Carrito):
            nuevo = Carrito()
            nuevo.__items = self.__items.copy() + otro.__items.copy()
            return nuevo
        return NotImplemented

    # Sobrecarga de len()
    def __len__(self):
        return len(self.__items)

# --- Uso cotidiano ---
if __name__ == "__main__":
    # Crear algunos productos
    leche = Alimento("Leche", 1.20, date(2025, 5, 10))
    tv = Electronico("Televisor", 399.99, 24)

    # Carrito inicial
    carrito1 = Carrito()
    carrito1.agregar(leche)
    carrito1.agregar(tv)
    print("Carrito 1:")
    carrito1.mostrar_items()
    print("Total:", carrito1.total())
    print("Cantidad de ítems:", len(carrito1))
    print("-" * 40)

    # Usando + para agregar un producto
    pan = Alimento("Pan", 0.80, date(2025, 4, 30))
    carrito2 = carrito1 + pan
    print("Carrito 2 (añadido Pan):")
    carrito2.mostrar_items()
    print("Total:", carrito2.total())
    print("-" * 40)

    # Combinar dos carritos
    otro = Carrito()
    otro.agregar(Electronico("Auriculares", 29.99, 12))
    combinado = carrito2 + otro
    print("Carrito combinado:")
    combinado.mostrar_items()
    print("Total combinado:", combinado.total())


"""
¿Cómo garantiza el código el encapsulamiento de nombre y precio en Producto, y por qué es útil?

Se usan atributos privados (self.__nombre, self.__precio) en la clase base y sólo se exponen a través de propiedades de sólo lectura (@property).

Esto impide que el código externo modifique directamente esos valores, protegiendo la integridad del producto y permitiendo controlar cualquier validación o lógica adicional al exponerlos.

¿Qué hace exactamente la llamada a detalles() en cada subclase y cómo refleja el polimorfismo?

Cada subclase (Alimento y Electronico) implementa su propia versión de detalles(), incluyendo información específica (fecha de caducidad o meses de garantía).

Cuando detalles() se invoca sobre una referencia de tipo Producto, Python ejecuta la implementación correspondiente al objeto real (ej. si es un Alimento o un Electronico), demostrando polimorfismo mediante una interfaz común.

Explique cómo funciona la sobrecarga de __add__ para añadir tanto un Producto como otro Carrito.

Si el operando derecho es un Producto, se crea un nuevo Carrito clonando la lista interna y añadiendo ese producto.

Si el operando derecho es otro Carrito, se crea un nuevo Carrito con la concatenación de ambas listas internas.

De esta forma carrito + producto o carrito1 + carrito2 devuelven siempre instancias nuevas sin alterar los originales.
"""

