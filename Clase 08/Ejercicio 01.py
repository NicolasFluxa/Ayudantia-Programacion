"""
Enunciado
Crea Empleado(nombre, sueldo) y Equipo que mantiene una lista de empleados.

__add__: suma sueldos o combina equipos.

Implementa try/except en __add__ de Equipo para capturar operaciones inválidas.

python
Copiar código
"""

class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

    def __add__(self, otro):
        try:
            if not isinstance(otro, Empleado):
                raise TypeError("Solo se pueden sumar Empleado")
            return self.sueldo + otro.sueldo
        except TypeError as e:
            print("Error sumando empleados:", e)
            return 0

class Equipo:
    def __init__(self, miembros=None):
        self.miembros = miembros if miembros else []

    def __add__(self, otro):
        try:
            if isinstance(otro, Empleado):
                return Equipo(self.miembros + [otro])
            if isinstance(otro, Equipo):
                return Equipo(self.miembros + otro.miembros)
            raise TypeError("Operando no soportado")
        except TypeError as e:
            print("Error en Equipo __add__:", e)
            return self  # devuelve el mismo equipo

    def __len__(self):
        return len(self.miembros)

# Prueba
if __name__ == "__main__":
    e1 = Empleado("Ana", 1000)
    e2 = Empleado("Luis", 1200)
    print("Suma sueldos:", e1 + e2)
    print("Suma inválida:", e1 + 5)     # Captura TypeError
    equipo = Equipo([e1])
    equipo2 = equipo + e2
    equipo3 = equipo + "otro"           # Captura TypeError
    print("Tamaño equipo:", len(equipo3))

"""
Pregunta 1
¿Qué imprime e1 + 5 en la consola?
Respuesta
Error sumando empleados: Solo se pueden sumar Empleado y luego 0.

Pregunta 2
¿Qué hace equipo + "otro" y qué devuelve?
Respuesta
Captura TypeError en Equipo.__add__, imprime el error y devuelve el mismo equipo original.

Pregunta 3
¿Por qué __add__ de Equipo retorna self tras el error en lugar de None?
Respuesta
Para mantener un objeto válido y evitar que se rompa la cadena de operaciones, devolviendo el estado anterior.
"""

