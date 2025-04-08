
"""
Ejercicio 2: Clase Persona y Estudiante (Herencia con Validaciones)
Objetivo: Heredar atributos y agregar validaciones específicas.
Requerimientos:

Clase Persona:

Atributos privados: _nombre (str), _edad (int).

Constructor y métodos getters/setters con validaciones básicas.

Clase Estudiante (hereda de Persona):

Atributo privado adicional: _carrera (str).

Método set_carrera() que valide que la carrera esté en una lista predefinida (ej: ["Ingeniería", "Medicina"]).
"""

class Persona:
    def __init__(self, nombre, edad):
        # Constructor: Inicializa atributos privados _nombre y _edad
        self._nombre = nombre
        self._edad = edad

    # Getter para obtener el nombre
    def get_nombre(self):
        return self._nombre

    # Getter para obtener la edad
    def get_edad(self):
        return self._edad

    # Setter para modificar el nombre con validación
    def set_nombre(self, nuevo_nombre):
        if isinstance(nuevo_nombre, str) and nuevo_nombre.strip() != "":
            self._nombre = nuevo_nombre.strip()
        else:
            print("Error: Nombre no válido.")

    # Setter para modificar la edad con validación de rango
    def set_edad(self, nueva_edad):
        if 0 <= nueva_edad <= 120:
            self._edad = nueva_edad
        else:
            print("Error: Edad debe estar entre 0 y 120.")


class Estudiante(Persona):
    CARRERAS_PERMITIDAS = ["Ingeniería", "Medicina", "Arquitectura"]

    def __init__(self, nombre, edad, carrera):
        # super() inicializa nombre y edad heredados de Persona
        super().__init__(nombre, edad)
        self.set_carrera(carrera)  # Valida la carrera al crearse

    # Getter para obtener la carrera del estudiante
    def get_carrera(self):
        return self._carrera

    # Setter para modificar la carrera con validación de opciones permitidas
    def set_carrera(self, nueva_carrera):
        if nueva_carrera.capitalize() in Estudiante.CARRERAS_PERMITIDAS:
            self._carrera = nueva_carrera
        else:
            print(f"Error: Carrera no válida. Opciones: {Estudiante.CARRERAS_PERMITIDAS}")

"""
¿Por qué se usa set_carrera en el constructor de Estudiante?
Para aprovechar la validación del setter y asegurar que la carrera sea válida al crear el objeto.

¿Qué pasa si no se define CARRERAS_PERMITIDAS como variable de clase?
La lista de carreras sería específica de cada objeto, lo que consumiría más memoria y dificultaría su mantenimiento.
"""

# Crear un estudiante válido
estudiante1 = Estudiante(" Ana López ", 22, "Medicina")

# Mostrar datos (strip() limpia espacios en el nombre)
print(f"Nombre: {estudiante1.get_nombre()}")    # "Ana López"
print(f"Carrera: {estudiante1.get_carrera()}")  # "Medicina"

# Intentar cambiar a carrera inválida
estudiante1.set_carrera("Física")               # Error: Carrera no válida.

# Validación de edad en setter
estudiante1.set_edad(150)                       # Error: Edad debe estar entre 0 y 120.
estudiante1.set_edad(25)                        # Éxito
print(f"Edad actualizada: {estudiante1.get_edad()}")  # 25