# EJEMPLO 1:

shift = 3 # Definir el recuento de turnos

text = "HELLO"

encryption = ""

for c in text:

    # Comprobar si el carácter es una letra mayúscula.
    if c.isupper():

        # Encontrar la posición en 0-25
        c_unicode = ord(c)

        c_index = ord(c) - ord("A")

        # Realizar el turno
        new_index = (c_index + shift) % 26

        # Convertir a nueva personaje
        new_unicode = new_index + ord("A")

        new_character = chr(new_unicode)

        # Anexar a la cadena encriptada
        encryption = encryption + new_character

    else:

        # Dado que el carácter no está en mayúsculas, déjelo como está.
        encryption += c
        
print("Plain text:",text)

print("Cipher text:",encryption)


# EJEMPLO 2:

shift = 3 # Definir el recuento de turnos

text = "hello, world"

encryption = ""

for c in text:

    # Comprobar si el carácter es una letra mayúscula.
    if c.isupper():

        # Encontrar la posición en 0-25
        c_unicode = ord(c)

        c_index = ord(c) - ord("A")

        # Realizar el turno
        new_index = (c_index + shift) % 26

        # Convertir a nueva personaje
        new_unicode = new_index + ord("A")

        new_character = chr(new_unicode)

        # Anexar a la cadena encriptada
        encryption = encryption + new_character

    else:

        # Dado que el carácter no está en mayúsculas, déjelo como está.
        encryption += c
        
print("Plain text:",text)

print("Cipher text:",encryption)