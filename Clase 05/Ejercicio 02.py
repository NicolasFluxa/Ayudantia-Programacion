
"""
Ejercicio 5: Calculadora Flexible con Sobrecarga de Métodos Simulada
Enunciado:
Crea una clase Calculadora que contenga un método llamado multiplicar()
que sea capaz de recibir una cantidad variable de argumentos utilizando *args.

Este método debe multiplicar todos los números recibidos como argumento.
Si no se recibe ninguno, debe retornar 1 (la identidad multiplicativa).

Este ejercicio simula la sobrecarga de métodos en Python (ya que no se puede
hacer como en otros lenguajes como Java o C++), aprovechando el uso de *args.
También refuerza el concepto de funciones flexibles y manejo de tuplas.
"""

class Calculadora:
    def multiplicar(self, *args):
        """
        Multiplica todos los argumentos recibidos.
        Si no se pasan, devuelve 1 (identidad multiplicativa).
        """
        resultado = 1
        for n in args:
            resultado *= n
        return resultado

# Ejemplos de uso
calc = Calculadora()
print(calc.multiplicar(2, 3))       # 6
print(calc.multiplicar(2, 3, 4))    # 24
print(calc.multiplicar(5))          # 5
print(calc.multiplicar())           # 1 (ningún argumento)

"""
Preguntas y respuestas

¿Por qué multiplicar(5) no da error?

Porque *args acepta cero o más valores; con uno, el bucle multiplica 1 * 5 = 5.

¿Qué retorna multiplicar() sin args?

1, la identidad de la multiplicación.

¿Cómo sería la versión con parámetros fijos a, b=1, c=1?

def multiplicar(self, a, b=1, c=1):
    return a * b * c

"""