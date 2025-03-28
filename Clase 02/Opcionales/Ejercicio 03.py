"""
Ejercicio 3: Sistema de Reservas para un Hotel de Lujo
Contexto:
Un hotel boutique necesita administrar reservas de habitaciones estándar y suites de lujo, evitando errores en los datos.
Requerimientos:

Reservas estándar:

Deben registrar el número de habitación y una lista de huéspedes (nombres no vacíos).

Los nombres con espacios vacíos (ej: " Ana ") deben limpiarse automáticamente.

Suites de lujo:

Deben incluir servicios adicionales (ej: "Jacuzzi", "Desayuno gourmet").

No se permiten servicios duplicados en la misma suite.
Objetivo del código:
Usar herencia y el método super() para:

La clase base ReservaHotel que gestione huéspedes con validaciones.

La clase hija ReservaSuite que herede la funcionalidad base y agregue servicios sin duplicados.
"""

class ReservaHotel:
    def __init__(self, num_habitacion):
        # Constructor: inicializa número de habitación y lista de huéspedes
        self._num_habitacion = num_habitacion
        self._huespedes = []  # Atributo privado

    def agregar_huesped(self, nombre):
        # Método: valida que el nombre no esté vacío (usa strip())
        if nombre.strip() != "":
            self._huespedes.append(nombre.strip())

class ReservaSuite(ReservaHotel):
    def __init__(self, num_habitacion, servicios):
        # Constructor: hereda num_habitacion y agrega servicios
        super().__init__(num_habitacion)
        self._servicios = servicios.copy()  # Evita modificar la lista original

    def agregar_servicio(self, servicio):
        # Método: evita agregar servicios duplicados
        if servicio not in self._servicios:
            self._servicios.append(servicio)

# Preguntas:
# 1. ¿Por qué se usa servicios.copy() en el constructor?
#    R: Para evitar que cambios en la lista externa afecten al objeto.
# 2. ¿Qué pasa si agregar_huesped("   ") recibe espacios vacíos?
#    R: El método ignora el nombre (strip() lo convierte en cadena vacía).

# Ejemplo de uso:
suite = ReservaSuite(101, ["Jacuzzi"])
suite.agregar_huesped("  Ana  ")  # Nombre válido: "Ana"
suite.agregar_servicio("Jacuzzi")  # No se agrega (duplicado)
print(suite._servicios)  # ["Jacuzzi"]