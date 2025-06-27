from ParteN1 import * 

# Aplicar 10% de descuento al Bolón Mixto
menu_restaurante['bolón mixto']['precio'] *= 0.9
print("\nSe aplico un descuento del 10% al bolón mixto.")

# Añadir nuevo plato del día: Encocado de Camarón
menu_restaurante['Encocado de Camaron'] = {
    'precio': 6.0,
    'ingredientes': ('arroz', 'camaron' , 'coco', 'sal', 'cilantro')
}
print("Plato del día: Encocado de Camaron.")

# Mostrar el menú actualizado con los cambios (descuento + nuevo plato)
mostrar_menu(menu_restaurante)

# Lista de platos especiales del día
especiales_del_dia = ['guatita', 'encebollado', 'ceviche de camaron']

print("\nESPECIALES DEL DIA")
for plato in especiales_del_dia:
    if plato in menu_restaurante:
        detalles = menu_restaurante[plato]
        print(f"\nPlato: {plato.title()}")
        print(f"Precio: ${detalles['precio']}")
        print(f"Ingredientes: {', '.join(detalles['ingredientes'])}")
