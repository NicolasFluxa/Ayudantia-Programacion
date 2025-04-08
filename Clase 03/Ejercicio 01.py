
"""
Crea una clase base llamada Animal con un método hacer_sonido().
Luego, define dos clases derivadas, Perro y Gato,
que sobreescriban el método para devolver sonidos específicos.
"""

# Definición de la clase base 'Animal'
class Animal:
    def hacer_sonido(self):
        # Método de la clase base que retorna un sonido genérico.
        return "Sonido genérico"

# Definición de la clase 'Perro' que hereda de 'Animal'
class Perro(Animal):
    def hacer_sonido(self):
        # Sobreescritura del método: el perro emite su propio sonido.
        return "Guau! Guau!"

# Definición de la clase 'Gato' que hereda de 'Animal'
class Gato(Animal):
    def hacer_sonido(self):
        # Sobreescritura del método: el gato emite su propio sonido.
        return "Miau! Miau!"

# Creación de instancias para cada clase
perro = Perro()   # Objeto de la clase Perro
gato = Gato()     # Objeto de la clase Gato

# Llamada al método polimórfico 'hacer_sonido' para cada objeto
print("El perro dice:", perro.hacer_sonido())  # Imprime el sonido específico del perro
print("El gato dice:", gato.hacer_sonido())      # Imprime el sonido específico del gatosaje)
# ¡Mismo método, distintos canales!


"""
Pregunta 1:
¿Qué significa que se sobreescriba el método  en las clases  y ?
Respuesta:
Significa que cada clase derivada proporciona una implementación propia del método,
 adaptándolo a su comportamiento específico,
  en lugar de utilizar la versión genérica definida en la clase base .
Pregunta 2:
¿Qué se imprimirá al ejecutar este código y por qué?
Respuesta:
Se imprimirán los sonidos específicos de cada animal — "Guau! Guau!" 
para el perro y "Miau! Miau!" para el gato — ya que cada objeto llama 
a su respectiva implementación del método .
Pregunta 3:
¿Por qué es útil definir un método común en la clase base al aplicar el polimorfismo?
Respuesta:
Es útil porque se establece una interfaz común para
todos los objetos de la jerarquía, lo que permite tratarlos de
manera uniforme y facilita la extensión y el mantenimiento del 
código al reutilizar el mismo método, aunque cada clase lo implemente
de forma distinta.
"""