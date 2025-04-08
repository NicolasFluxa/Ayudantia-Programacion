
"""
Crea una jerarquía de clases en la que Vehiculo es la clase base que
define el método moverse().
Luego, crea dos clases derivadas (Coche y Bicicleta) que
sobreescriben el método moverse() para reflejar diferentes maneras
de desplazamiento.
"""

# Definición de la clase base 'Vehiculo'
class Vehiculo:
    def moverse(self):
        # Método base que indica que el vehículo se está moviendo de una forma no especificada
        return "El vehículo se desplaza de alguna forma"

# Clase 'Coche' que hereda de 'Vehiculo'
class Coche(Vehiculo):
    def moverse(self):
        # Sobreescritura: especifica el desplazamiento de un coche
        return "El coche se desplaza a alta velocidad sobre la carretera"

# Clase 'Bicicleta' que hereda de 'Vehiculo'
class Bicicleta(Vehiculo):
    def moverse(self):
        # Sobreescritura: especifica el desplazamiento de una bicicleta
        return "La bicicleta se desplaza pedaleando en la ciudad"

# Instanciación de objetos de cada tipo de vehículo
coche = Coche()
bicicleta = Bicicleta()

# Impresión del modo en que se mueve cada vehículo
print(coche.moverse())       # Muestra cómo se mueve el coche
print(bicicleta.moverse())   # Muestra cómo se mueve la bicicleta

"""
Pregunta 1:
¿Cuál es la ventaja de definir el método  en la clase base ?
Respuesta:
La ventaja es proporcionar una interfaz común para todos los tipos de vehículos, facilitando que se puedan manipular de forma uniforme, independientemente de su implementación específica de movimiento.
Pregunta 2:
¿Cómo se refleja el concepto de polimorfismo en las clases  y ?
Respuesta:
Se refleja en que cada una de estas clases sobreescribe el método  para describir de manera específica su propio estilo de desplazamiento, permitiendo que al invocar el mismo método se ejecute la función adecuada para cada tipo de vehículo.
Pregunta 3:
¿Qué diferencias observas en la implementación del método en cada subclase?
Respuesta:
La clase  implementa el método destacando la alta velocidad y el uso de la carretera, mientras que  lo implementa enfatizando el pedaleo y la movilidad en entornos urbanos.
"""