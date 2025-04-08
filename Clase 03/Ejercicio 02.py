"""
Utilizando las clases definidas en el ejercicio anterior, crea una lista que contenga instancias de ,
  y una instancia directa de . Itera sobre la lista e invoca el método  en cada objeto.
   Este ejercicio refuerza cómo el polimorfismo permite utilizar una misma interfaz (en este caso, el método)
   en objetos de diferentes tipos.
"""

# Definición de la clase base 'Animal'
class Animal:
    def hacer_sonido(self):
        # Devuelve un sonido genérico
        return "Sonido genérico"

# Clase 'Perro' que hereda de 'Animal'
class Perro(Animal):
    def hacer_sonido(self):
        # Devuelve el sonido característico del perro
        return "Guau! Guau!"

# Clase 'Gato' que hereda de 'Animal'
class Gato(Animal):
    def hacer_sonido(self):
        # Devuelve el sonido característico del gato
        return "Miau! Miau!"

# Creación de una lista con diferentes tipos de animales
animales = [Perro(), Gato(), Animal()]

# Iteración sobre la lista: se llama al método 'hacer_sonido' de cada objeto
for animal in animales:
    # Al ejecutar 'hacer_sonido', cada objeto utiliza su propia implementación
    print(animal.hacer_sonido())


"""Pregunta 1:
¿Qué demuestra este ejercicio en relación al polimorfismo?
Respuesta:
Demuestra que, a pesar de que los objetos pertenezcan a clases diferentes, pueden responder al mismo método (), cada uno con su propia implementación, lo que es la esencia del polimorfismo.
Pregunta 2:
¿Por qué se pueden almacenar objetos de clases distintas en la misma lista y llamar al método  sin problemas?
Respuesta:
Porque Python es un lenguaje dinámico que permite trabajar con objetos heterogéneos siempre que estos compartan la interfaz o el método requerido, sin necesidad de tener una relación de herencia estricta para ser tratados de forma similar.
Pregunta 3:
¿Qué pasaría si una clase no sobreescribe el método y se usa la implementación de la clase base?
Respuesta:
Si una subclase no sobreescribe el método, se hereda la implementación de la clase base, por lo que se ejecutaría la versión genérica definida en  (por ejemplo, "Sonido genérico")."""