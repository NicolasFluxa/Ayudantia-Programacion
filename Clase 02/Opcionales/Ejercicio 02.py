"""
Ejercicio 2: Sistema de Inventario para una Tienda de Electrónicos
Contexto:
Una tienda de electrónicos necesita gestionar dispositivos y laptops, asegurando que sus datos cumplan estándares de calidad.
Requerimientos:

Dispositivos genéricos:

Todo dispositivo debe tener un modelo (texto de al menos 3 caracteres) y una marca.

Si el modelo es inválido (ej: "A"), el sistema debe rechazarlo.

Laptops:

Deben incluir RAM en GB, con valores permitidos: 4, 8, 16 o 32 GB.

Si se intenta asignar una RAM no permitida (ej: 64), se debe mostrar un error.
Objetivo del código:
Implementar encapsulamiento y herencia para:

La clase base DispositivoElectronico con validación de modelo.

La clase hija Laptop que herede el modelo y gestione la RAM con validaciones específicas.
"""

class DispositivoElectronico:
    def __init__(self, modelo, marca):
        # Constructor: inicializa modelo y marca
        self._modelo = modelo
        self._marca = marca

    def set_modelo(self, nuevo_modelo):
        # Setter: valida longitud mínima del modelo
        if len(nuevo_modelo) >= 3:
            self._modelo = nuevo_modelo
        else:
            print("Error: Modelo debe tener al menos 3 caracteres.")

class Laptop(DispositivoElectronico):
    def __init__(self, modelo, marca, ram_gb):
        # Constructor: hereda modelo y marca usando super()
        super().__init__(modelo, marca)
        self._ram_gb = ram_gb  # Atributo adicional

    def actualizar_ram(self, nueva_ram):
        # Método: valida que la RAM esté en opciones permitidas
        if nueva_ram in [4, 8, 16, 32]:
            self._ram_gb = nueva_ram
        else:
            print("RAM inválida. Opciones: 4, 8, 16, 32 GB.")

# Preguntas:
# 1. ¿Por qué actualizar_ram no es un setter tradicional?
#    R: Para incluir lógica específica de valores permitidos.
# 2. ¿Qué pasa si se asigna ram_gb = 64 al crear un objeto Laptop?
#    R: El error no se detecta hasta usar actualizar_ram().

# Ejemplo de uso:
laptop = Laptop("XPS13", "Dell", 8)
laptop.set_modelo("A")  # Error: Modelo inválido
laptop.actualizar_ram(64)  # Error: RAM inválida
