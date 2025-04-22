"""
Explicaciones adicionales

Sobrecarga de operadores: __add__

__add__ es un método especial invocado por el operador +.

Para retornar un nuevo objeto o valor al sumar instancias.

Si no se soporta el tipo, debe devolver NotImplemented.

Representación con __str__

__str__ define cómo se muestra el objeto cuando se imprime con print().

Facilita la lectura humana, evitando ver la referencia de memoria.

Decoradores y abc en abstracción

El módulo abc proporciona ABC (base de clases abstractas) y @abstractmethod.

Una clase que hereda de ABC y contiene métodos @abstractmethod no puede instanciarse hasta que todas las subclases implementen dichos métodos.

Ventajas:

Define un contrato claro (interfaz).

Obliga a las subclases a implementar los métodos esenciales.

Refuerza el diseño orientado a objetos y el polimorfismo.
"""