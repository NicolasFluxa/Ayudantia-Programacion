"""
Enunciado
Define una clase base Producto con método abstracto precio().

Subclases Libro y VideoJuego implementan precio().

En el método mostrar_precio(prod), usa try/except para capturar si precio() devolviera un valor no numérico.
"""

from abc import ABC, abstractmethod

class Producto(ABC):
    def __init__(self, titulo, precio_base):
        self.titulo = titulo
        self.precio_base = precio_base

    @abstractmethod
    def precio(self):
        pass  # Implementar en subclases

class Libro(Producto):
    def precio(self):
        return self.precio_base

class VideoJuego(Producto):
    def precio(self):
        return self.precio_base * 1.2

def mostrar_precio(prod):
    try:
        p = prod.precio()             # Puede fallar si precio() no retorna número
        if not isinstance(p, (int, float)):
            raise ValueError("Precio no es numérico")
        print(f"{prod.titulo} → ${p:.2f}")
    except Exception as e:
        print(f"Error mostrando precio de {prod.titulo}:", e)

# Prueba
if __name__ == "__main__":
    p1 = Libro("1984", 15.0)
    p2 = VideoJuego("Zelda", "sesenta")  # error intencional
    mostrar_precio(p1)
    mostrar_precio(p2)


"""
Pregunta 1
¿Qué captura el except cuando VideoJuego("Zelda", "sesenta").precio() falla?
Respuesta
Un TypeError al intentar multiplicar string * 1.2, o bien el ValueError si llega al chequeo de tipo.

Pregunta 2
¿Cómo ajustarías el except para manejar por separado TypeError y ValueError?
Respuesta
Usando dos bloques:
except TypeError as e:
    ...
except ValueError as e:
    ...
Pregunta 3
¿Qué imprimiría el programa para p2?
Respuesta
Error mostrando precio de Zelda: Precio no es numérico (o el mensaje del TypeError, dependiendo del orden de chequeo).
"""