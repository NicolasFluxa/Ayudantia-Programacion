

"""
Define una clase base Mascota con un método moverse().
Luego, crea dos clases derivadas Perro y Pez, donde cada una
sobrescriba el método para indicar cómo se mueve cada mascota.
Este ejercicio muestra cómo diferentes mascotas pueden compartir
la misma interfaz de método pero con acciones distintas.
"""


# Definición de la clase base 'Mascota'
class Mascota:
    def moverse(self):
        raise NotImplementedError("Este método debe ser implementado en una subclase")

# Clase 'Perro' que hereda de 'Mascota'
class Perro(Mascota):
    def moverse(self):
        return "El perro corre por el parque."

# Clase 'Pez' que hereda de 'Mascota'
class Pez(Mascota):
    def moverse(self):
        return "El pez nada en el agua."

# Creación de instancias de mascotas
perro = Perro()
pez = Pez()

# Impresión del movimiento de cada mascota
print(perro.moverse())  # "El perro corre por el parque."
print(pez.moverse())  # "El pez nada en el agua."


"""
Pregunta 1: ¿Por qué Mascota tiene un método sin implementación?
Respuesta: Para establecer una interfaz común que todas las subclases deben cumplir,
garantizando que cada mascota tenga su propia forma de moverse.
Pregunta 2: ¿Cómo ayuda el polimorfismo en este caso?
Respuesta: Permite que diferentes mascotas respondan a la misma llamada de método
(moverse()), adaptando su comportamiento según el tipo de mascota.
Pregunta 3: ¿Cómo podríamos agregar más mascotas con sus propias formas de moverse?
Respuesta: Creando nuevas clases que hereden de Mascota y sobrescriban moverse() con
su propio movimiento.
"""
