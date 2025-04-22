
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