
"""
Crea una clase base llamada "Intrumento" con el método "tocar()".
Luego, define dos clases derivadas: "Guitarra y Piano", donde cada una sobreescribe el
método "tocar()" para reflejar una forma distinta de
"tocar" el instrumento.
"""

# Definición de la clase base 'Instrumento'
class Instrumento:
    def tocar(self):
        # Método base que indica que el instrumento se está tocando
        return "El instrumento está siendo tocado"

# Clase 'Guitarra' que hereda de 'Instrumento'
class Guitarra(Instrumento):
    def tocar(self):
        # Sobreescritura: la guitarra emite acordes específicos
        return "La guitarra emite acordes vibrantes"

# Clase 'Piano' que hereda de 'Instrumento'
class Piano(Instrumento):
    def tocar(self):
        # Sobreescritura: el piano reproduce notas elegantes
        return "El piano emite notas elegantes"

# Creación de instancias para cada instrumento
guitarra = Guitarra()
piano = Piano()

# Impresión de los sonidos al tocar cada instrumento
print(guitarra.tocar())  # Salida propia de la guitarra
print(piano.tocar())     # Salida propia del piano

"""
Pregunta 1:
¿En qué se diferencian las implementaciones del método  en las clases  y ?
Respuesta:
La clase  implementa  devolviendo una cadena que describe la emisión de "acordes vibrantes", mientras que la clase  lo hace describiendo la emisión de "notas elegantes", reflejando la forma única en que cada instrumento es tocado.
Pregunta 2:
¿Cómo ayuda este ejemplo a comprender el polimorfismo en Python?
Respuesta:
Ilustra que, al utilizar el mismo método () en distintas instancias, cada una ejecuta su propia versión,
lo que permite que objetos diferentes se comporten de manera particular frente a la misma llamada de método.
Pregunta 3:
¿Qué ventaja tiene tener un método común en la clase base para ser reutilizado y adaptado en diferentes subclases?
Respuesta:
Permite definir una interfaz unificada y consistente que puede ser extendida o modificada en cada subclase, favoreciendo la reutilización de código y simplificando la integración de nuevos comportamientos sin alterar la estructura general.
"""