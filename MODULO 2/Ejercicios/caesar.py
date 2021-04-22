# Primero

shift = 3 # Definir el recuento de turnos

text = "CAESAR"

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



# siguiente

import string

def cipher_cipher_using_lookup(text,  key, characters = string.ascii_lowercase, decrypt=False):

    if key < 0:

        print("key cannot be negative")

        return None

    n = len(characters)

    if decrypt==True:

        key = n - key

    table = str.maketrans(characters, characters[key:]+characters[:key])
    
    translated_text = text.translate(table)
    
    return translated_text

