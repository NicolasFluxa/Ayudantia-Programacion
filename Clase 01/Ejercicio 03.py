"""
Ejercicio 3: Clase Termostato con Límites
Objetivo: Controlar valores dentro de un rango.
Pasos:

Crea la clase Termostato con un atributo privado _temperatura.

Define get_temperatura() y set_temperatura(nueva_temp).

En set_temperatura, valida que nueva_temp esté entre 10°C y 40°C.
"""


class Termostato:
    def __init__(self):
        # Inicializamos la temperatura con un valor predeterminado de 20°C
        self._temperatura = 20

    def get_temperatura(self):
        # Método getter: Devuelve la temperatura actual
        return self._temperatura

    def set_temperatura(self, nueva_temp):
        # Método setter: Permite establecer una nueva temperatura
        # La temperatura debe estar dentro del rango de 10°C a 40°C
        if 10 <= nueva_temp <= 40:
            self._temperatura = nueva_temp
        else:
            # Si el valor está fuera del rango, muestra un mensaje de error
            print("Temperatura debe estar entre 10°C y 40°C.")


# Importa la clase Termostato desde tu archivo o código fuente
# Crea una instancia de la clase
termostato = Termostato()

# Obtén la temperatura inicial
print("Temperatura inicial:", termostato.get_temperatura())

# Cambia la temperatura a un valor válido
termostato.set_temperatura(25)
print("Nueva temperatura:", termostato.get_temperatura())

# Intenta establecer una temperatura fuera del rango permitido
termostato.set_temperatura(50)  # Esto mostrará un mensaje de error


"""
¿Qué pasa si no limitamos la temperatura a un rango?

Si no se limita la temperatura, el termostato podría aceptar valores irreales (por ejemplo, negativos o superiores al punto de ebullición), lo que sería inconsistente con su propósito. Esto también podría generar errores en sistemas que dependen de valores válidos para operar correctamente.

¿Cómo podríamos agregar un método para aumentar/disminuir la temperatura en pasos?

Podríamos crear métodos como incrementar_temperatura(pasos) y disminuir_temperatura(pasos) que ajusten la temperatura en unidades específicas, validando que el resultado se mantenga dentro del rango permitido. Ejemplo:

def incrementar_temperatura(self, pasos):
    nueva_temp = self._temperatura + pasos
    if 10 <= nueva_temp <= 40:
        self._temperatura = nueva_temp
    else:
        print("Valor fuera del rango permitido.")

"""