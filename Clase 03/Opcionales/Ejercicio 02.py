
"""
Demuestra cómo el polimorfismo se aplica a los métodos especiales
de Python mediante la sobreescritura del método __str__.
Crea una clase base Empleado con un formato básico al imprimir
el objeto y una clase derivada Gerente que agrega información adicional,
 como el departamento. Al imprimir los objetos, se utilizará la versión
 sobreescrita de __str__.
"""

# Definición de la clase base 'Empleado'
class Empleado:
    def __init__(self, nombre, puesto):
        # Inicializa el nombre y puesto del empleado
        self.nombre = nombre   # Atributo que almacena el nombre
        self.puesto = puesto   # Atributo que almacena el puesto

    def __str__(self):
        # Método especial que define la representación en cadena del objeto
        return f"Empleado: {self.nombre}, Puesto: {self.puesto}"

# Definición de la clase 'Gerente' que hereda de 'Empleado'
class Gerente(Empleado):
    def __init__(self, nombre, puesto, departamento):
        # Llama al constructor de la clase base para inicializar nombre y puesto
        super().__init__(nombre, puesto)
        # Atributo adicional para el departamento del gerente
        self.departamento = departamento

    def __str__(self):
        # Sobreescritura de __str__ para incluir la información del departamento
        return f"Gerente: {self.nombre}, Puesto: {self.puesto}, Departamento: {self.departamento}"

# Creación de instancias de Empleado y Gerente
empleado = Empleado("Juan", "Analista")
gerente = Gerente("María", "Jefa", "Finanzas")

# Al imprimir cada objeto se invoca automáticamente su método __str__
print(empleado)  # Representación en cadena del objeto Empleado
print(gerente)   # Representación en cadena del objeto Gerente, con información extra

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