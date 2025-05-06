
"""
Diseña una pequeña clase contenedora Numeros que gestione internamente una lista de enteros y permita la sobrecarga de operadores:

__add__: si se suma a un entero, lo agrega al final de la lista; si se suma con otro Numeros, combina ambas listas.

__len__: devuelve cuántos elementos hay.
"""

class Numeros:
    def __init__(self, datos=None):
        # Inicializa la lista, por defecto vacía
        self.datos = datos if datos is not None else []

    def __add__(self, otro):
        # Si it's un entero...
        if isinstance(otro, int):
            # Devuelve nuevo objeto con copia de la lista + el entero
            return Numeros(self.datos + [otro])
        # Si es otra instancia de Numeros...
        if isinstance(otro, Numeros):
            return Numeros(self.datos + otro.datos)
        return NotImplemented  # Si no soportamos el tipo

    def __len__(self):
        # Longitud de la lista interna
        return len(self.datos)

# Ejemplo de uso
n1 = Numeros([1, 2, 3])
n2 = Numeros([4, 5])
n3 = n1 + 6           # [1,2,3,6]
n4 = n1 + n2          # [1,2,3,4,5]
print(n3.datos, len(n3))
print(n4.datos, len(n4))

"""
Pregunta 1
¿Qué retorna n1 + "hola" y por qué?
Respuesta
Devuelve NotImplemented, y Python luego lanzará un TypeError, pues no soportamos concatenar con string.

Pregunta 2
¿Cómo cambiarías __add__ para que también acepte tuplas de enteros?
if isinstance(otro, tuple):
    return Numeros(self.datos + list(otro))
    
Pregunta 3
¿Por qué es importante devolver un nuevo objeto en cada operación __add__?
Respuesta
Para no mutar el objeto original, manteniendo la inmutabilidad funcional y evitando efectos colaterales.

"""