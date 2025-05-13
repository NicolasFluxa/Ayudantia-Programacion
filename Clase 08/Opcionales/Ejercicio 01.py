"""
Enunciado
Crea una clase Contador que mantenga un valor interno (inicialmente 0).

Implementa métodos incrementar(), decrementar() y valor().

Agrega manejo de errores para detectar si alguien intenta usar un valor no entero como incremento o decremento, lanzando y capturando la excepción adecuada.
"""

class Contador:
    def __init__(self):
        self._valor = 0                  # Valor interno inicial

    def incrementar(self, paso=1):
        try:
            # Intentamos sumar un entero
            if not isinstance(paso, int):
                raise TypeError("Paso debe ser entero")
            self._valor += paso          # Aumenta el contador
        except TypeError as e:
            print("Error al incrementar:", e)

    def decrementar(self, paso=1):
        try:
            # Intentamos restar un entero
            if not isinstance(paso, int):
                raise TypeError("Paso debe ser entero")
            self._valor -= paso          # Disminuye el contador
        except TypeError as e:
            print("Error al decrementar:", e)

    def valor(self):
        return self._valor               # Devuelve el valor actual

# Prueba rápida
if __name__ == "__main__":
    c = Contador()
    c.incrementar(3)
    c.incrementar("dos")               # Captura TypeError
    c.decrementar()
    print("Valor final:", c.valor())

"""
Pregunta 1
¿Qué sucede cuando llamas c.incrementar("dos")?
Respuesta
Se lanza un TypeError("Paso debe ser entero") y el except lo captura, imprimiendo el mensaje de error.

Pregunta 2
¿Qué valor mostrará c.valor() al final del bloque de prueba?
Respuesta
1 (se sumó 2, el intento con string no cambió nada, y luego se restó 1).

Pregunta 3
¿Cómo modificarías el método incrementar para atrapar también valores como None o listas?
Respuesta
Al mismo if not isinstance(paso, int) ya cubre None y listas, pues no son instancias de int.
"""