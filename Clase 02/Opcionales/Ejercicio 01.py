"""
Ejercicio 1: Sistema de Gestión de Animales para un Zoológico
Contexto:
Un zoológico necesita un sistema digital para registrar información de sus animales, enfocándose en especies terrestres.
Requerimientos:

Datos básicos:

Todos los animales deben tener un nombre (no vacío) y una especie (texto válido).

El nombre debe limpiarse de espacios vacíos al inicio/final (ej: " León " → "León").

Animales terrestres:

Deben registrar el número de patas (entero positivo mayor a 0).

Si se intenta asignar un valor inválido (negativo, cero o no numérico), el sistema debe mostrar un error.
Objetivo del código:
Crear una jerarquía de clases usando herencia, donde:

La clase base Animal gestione nombre y especie con validaciones.

La clase hija AnimalTerrestre herede estos atributos y agregue el manejo de patas.
"""

class Animal:
    def __init__(self, nombre, especie):
        # Constructor de la clase base: inicializa nombre y especie
        self._nombre = nombre  # Atributo privado
        self._especie = especie

    def get_nombre(self):
        # Getter: retorna el nombre del animal
        return self._nombre

    def set_nombre(self, nuevo_nombre):
        # Setter: valida que el nombre no sea vacío (usa strip() para limpiar espacios)
        if nuevo_nombre.strip() != "":
            self._nombre = nuevo_nombre.strip()
        else:
            print("Error: Nombre no puede estar vacío.")

class AnimalTerrestre(Animal):
    def __init__(self, nombre, especie, patas):
        # Constructor de la clase hija: usa super() para heredar atributos del padre
        super().__init__(nombre, especie)
        self._patas = patas  # Atributo adicional

    def get_patas(self):
        # Getter: retorna el número de patas
        return self._patas

    def set_patas(self, nuevas_patas):
        # Setter: valida que las patas sean un número positivo
        if nuevas_patas > 0:
            self._patas = nuevas_patas
        else:
            print("Error: Patas deben ser mayor a 0.")

# Preguntas:
# 1. ¿Por qué AnimalTerrestre no valida nombre y especie en su constructor?
#    R: Porque hereda los setters de Animal, que ya incluyen validaciones.
# 2. ¿Qué pasa si creo un AnimalTerrestre con patas = "cuatro"?
#    R: Error, ya que el método espera un número entero.

# Ejemplo de uso:
tigre = AnimalTerrestre("  Tigre  ", "Felino", 4)
tigre.set_patas(-3)  # Error: Patas deben ser mayor a 0.
print(tigre.get_nombre())  # "Tigre" (strip() elimina espacios)