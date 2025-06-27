from ParteN2 import *

# 1. Error de IndexError
print("\nIndexError")
try:
    # Aquí se intenta acceder a un índice fuera del rango de la lista pedido_actual
    print(pedido_actual[10])
except IndexError as e:
      # Aquí se captura el error y muestra un mensaje en pantalla
    print(f"Error: {e}")

# 2. Error de Clave (KeyError)
print("\nKeyError")
try:
      # Lo que hace es que Intenta acceder a una clave que no existe en el diccionario
    print(menu_restaurante['conchas'])
except KeyError as e:
    print(f"Error: {e}")

# 3. Inmutabilidad de Tuplas (TypeError)
print("\nTypeError")
try:
      # Intenta modificar un elemento dentro de una tupla
    menu_restaurante['encebollado']['ingredientes'][0] = 'yuca' 
except TypeError as e:
    print(f"Error: {e}")