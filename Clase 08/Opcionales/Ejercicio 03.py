"""
Enunciado
Crea Persona(nombre, edad) y Estudiante(nombre, edad, carrera), extendiendo descripcion().

Usa try/except en el constructor de Persona para asegurar que edad sea un entero positivo.
"""

class Persona:
    def __init__(self, nombre, edad):
        try:
            if not (isinstance(edad, int) and edad >= 0):
                raise ValueError("Edad debe ser entero ≥ 0")
            self.nombre = nombre
            self.edad = edad
        except ValueError as e:
            print("Error en Persona:", e)
            # Valor por defecto para seguir
            self.nombre = nombre
            self.edad = 0

    def descripcion(self):
        return f"{self.nombre}, {self.edad} años"

class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera

    def descripcion(self):
        base = super().descripcion()
        return f"{base}, estudia {self.carrera}"

# Prueba
if __name__ == "__main__":
    p = Persona("Juan", -5)           # Captura ValueError
    print(p.descripcion())            # Edad toma 0
    e = Estudiante("Ana", 20, "I.T.")
    print(e.descripcion())

"""
Pregunta 1
¿Qué valor de edad queda en la instancia p tras el error?
Respuesta
0, asignado en el except.

Pregunta 2
¿Por qué seguimos instanciando Persona tras el error en edad?
Respuesta
Porque el except atrapa el error y asigna valores por defecto, permitiendo que la construcción continúe.

Pregunta 3
¿Cómo podrías loguear el error en lugar de imprimirlo?
Respuesta
Importando logging y usando logging.error(e) dentro del except.
"""