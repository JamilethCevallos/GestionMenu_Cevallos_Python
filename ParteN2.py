from ParteN1 import *

# Lista para almacenar los platos que el cliente selecciona
pedido_actual = []
# Variable para llevar el total acumulado del pedido
total_pago = 0

# Se muestra el menú de platos disponibles al usuario
mostrar_menu(menu_restaurante)

# Bucle que permite recibir varios platos del cliente
while True:
    entrada = input("\nPor favor coloca el nombre el plato o 'fin' si ya no deseas añadir más: ").lower()
    
    if entrada == 'fin':
        break # Salir del bucle si el usuario ha terminado su pedido
    elif entrada in menu_restaurante:
        pedido_actual.append(entrada) # Se agrega el nombre del plato a la lista
        total_pago+= menu_restaurante[entrada]['precio'] # Se suma su precio al total
        print(f"'{entrada.title()}' añadido al carrito")
    else:
        print("Lo sentimos, ese plato no está en el menú.")

# Mostrar el resumen del pedido una vez el cliente termina
print("\nRESUMEN DEL PEDIDO REALIZADO")
for plato in pedido_actual:
    print(f"- {plato.title()}") # Lista cada plato elegido
print(f"Total a pagar: ${total_pago}")  # Imprime el total acumulado