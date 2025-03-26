"""
Ejercicio 3: Clase Usuario
Instrucciones:

Crea una clase Usuario con _email y _contraseña.

Valida en set_email() que el email contenga "@" y "." después de este.

En set_contraseña(), verifica que la contraseña tenga al menos 8 caracteres.
"""

class Usuario:
    def __init__(self, email, contraseña):
        self._email = None
        self._contraseña = None
        self.set_email(email)
        self.set_contraseña(contraseña)

    def get_email(self):
        return self._email

    def set_email(self, nuevo_email):
        # Valida que el email tenga "@" y un "." después
        if "@" in nuevo_email:
            partes = nuevo_email.split("@", 1)
            dominio = partes[1]
            if "." in dominio:
                self._email = nuevo_email
            else:
                print("Error: El dominio después de @ debe contener un '.'.")
        else:
            print("Error: El email debe contener '@'.")

    def get_contraseña(self):
        return self._contraseña

    def set_contraseña(self, nueva_contraseña):
        # Valida longitud mínima de 8 caracteres
        if len(nueva_contraseña) >= 8:
            self._contraseña = nueva_contraseña
        else:
            print("Error: La contraseña debe tener al menos 8 caracteres.")


usuario1 = Usuario("ana@example.com", "12345678")  # Válido
print(usuario1.get_email())  # "ana@example.com"

usuario2 = Usuario("error.com", "abc")  # Inválido
# Salida:
# Error: El email debe contener '@'.
# Error: La contraseña debe tener al menos 8 caracteres.



"""
¿Qué pasa si no validamos el formato del email?

Sin validación, podríamos aceptar emails incorrectos (por ejemplo, sin un dominio o el símbolo @). Esto podría causar problemas en sistemas que dependen de direcciones válidas para enviar información o autenticar usuarios.

¿Cómo podríamos mejorar la seguridad de la contraseña?

Podríamos implementar validaciones más estrictas, como requerir un mínimo de caracteres, incluir números, letras mayúsculas y minúsculas, y al menos un carácter especial. También podríamos añadir un método para encriptar contraseñas antes de almacenarlas.
"""