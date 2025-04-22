Aquí tienes el enunciado actualizado con las nuevas características integradas:

---

# 🏦 BancoPy: Sistema de Gestión de Cuentas Bancarias y Tarjetas con Autentificación y Registro de Transacciones

Desarrolla un modelo en Python orientado a objetos que simule el funcionamiento básico de un banco. El sistema debe gestionar cuentas bancarias, tarjetas asociadas, operaciones entre ellas, y además implementar un registro de cada transacción y un sistema de autentificación para garantizar el acceso seguro a las operaciones.

---

## 🔐 Sistema de Autentificación

- **Objetivo:**  
  Antes de ejecutar operaciones sensibles (como depósitos, retiros, transferencias y pagos con tarjeta), se debe verificar la identidad del usuario.

- **Requisitos:**  
  - **Clase `Usuario`:**  
    - **Atributos:**  
      - `nombre_usuario` (str).  
      - `contraseña` (str), que idealmente se almacene de forma hasheada para mayor seguridad.
    - **Métodos:**  
      - `login(contraseña: str) -> bool`: Verifica la contraseña y autentica al usuario.  
      - `logout()`: Finaliza la sesión actual.
  - Cada objeto `CuentaBancaria` debe estar asociada a un objeto `Usuario` y requerir la autentificación antes de procesar operaciones críticas.  
  - Se deberán lanzar excepciones en caso de que un usuario intente realizar una operación sin haberse autenticado correctamente.

---

## 📝 Registro de Transacciones

- **Objetivo:**  
  Registrar todas las operaciones realizadas en el sistema para fines de auditoría y seguimiento.

- **Requisitos:**  
  - **Clase `Transaccion`:**  
    - **Atributos:**  
      - `fecha_hora`: Marca temporal de la operación (puede utilizarse `datetime.now()` para ello).  
      - `tipo`: Tipo de operación (ej. depósito, retiro, transferencia, pago con tarjeta, etc.).  
      - `monto`: Monto asociado a la transacción.  
      - `descripcion`: Detalles adicionales (por ejemplo, número de cuenta origen y destino).
  - Cada vez que se invoque un método que modifique el estado de una cuenta o se ejecute un pago, se debe crear y almacenar un registro de la transacción.
  - El registro puede almacenarse en una estructura central (como un log global) o asociado a cada cuenta, según lo que se desee enfatizar en el diseño.

---

## ✅ Clases de Cuentas

Crea una clase base `CuentaBancaria` y las subclases `CuentaAhorros`, `CuentaCorriente` y `CuentaVista`.

### 🔹 CuentaBancaria (base)

- **Atributos privados:**
  - `__titular`: Nombre del titular (str).  
  - `__saldo`: Saldo actual (float), inicia en 0.0.  
  - `__numero_cuenta`: Número aleatorio entre 8 y 9 dígitos (int).

- **Métodos:**
  - `depositar(monto: float)`: Agrega monto al saldo. Si `monto ≤ 0`, lanza `ValueError`.
  - `retirar(monto: float)`: Descuenta monto del saldo. Si `monto ≤ 0` o `monto > saldo`, lanza `ValueError`.
  - `mostrar_saldo()`: Retorna el saldo actual.
  - `tipo_cuenta()`: Retorna `"Genérica"`.
  - `transferir(destino: CuentaBancaria, monto: float)`: Transfiere monto a otra cuenta; debe realizar internamente un `retirar` en la cuenta origen y un `depositar` en la cuenta destino.
  - **Integración con Transacciones:** Cada método que modifique el saldo debe generar un objeto `Transaccion` con la información correspondiente.

### 🔹 CuentaAhorros

- **Hereda de:** `CuentaBancaria`.

- **Atributo privado:**
  - `__interes`: Tasa de interés (float), por ejemplo 0.02.

- **Métodos:**
  - `tipo_cuenta()`: Retorna `"Ahorros"`.
  - `aplicar_interes()`: Incrementa el saldo multiplicándolo por `(1 + interes)` y registra la operación como transacción.

### 🔹 CuentaCorriente

- **Hereda de:** `CuentaBancaria`.

- **Atributo privado:**
  - `__linea_credito`: Monto adicional permitido como descubierto (float), por defecto 500_000.0.

