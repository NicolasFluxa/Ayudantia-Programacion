"""
Ejercicio 2: Clase Estudiante con Validaciones
Objetivo: Validar datos al modificar atributos.
Pasos:

Define la clase Estudiante con atributos privados _nombre y _matricula.

Crea métodos get_nombre() y get_matricula().

Crea un método set_nombre(nuevo_nombre) que verifique que nuevo_nombre no sea una cadena vacía.

Crea un método set_matricula(nueva_matricula) que asegure que nueva_matricula sea un número de 5 dígitos.
"""

class Estudiante:
    def __init__(self, nombre, matricula):
        # Inicializamos los atributos privados nombre y matrícula
        self.__nombre = nombre
        self.__matricula = matricula

    def get_nombre(self):
        # Método getter: Devuelve el nombre del estudiante
        return self._nombre

    def set_nombre(self, nuevo_nombre):
        # Método setter: Permite establecer un nuevo nombre
        # El nombre no puede estar vacío (se elimina espacios en blanco)
        if nuevo_nombre.strip() != "":
            self._nombre = nuevo_nombre.strip()
        else:
            # Si el nombre está vacío, muestra un mensaje de error
            print("Error: Nombre no puede estar vacío.")

    def get_matricula(self):
        # Método getter: Devuelve la matrícula del estudiante
        return self._matricula

    def set_matricula(self, nueva_matricula):
        # Método setter: Permite establecer una nueva matrícula
        # La matrícula debe ser un número de exactamente 5 dígitos
        if len(str(nueva_matricula)) == 5 and str(nueva_matricula).isdigit():
            self._matricula = nueva_matricula
        else:
            # Si la matrícula no cumple las condiciones, muestra un mensaje de error
            print("Matrícula debe ser un número de 5 dígitos.")


# Importa la clase Estudiante desde tu archivo o código fuente
# Crea una instancia de la clase
estudiante = Estudiante("Nicolás", 12345)

# Obtén el nombre y la matrícula del estudiante
print("Nombre:", estudiante.get_nombre())
print("Matrícula:", estudiante.get_matricula())

# Cambia el nombre a un valor válido
estudiante.set_nombre("Ana")
print("Nuevo nombre:", estudiante.get_nombre())

# Intenta establecer un nombre vacío
estudiante.set_nombre("")  # Esto mostrará un mensaje de error

# Cambia la matrícula a un número válido
estudiante.set_matricula(67890)
print("Nueva matrícula:", estudiante.get_matricula())

# Intenta establecer una matrícula inválida
estudiante.set_matricula("abc")  # Esto mostrará un mensaje de error



"""
¿Qué pasa si no validamos la longitud de la matrícula?

Si no se valida la matrícula, se podrían asignar valores incorrectos, como cadenas no numéricas o números con menos de cinco dígitos. Esto afectaría la funcionalidad de la clase y podría generar problemas si la matrícula es utilizada para identificar a los estudiantes en otros sistemas.

¿Cómo podríamos mejorar la validación del nombre?

Se podría añadir lógica que detecte caracteres no permitidos, como números o símbolos, asegurando que el nombre contenga únicamente letras y espacios. También se podría implementar un límite de longitud para evitar nombres excesivamente largos.
"""