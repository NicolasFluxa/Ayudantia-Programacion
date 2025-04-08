
"""
Demuestra cómo el duck typing permite aplicar el polimorfismo en
Python sin necesidad de que las clases estén relacionadas por herencia.
Crea dos clases,  y , que implementen el método , y una función que
acepte un objeto cualquiera y llame a su método . Esto evidencia que,
mientras el objeto tenga el método requerido, éste se puede utilizar
de manera intercambiable.
"""

# Definición de la clase 'Pato'
class Pato:
    def volar(self):
        # Método que simula la forma en que un pato vuela
        return "El pato vuela de manera torpe pero efectiva."

# Definición de la clase 'Avion'
class Avion:
    def volar(self):
        # Método que simula la forma en que un avión vuela
        return "El avión vuela a gran velocidad por el cielo."

# Función que acepta cualquier objeto con el método 'volar' y lo utiliza
def hazlo_volar(objeto):
    # Llama al método 'volar' del objeto recibido y lo imprime
    print(objeto.volar())

# Creación de instancias de Pato y Avion
pato = Pato()
avion = Avion()

# Uso de la función 'hazlo_volar' con distintos tipos de objetos
hazlo_volar(pato)   # Se utiliza el método 'volar' definido en la clase Pato
hazlo_volar(avion)  # Se utiliza el método 'volar' definido en la clase Avion

"""
Ejemplo 5 (Polimorfismo con Métodos Especiales )
Pregunta 1:
¿Qué hace el método especial  y por qué es útil?
Respuesta:
El método  define la forma en que se representa un objeto en formato de cadena, facilitando su impresión y comprensión al mostrar información legible y detallada sobre el estado del objeto.
Pregunta 2:
¿Cómo difiere la salida de un objeto de la clase  de la de un objeto ?
Respuesta:
Un objeto de la clase  muestra únicamente el nombre y el puesto, mientras que un objeto  incluye información adicional como el departamento, lo que ofrece una representación más completa y detallada del objeto.
Pregunta 3:
¿Qué beneficios ofrece la sobreescritura de métodos especiales en el contexto del polimorfismo?
Respuesta:
Permite personalizar la forma en que se presentan y procesan los objetos, haciendo que cada clase pueda ofrecer una representación adaptada a sus características específicas, lo que mejora la claridad, la depuración y la interacción con el usuario.

"""