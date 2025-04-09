# Definición de la clase 'Persona'
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo nombre
        self.edad = edad      # Atributo edad

    def __str__(self):
        # Define la representación en cadena del objeto
        return f"Persona: {self.nombre}, Edad: {self.edad}"

    def mostrar(self, nombre, edad):
        print(f"Persona: {self.nombre}, Edad: {self.edad}")

# Creación de una instancia de Persona
persona = Persona("Nicolás", 25)

# Imprimimos el objeto
print(persona)  # Salida: Persona: Nicolás, Edad: 25
persona.mostrar("nombre", "edad")