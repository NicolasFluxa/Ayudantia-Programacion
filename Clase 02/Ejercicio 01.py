
"""
Ejercicio 1: Clase Vehiculo y Coche (Herencia)
Objetivo: Crear una jerarquía de clases usando herencia y super().
Requerimientos:

Clase Vehiculo:

Atributos privados: _marca (str), _modelo (str).

Constructor: Inicializa _marca y _modelo.

Métodos: get_marca(), get_modelo(), set_marca(), set_modelo().

Clase Coche (hereda de Vehiculo):

Atributo privado adicional: _kilometraje (int, inicial 0).

Constructor: Usa super() para heredar atributos del padre.

Métodos: get_kilometraje(), actualizar_kilometraje(nuevos_km) que sume kilómetros válidos (no negativos).
"""
class Vehiculo:
    def __init__(self, marca, modelo):
        # Constructor: Inicializa atributos privados _marca y _modelo
        self._marca = marca
        self._modelo = modelo

    # Getter para obtener la marca del vehículo
    def get_marca(self):
        return self._marca

    # Getter para obtener el modelo del vehículo
    def get_modelo(self):
        return self._modelo

    # Setter para modificar la marca con validación de tipo y contenido
    def set_marca(self, nueva_marca):
        if isinstance(nueva_marca, str) and nueva_marca.strip() != "":
            # strip() elimina espacios vacíos al inicio/final
            self._marca = nueva_marca.strip()
        else:
            print("Error: La marca debe ser un texto no vacío.")

    # Setter para modificar el modelo con validación de tipo y contenido
    def set_modelo(self, nuevo_modelo):
        if isinstance(nuevo_modelo, str) and nuevo_modelo.strip() != "":
            self._modelo = nuevo_modelo.strip()
        else:
            print("Error: El modelo debe ser un texto no vacío.")


class Coche(Vehiculo):
    def __init__(self, marca, modelo):
        # super() llama al constructor de la clase padre (Vehiculo)
        super().__init__(marca, modelo)
        self._kilometraje = 0  # Atributo privado adicional

    # Getter para obtener el kilometraje
    def get_kilometraje(self):
        return self._kilometraje

    # Método para actualizar el kilometraje con validación de valores positivos
    def actualizar_kilometraje(self, nuevos_km):
        if nuevos_km >= 0:
            self._kilometraje += nuevos_km
        else:
            print("Error: Kilometraje no puede ser negativo.")

"""
¿Por qué se usa super().__init__() en la clase Coche?
Para heredar e inicializar los atributos _marca y _modelo definidos en la clase padre Vehiculo, evitando repetir código.

¿Qué ocurriría si en set_marca no se usara strip()?
Se permitirían marcas con espacios al inicio/final (ej: " Toyota "), lo que generaría inconsistencia en los datos.
"""

# Crear un coche
mi_coche = Coche("Toyota", "Corolla")

# Mostrar datos heredados
print(f"Marca: {mi_coche.get_marca()}")         # Toyota
print(f"Modelo: {mi_coche.get_modelo()}")       # Corolla

# Actualizar kilometraje válido
mi_coche.actualizar_kilometraje(150)
print(f"Kilometraje: {mi_coche.get_kilometraje()} km")  # 150

# Intentar kilómetros negativos (error)
mi_coche.actualizar_kilometraje(-50)            # Error: Kilometraje no puede ser negativo.