- **Métodos:**
  - `tipo_cuenta()`: Retorna `"Corriente"`.
  - `retirar(monto: float)`: Permite que el saldo baje hasta `-__linea_credito`. Si `monto ≤ 0` o `monto > saldo + linea_credito`, lanza `ValueError`.

> **Nota:** La cuenta corriente es la única que permite una tarjeta de crédito. Para la tarjeta de débito, el saldo disponible es la suma del saldo de la cuenta y la línea de crédito.

### 🔹 CuentaVista

- **Hereda de:** `CuentaBancaria`.

- **Atributos privados:**
  - `__limite_diario`: Máximo que se puede girar en un día (float), por ejemplo 1_000_000.0.
  - `__gastos_transferencia`: Comisión fija por transferencia (float), por ejemplo 300.0.
  - `__retirado_hoy`: Acumulado de retiros del día (float), inicia en 0.0.

- **Métodos:**
  - `tipo_cuenta()`: Retorna `"Vista"`.
  - `retirar(monto: float)`: Valida que el total retirado en el día no supere el límite y descuenta la comisión por transferencia, registrando la transacción correspondiente.
  - `reset_limite_diario()`: Reinicia el monto retirado del día para simular el inicio de una nueva jornada.

---

## 💳 Clases de Tarjetas

Crea una clase base `Tarjeta` y las subclases `TarjetaDebito` y `TarjetaCredito`.

### 🔸 Tarjeta (base)

- **Atributos privados:**
  - `__titular`: Cuenta bancaria asociada (`CuentaBancaria`).
  - `__numero`: Número de tarjeta aleatorio de 16 dígitos (str).

- **Métodos:**
  - `mostrar_numero()`: Devuelve el número de la tarjeta.

### 🔸 TarjetaDebito

- **Hereda de:** `Tarjeta`.

- **Método:**
  - `pagar(monto: float)`: Utiliza el método `retirar()` de la cuenta asociada. Si no alcanza el saldo (y la línea de crédito, en el caso de `CuentaCorriente`), lanza `ValueError` y registra la transacción.

### 🔸 TarjetaCredito

- **Restricción:** Solo puede asociarse a una `CuentaCorriente`.

- **Atributos privados:**
  - `__limite`: Máximo permitido, por defecto 500_000.0.
  - `__saldo_utilizado`: Inicia en 0.0.

- **Métodos:**
  - `pagar(monto: float)`: Si el monto supera el límite restante, lanza `ValueError` y registra la transacción.
  - `mostrar_saldo_credito()`: Muestra el saldo utilizado.

---

## 🔧 Funciones de Operación

Implementa dos funciones separadas para gestionar operaciones en cuentas y tarjetas:

### Función `administrar_cuenta`

- **Firma:**  
  `administrar_cuenta(cuenta: CuentaBancaria, depositos: list[float], retiros: list[float], transferencias: list[tuple[CuentaBancaria, float]])`

- **Operaciones a realizar:**  
  - Muestra información relevante de la cuenta (tipo, titular, número, etc.).  
  - Ejecuta depósitos y retiros (capturando y gestionando los posibles errores de operación o de autentificación).  
  - Realiza transferencias a otras cuentas.  
  - Si la cuenta es de ahorro, aplica los intereses correspondientes.  
  - Cada operación exitosa deberá crear un registro en el sistema de transacciones.  
  - Muestra el saldo final de la cuenta.

### Función `operar_tarjetas`

- **Firma:**  
  `operar_tarjetas(tarjetas: list[Tarjeta], pagos: list[float])`

- **Operaciones a realizar:**  
  - Para cada tarjeta y monto, ejecuta el pago correspondiente (capturando errores y verificando la autenticación cuando sea necesario).  
  - En caso de ser una tarjeta de débito, muestra el saldo actualizado de la cuenta.  
  - Si se trata de una tarjeta de crédito, muestra el saldo utilizado.  
  - Cada pago deberá quedar registrado como transacción en el sistema.

---

Este enunciado ahora integra, además de los conceptos de herencia, encapsulamiento y polimorfismo, un sistema completo de autentificación y un registro detallado de transacciones que harán el ejercicio aún más realista y retador para los alumnos.  
¿Te gustaría profundizar en algún ejemplo de implementación o discutir alguna de estas partes en mayor detalle?